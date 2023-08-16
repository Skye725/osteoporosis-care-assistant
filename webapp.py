import streamlit as st
import pandas as pd
import numpy as np
def main():
    st.title('Osteoporosis Care Assistant')
    # Embed Dialogflow Messenger using HTML
#     st.title("Hello! Here is your Osteoporosis Care Assistant!")
#     st.write("I am a chatbot that can help you understand and care for osteoporosis. ")
#     st.write("Click below to start chatting with me!")
    
#     html_code ="""
#     <script src="https://www.gstatic.com/dialogflow-console/fast/messenger-cx/bootstrap.js?v=1"></script>
#     <df-messenger
#       df-cx="true"
#       location="us-central1"
#       chat-title="Osteoporosis Care Assistant"
#       agent-id="89b18026-b1f1-4e60-bb15-607bfd386d97"
#       language-code="en"
#     ></df-messenger>
#     """        
#     st.components.v1.html(html_code, height=300, scrolling=True)
    
    
    html_code ="""
   <div style="display: flex; justify-content: center; align-items: center; height: 70vh; "> <!-- Adjust the height here -->
        <div style="width: 50%; padding: 20px; border-right: 1px solid #ccc;">
            <!-- Your content goes here -->
            <p style="font-size: 20px;">Hello! Here is your Osteoporosis Care Assistant!</p>
            <p style="font-size: 20px;">I am a chatbot that can help you understand and care for osteoporosis.</p>
            <p style="font-size: 20px;">Click below to start chatting with me!</p>
        </div>
        <div style="width: 50% ;">
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
    st.components.v1.html(html_code, height=700, scrolling=False)
    
    
    
if __name__ == "__main__":
    main()

