import streamlit as st

def display_intro():
    st.markdown("## **Welcome to the Job Seeker Application System!**")
    st.markdown("""
    Welcome to the **Job Seeker Application System**—your one-stop platform for submitting job applications and discovering new career opportunities. Whether you're a recent graduate or a seasoned professional, our easy-to-use form lets you share your personal and professional details with potential employers.

    ### **What You Can Do Here:**
    - **Submit Your Application**: Fill out your personal and job-related information.
    - **Get Personalized Recommendations**: Receive job suggestions powered by AI.
    - **Explore Industry Insights**: View trends and salary data to guide your career choices.
    """)

# Call the function to display the introduction
if __name__ == "__main__":
    display_intro()
