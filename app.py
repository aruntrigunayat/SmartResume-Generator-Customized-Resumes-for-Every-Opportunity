import streamlit as st
import google.generativeai as genai
import json


# Configure Google Gemini API
API_KEY = "AIzaSyD4PDnHaB3fqfIMovfiDAlOKuV2SjHfX0s"
genai.configure(api_key=API_KEY)



# Streamlit UI
st.set_page_config(page_title="SmartResume Generator", layout="centered")
st.title("📄 SmartResume Generator")
st.write("Customized Resumes for Every Opportunity")

# User Input
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
skills = st.text_area("Skills (comma-separated)")
education = st.text_area("Education Details")
experience = st.text_area("Work Experience")
custom_info = st.text_area("Additional Information (Projects, Certifications, etc.)")

# Resume Style Selection
template = st.selectbox("Choose Resume Template", ["Classic", "Modern", "Minimal"])

if st.button("Generate Resume"):
    if name and email and skills:
        with st.spinner("Generating Resume with AI..."):
            # Prepare input for AI
            prompt = f"Generate a professional resume for {name} with these details:\n\n"
            prompt += f"Email: {email}\nPhone: {phone}\n\n"
            prompt += f"Skills: {skills}\nEducation: {education}\nExperience: {experience}\n\n"
            prompt += f"Additional Info: {custom_info}\nTemplate: {template}"
            
            # Call Gemini API
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            
            # Display generated resume
            st.subheader("Generated Resume")
            st.write(response.text)
    else:
        st.warning("Please fill in at least your name, email, and skills.")




# Run: streamlit run filename.py
