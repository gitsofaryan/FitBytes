import streamlit as st
import subprocess
import os

# A variable to keep track of the currently running process
current_process = None

# Function to run the selected app
def run_app(command):
    global current_process

    # If there's a running process, terminate it
    if current_process:
        current_process.terminate()

    # Start the new process
    current_process = subprocess.Popen(command, shell=True)

# Streamlit UI
st.title("Health and Fitness App")

# Sidebar for navigation
tab = st.sidebar.selectbox("Select a Tab", ["Yoga", "Gym", "Mental Bot", "Assistant and Diet Support"])

if tab == "Yoga":
    st.write("Yoga Tab Selected")
    run_app("streamlit run .\yoga\yoga.py")
elif tab == "Gym":
    st.write("Gym Tab Selected")
    run_app("python .\Gym\main.py")
elif tab == "Mental Bot":
    st.write("Mental Bot Tab Selected")
    run_app("python mental_bot_app.py")
elif tab == "Assistant and Diet Support":
    st.write("Assistant and Diet Support Tab Selected")
    run_app("python assistant_diet_app.py")

# A Streamlit command to terminate the process when the app is closed
if st.button("Stop All"):
    if current_process:
        current_process.terminate()
        current_process = None
        st.write("All processes stopped.")
