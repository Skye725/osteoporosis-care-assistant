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
    
    st.write("After using, we sincerely invite you to participate in our user survey！")
   
    # survey_questions = [
    #         "The assessment result is accurate",
    #         "The AI expert can provide accurate answers",
    #         "The system is useful",
    #         "The system is easy to use",
    #         "The system is flexible"
    #     ]

    # # Loop through each survey question
    # for question in survey_questions:
    #     # st.write(f"Please provide your satisfaction rating for the following question: {question}")

    #     # Create a slider for user to input satisfaction rating
    #     satisfaction_rating = st.slider(f"{question} (1-5)", min_value=1, max_value=5, step=1)
    st.components.v1.html(
        """
        <div data-tf-widget="FmSIrjqJ" data-tf-opacity="100"
             data-tf-iframe-props="title=User Research Form for Osteoporosis Chatbot App"
             data-tf-transitive-search-params data-tf-medium="snippet"
             style="width:100%;height:500px;">
        </div>
        <script src="//embed.typeform.com/next/embed.js"></script>
        """,
        height=550
    )



if __name__ == "__main__":
    main()
