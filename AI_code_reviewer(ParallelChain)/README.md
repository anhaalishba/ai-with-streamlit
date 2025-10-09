## 💻 AI Code Reviewer 🧠

### 🧠 Overview

**AI Code Reviewer** is a **multi-model AI-powered application** built with **LangChain** and **Streamlit**.
It automatically reviews your code, refactors it for better performance, and suggests professional coding tips — all in seconds!

This project demonstrates the use of **three different AI models from three different sources:**

* 🧩 **Gemini (Google)** → Combines and formats the final report
* 🤗 **Hugging Face (distilgpt2)** → Generates improvement tips
* 🦙 **LLaMA (via Together/OpenAI endpoint)** → Performs detailed review and refactoring

---

### 🚀 Features

✅ Uses **RunnableParallel** to run multiple models simultaneously
✅ Automatically reviews and refactors code
✅ Generates 3 professional improvement tips
✅ Combines all results into a single clean report
✅ Built with **Streamlit** for an easy-to-use interface
✅ Works with **environment variables** via `.env` file

---

### 🏗️ Tech Stack

* **Python 3.10+**
* **LangChain**
* **Streamlit**
* **Google Gemini**
* **Hugging Face Transformers**
* **LLaMA (Open Source)**
* **dotenv** (for environment setup)

---

### ⚙️ Installation Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anhaalishba/ai-with-streamlit/edit/main/AI_code_reviewer(ParallelChain)
```

#### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Add Environment Variables

Create a `.env` file in the root folder and add your keys:

```
OPENAI_API_KEY=your_openai_or_together_api_key
OPENAI_BASE_URL=your_model_endpoint_url
```

#### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

### 📁 Project Structure

```
📂 ai-code-reviewer/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
└── .env                 # API keys (excluded from git)
```

---

### 📄 Example Output

When you paste your code and click **“Review Code”**, the app will display:

* **Review Section:** Analysis of code, bugs, and suggestions
* **Refactored Code:** Clean, efficient version of your code
* **Tips & Best Practices:** 3 improvement tips from Hugging Face
* **Final Merged Report:** Neatly formatted by Gemini

---

### 🧠 Concepts Demonstrated

* Multi-model orchestration with **LangChain**
* Parallel execution using **RunnableParallel**
* Combining results with **merge chains**
* Using **PromptTemplate** for structured instructions
* Output parsing via **StrOutputParser**
* Interactive **Streamlit UI**

---

### ⚡ RunnableParallel – How It Works

`RunnableParallel` runs multiple models **at the same time**, improving speed and efficiency.
In this project, it runs:

* **Review** → via LLaMA
* **Refactor** → via LLaMA
* **Tips** → via Hugging Face

All three outputs are merged using **Gemini**.

#### 🔧 Code Example

```python
parallel_chain = RunnableParallel({
    "review": review_template | code_review_model | parser,
    "refactor": refactor_template | code_review_model | parser,
    "tips": tips_template | suggestions_model | parser
})
```

Then merged by:

```python
merge_chain = merge_template | gemini_model | parser
```

### 🧪 Sample Test Code

Try this example inside your app to test it:

```python
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    print("Average is:", average)

data = [10, 20, 30, 40, 50]
calculate_average(data)
```

✅ Expected Output:

* Review identifies unoptimized loop and missing error handling
* Refactor uses `sum(numbers)` and returns result
* Tips suggest adding docstrings and exception handling
* Gemini merges everything into one formatted report

---

### ✨ Future Enhancements

* Add syntax highlighting to reviewed code
* Support for multiple languages (Python, JavaScript, C++)
* Export review as a downloadable **PDF** report
* Add separate tabs for review, refactor, and tips sections

---

### 👩‍💻 Author

**Developed by:**Anha Alishba
