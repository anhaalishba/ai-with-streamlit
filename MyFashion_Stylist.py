from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

st.title("AI Fashion Stylist 👗✨")

gender = st.selectbox("Select your Gender", ["Male", "Female", "Other"])
age = st.number_input("Enter your Age", min_value=10, max_value=100)
occasion = st.selectbox("Select Occasion", ["Casual", "Party", "Office", "Wedding", "Sports"])
style = st.multiselect(
    "Select preferred styles",
    ["Trendy", "Formal", "Casual", "Vintage", "Elegant", "Sporty", "Bohemian"]
)
budget = st.selectbox("Select your Budget Range", ["Low", "Medium", "High", "Luxury"])
season = st.selectbox("Select the Current Season", ["Summer", "Winter", "Spring", "Autumn"])
colors = st.text_input("Enter your Favorite Colors ")


 #prompt
prompt = f"""
You are a professional fashion stylist.
USER PROFILE:
- Gender: {gender}
- Age: {age}
- Occasion: {occasion}
- Style preferences: {', '.join(style) }
- Budget: {budget}
- Season: {season}
- Favorite Colors: {colors}
 TASK:
Based on this profile, suggest:
1. Outfit ideas (top, bottom, shoes, etc.)
2. Color combinations
3. Accessories
4. Budget-friendly tips (according to selected budget)
5. Seasonal recommendations (fabrics or layers)
        
RULES:
- Keep suggestions practical and creative.
- Don’t suggest unrealistic fashion items.
- Make the explanation clear and easy to follow.
"""

if st.button("Generate Outfit"):
    with st.spinner("Creating your outfit ideas.."):
        result = model.invoke(prompt)
        st.subheader("Your  Fashion Suggestions 🎨")
        st.text_area("Outfit Ideas", value=result.content, height=500)
