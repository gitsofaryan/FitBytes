import streamlit as st
import requests

# Function to call the Gemini API
def get_bot_response(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDb-a07ki8epIZbxyr05oQU-dkHt9sXIxg"  # Adjust if necessary
    headers = {
        "Authorization": "Bearer AIzaSyDb-a07ki8epIZbxyr05oQU-dkHt9sXIxg",  # Replace with your actual OAuth 2.0 access token
        "Content-Type": "application/json"
    }
    payload = {
        "text": prompt  # Adjust based on API documentation
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get('content', 'No response from bot.')  # Adjust field name based on response format
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit app layout
def main():
    st.title("Mental Bot")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for msg in st.session_state.messages:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

    # Create a container for the input and button
    with st.container():
        # Input box
        user_input = st.text_input("You:", "", key="input")

        # Button to send message
        if st.button("Send"):
            if user_input:
                # Append user message
                st.session_state.messages.append({"role": "user", "content": user_input})

                # Get response from bot
                with st.spinner("Fetching response..."):
                    bot_response = get_bot_response(user_input)

                # Append bot response
                st.session_state.messages.append({"role": "bot", "content": bot_response})

                # Clear input box
                # st.session_state.input = ""  # Use this to clear input box
                st.experimental_rerun()  # Refresh the app to reflect input box clearing

if __name__ == "__main__":
    main()
