
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

from ollama import chat


st.title('Gacha Games Chatbot')

def ollama_stream_chat():
    response = chat(
                    model='llama3.2:3b-instruct-q4_K_M',
                    stream = True,
                    messages=[{
                    'role': k['role'],'content': k['content']}
                    for k in st.session_state.messages])
        
    for chunk in response:
        yield chunk['message']['content']
    

def main():
    if "messages" not in st.session_state:
        st.session_state.messages = [{'role':'system','content':'''You are a Customer Chatbot which
        provides guides,tips and reviews about Gacha Games'''}]


    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("What is up?"):
        
        st.chat_message("user").markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})

        
        with st.chat_message("assistant"):

            with st.status('Typing...'):
                res = st.write_stream(ollama_stream_chat())        
                
        st.session_state.messages.append({"role": "assistant", "content": res})

if __name__ == "__main__":
    main()