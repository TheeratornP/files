import streamlit as st
import pandas as pd

# Example of data in session_state (for demonstration purposes)
# If you already have your 'submissions' in session state, you can ignore this part.
if 'submissions' not in st.session_state:
    st.session_state.submissions = pd.DataFrame(columns=[
        "Name", "Email", "Phone", "Desired Job Role", "Expected Salary", 
        "Years of Experience", "Highest Level of Education", "Skills"
    ])

# Access the data stored in session state
if not st.session_state.submissions.empty:
    # Convert the dataframe to a CSV string (without index column)
    csv = st.session_state.submissions.to_csv(index=False)
    
    # Display the download button at the top
    st.title("All Job Seeker Applications")
    st.download_button(
        label="Download .csv to your desktop",
        data=csv,
        file_name="job_applications.csv",
        mime="text/csv"
    )
    
    # Display the table below the download button
    st.dataframe(st.session_state.submissions)
    
else:
    st.title("No Applications Yet")
    st.write("There are no job seeker applications to display.")
