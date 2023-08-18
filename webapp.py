import streamlit as st
import pandas as pd
import numpy as np
def main():
    # Add some space above the title to move it up
    # st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Use CSS to style the container
    st.markdown(
        """
        <style>
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 70vh;
            position: relative;
        }
        
        .content {
            width: 50%;
            padding: 20px;
            border-right: 1px solid #ccc;
            z-index: 1;
            background-color: white;
        }
        
        .df-messenger {
            width: 50%;
            position: absolute;
            right: 0;
            top: 0;
            z-index: 2;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title('Osteoporosis Care Assistant')

    html_code = """
    <div class="container">
        <div class="content">
            <!-- Your content goes here -->
            <p style="font-size: 24px;">Hello! Here is your Osteoporosis Care Assistant!</p>
            <br>
            <p style="font-size: 20px;">I am a chatbot that can help you with osteoporosis.</p>
            <br>
            <p style="font-size: 20px;">Click below to start chatting with me!</p>
        </div>
        <div class="df-messenger">
            <script src="https://www.gstatic.com/dialogflow-console/fast/messenger-cx/bootstrap.js?v=1"></script>
            <df-messenger
                df-cx="true"
                location="us-central1"
                chat-title="Osteoporosis Care Assistant"
                agent-id="89b18026-b1f1-4e60-bb15-607bfd386d97"
                language-code="en"
            ></df-messenger>
        </div>
    </div>
    """
    st.components.v1.html(html_code, height=650, scrolling=False)
    
    st.write("Please provide your satisfaction rating from 1 to 5:")

    # Create a slider for user to input satisfaction rating
    satisfaction_rating = st.slider("Satisfaction Rating", min_value=1, max_value=5, step=1)

    # Create a button to submit the survey
    if st.button("Submit"):
        # Write the satisfaction rating to a file
        with open("user_research.txt", "a") as f:
            f.write(str(satisfaction_rating) + "\n")
        st.success("Thank you for participating in the survey!")



if __name__ == "__main__":
    main()
