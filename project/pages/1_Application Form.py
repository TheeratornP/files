import streamlit as st
import pandas as pd
import re

# Define the file path for storing the CSV file
CSV_FILE = "job_applications.csv"

# Initialize session state
def initialize_state():
    if 'submissions' not in st.session_state:
        try:
            st.session_state.submissions = pd.read_csv(CSV_FILE)
        except FileNotFoundError:
            st.session_state.submissions = pd.DataFrame(columns=[
                "Languages", "Gender", "First Name", "Last Name", "Birth Date", "Email", "Phone", 
                "Desired Job Role", "Work Environment", "Job Type", "Preferred Location", "Near BTS/MRT Line", 
                "Expected Salary (Min)", "Expected Salary (Max)", "Years of Experience", 
                "Highest Level of Education", "Skills"
            ])

# Validate email format
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Display job seeker form
def display_form():
    st.markdown("## 🎯 **Job Seeker Application Form**")
    st.markdown("Please fill out the form below to apply for your desired job role. Fields marked with * are required.")

    with st.form("job_seeker_form"):
        # Personal details
        st.markdown("### 👤 **Personal Details**")
        gender = st.radio("Gender*", ["Male", "Female", "Other"], key="gender")
        
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name*", key="first_name")
        with col2:
            last_name = st.text_input("Last Name*", key="last_name")
        
        birth_date = st.date_input("Birth Date*", key="birth_date", help="Select your date of birth")
        
        # Email and Phone on the same line
        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input("Email Address*", key="email", help="e.g., example@domain.com")
        with col2:
            phone = st.text_input("Phone Number*", key="phone", help="Enter a valid phone number")
        
        # Languages (checkbox list, moved after phone number)
        st.markdown("### 🌍 **Preferred Languages**")
        languages = st.multiselect(
            "Select languages you speak*", 
            ["Thai", "English", "Japanese", "Chinese", "Other"],
            default=["Thai"],  # Default to Thai
            key="languages"
        )
        
        # Job-related details
        st.divider()
        st.markdown("### 💼 **Job Preferences**")
        
        # Desired Job Role on the first column
        job_roles = [
            "",  # Blank option
            "Software Development", "Data Science", "Product Management", "Design", 
            "Marketing", "Sales", "Human Resources", "Customer Support", 
            "Finance", "Project Management", "Content Creation", "UI/UX Design", 
            "Business Analysis", "Engineering", "Cybersecurity", "Operations", 
            "Production", "Other"
        ]
        job_role = st.selectbox("Desired Job Role*", job_roles, key="job_role")
        
        # Work Environment and Job Type on the same line
        col1, col2 = st.columns(2)
        with col1:
            work_environment = st.selectbox("Work Environment*", ["", "Full Remote", "Hybrid", "On-site", "Other"], key="work_environment")
        with col2:
            job_type = st.selectbox("Job Type*", ["", "Full-time", "Contract"], key="job_type")
        
        # Salary and Experience on the same line
        st.write("Expected Salary (THB)")
        col1, col2 = st.columns(2)
        with col1:
            expected_salary_min = st.number_input("Minimum*", min_value=0, step=1000, key="min_salary")
        with col2:
            expected_salary_max = st.number_input("Maximum*", min_value=0, step=1000, key="max_salary")
        
        # Years of Experience and Highest Level of Education on the same line
        col1, col2 = st.columns(2)
        with col1:
            years_of_experience = st.number_input("Years of Experience*", min_value=0, max_value=50, step=1, key="experience")
        with col2:
            education = st.selectbox("Highest Level of Education*", ["", "High School", "Associate Degree", "Bachelor's Degree", "Master's Degree", "PhD"], key="education")
        
        # Preferred Location dropdown
        st.divider()
        st.markdown("### 🌍 **Preferred Location**")
        locations = [
            "",  # Blank option
            "Bangkok", "Chiang Mai", "Khon Kaen", "Phuket", "Chiang Rai", 
            "Chonburi", "Saraburi", "Samutprakan", "Other"
        ]
        preferred_location = st.selectbox("Preferred Location*", locations, key="preferred_location")
        
        # Checkbox for Near BTS/MRT Line
        near_bts_mrt = st.checkbox("Near BTS/MRT Line", key="near_bts_mrt")
        
        # Additional details
        st.divider()
        st.markdown("### 🛠️ **Additional Details**")
        skills = st.text_area("Skills", help="e.g., Python, JavaScript, SQL", key="skills")
        
        submit_button = st.form_submit_button("Submit Application")
        
        if submit_button:
            if not validate_email(email):
                st.error("Invalid email address. Please enter a valid email.")
            elif expected_salary_max < expected_salary_min:
                st.error("Maximum salary must be greater than or equal to minimum salary.")
            else:
                save_submission(languages, gender, first_name, last_name, birth_date, email, phone, job_role, 
                                work_environment, job_type, preferred_location, near_bts_mrt, expected_salary_min, 
                                expected_salary_max, years_of_experience, education, skills)
                st.success("Application Submitted Successfully!")

# Save submission to session state and file
def save_submission(languages, gender, first_name, last_name, birth_date, email, phone, job_role, work_environment, 
                    job_type, preferred_location, near_bts_mrt, min_salary, max_salary, experience, education, skills):
    new_data = {
        "Languages": ", ".join(languages),  # Save the selected languages as a comma-separated string
        "Gender": gender,
        "First Name": first_name,
        "Last Name": last_name,
        "Birth Date": birth_date,
        "Email": email,
        "Phone": phone,
        "Desired Job Role": job_role,
        "Work Environment": work_environment, 
        "Job Type": job_type,  # Added job type (Full-time or Contract)
        "Preferred Location": preferred_location,  # Added preferred location
        "Near BTS/MRT Line": near_bts_mrt,  # Added checkbox result
        "Expected Salary (Min)": min_salary,
        "Expected Salary (Max)": max_salary,
        "Years of Experience": experience,
        "Highest Level of Education": education,
        "Skills": skills
    }
    new_df = pd.DataFrame([new_data])
    st.session_state.submissions = pd.concat([st.session_state.submissions, new_df], ignore_index=True)
    st.session_state.submissions.to_csv(CSV_FILE, index=False)

# Main function
def main():
    initialize_state()
    display_form()

if __name__ == "__main__":
    main()
