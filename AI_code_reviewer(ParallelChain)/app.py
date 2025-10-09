import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
 
load_dotenv()
 
st.set_page_config(page_title="AI Code Reviewer", page_icon="💻")
st.title("AI Code Reviewer 🧠")
 

gemini_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
suggestions_model = HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",
    task="text-generation",
    model_kwargs={"max_length": 200}
)
 
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
code_review_model = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
    base_url=base_url
)
 
parser = StrOutputParser()
 
user_code = st.text_area("Paste your code here:", height=300)
 
if st.button("Review Code") and user_code.strip() != "":
    with st.spinner("Analyzing your code..."):
        code_truncated = user_code[:3000]
        review_template = PromptTemplate(
            template="You are an expert programmer. Review the following code and provide feedback, bug fixes, and suggestions for improvement:{code}",
            input_variables=["code"]
        )
 
        refactor_template = PromptTemplate(
            template="You are an expert programmer. Refactor the following code for better readability and performance. Keep functionality same:{code}",
            input_variables=["code"]
        )
 
        tips_template = PromptTemplate(
            template="Provide 3 key tips and best practices for improving the following code:{code}",
            input_variables=["code"]
        )
 
        merge_template = PromptTemplate(
            template=(
                "Combine the following into a single Code Review Report:\n\n"
                "Review:{review}\n"
                "Refactored Code:{refactor}\n"
                "Tips & Best Practices:{tips}\n"
                "Return a neatly formatted professional report."
            ),
            input_variables=["review", "refactor", "tips"]
        )
 
        parallel_chain = RunnableParallel({
            "review": review_template | code_review_model | parser,
            "refactor": refactor_template | code_review_model | parser,
            "tips": tips_template | suggestions_model | parser
        })
 
        merge_chain = merge_template | gemini_model | parser
        parallel_result = parallel_chain.invoke({"code": code_truncated})
        full_result = merge_chain.invoke({
            "review": parallel_result["review"],
            "refactor": parallel_result["refactor"],
            "tips": parallel_result["tips"]
        })
 

        st.subheader("AI Code Review Report📄")
        st.text_area("Full Code Review Report",value=full_result,height=500)
 
