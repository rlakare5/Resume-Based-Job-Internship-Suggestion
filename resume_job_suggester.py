import streamlit as st
import PyPDF2
from openai import OpenAI


client = OpenAI(api_key="AIzaSyC0ZmcX3VZ3D0FfHy2lAoH3h6O1adFU4BA")  # Replace with your OpenAI API key


st.title("💼 Resume-Based Job & Internship Suggestion")
st.write("Upload your resume to get recommended jobs and internships.")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.subheader("📝 Resume Content Preview")
    st.write(text[:1000] + "...")  
    
    if st.button("Suggest Jobs & Internships"):
        prompt = f"""
        Analyze the following resume and suggest 5 relevant job positions or internships, 
        including a brief reason for each recommendation. 
        Resume content: {text}
        """
        # Query LLM
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        
        suggestions = response.choices[0].message.content
        
        st.subheader("💡 Suggested Jobs & Internships")
        st.write(suggestions)
