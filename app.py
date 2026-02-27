import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI Configuration
st.set_page_config(page_title="AI Resume Builder", page_icon="📄")
st.title("📄 AI Resume & Portfolio Builder")
st.markdown("Generate a highly technical, professional resume using Generative AI.")

# User Inputs
with st.form("resume_form"):
    name = st.text_input("Full Name", placeholder="e.g., John Doe")
    education = st.text_input("Education", placeholder="e.g., B.Tech Computer Science, 6th Semester")
    skills = st.text_area("Technical Skills", placeholder="e.g., Python, Machine Learning, Scikit-Learn, Pandas")
    projects = st.text_area("Projects", placeholder="e.g., Facial Recognition System using OpenCV...")
    experience = st.text_area("Experience/Internships", placeholder="e.g., AIML Intern - Focused on data processing...")
    
    submitted = st.form_submit_button("Generate AI Resume")

# AI Generation Logic
if submitted:
    if not name or not skills:
        st.warning("Please fill in at least your name and skills!")
    else:
        with st.spinner("Processing data and generating resume..."):
            prompt = f"""
            You are an expert technical resume writer. Take the following student data and generate a professional, tailored resume in Markdown format. 
            Make the project descriptions sound highly technical, action-oriented, and impactful.

            Name: {name}
            Education: {education}
            Skills: {skills}
            Projects: {projects}
            Experience: {experience}

            Format the output cleanly with standard resume headings.
            """
            
            try:
                # Call the Gemini API via Python
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("Resume Generated Successfully!")
                
                # Display the output
                st.markdown("### Your Generated Resume")
                st.markdown(response.text)
                
                # Add a download button for the generated text
                st.download_button(
                    label="Download Resume as Text",
                    data=response.text,
                    file_name=f"{name.replace(' ', '_')}_Resume.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")