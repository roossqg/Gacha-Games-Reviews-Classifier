import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

from ollama import chat

from langchain.agents import create_agent,AgentState
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver,MemorySaver
from  langchain.messages import HumanMessage,AIMessage

from ai_agent.chat_langc import agent_stream

from pydantic import BaseModel
import streamlit as st

class Agent_State(AgentState):
    use_id: int

checkpointer = InMemorySaver()

model = init_chat_model(
    model = 'llama3.2:3b-instruct-q4_K_M',
    model_provider='ollama',
    temperature = 0.5,
    max_tokens = 5000
)

agent = create_agent(
    model=model,
    state_schema=AgentState,
    checkpointer=InMemorySaver()

)

config = {'thread_id': 'main_chat'}

st.title('Gacha Games Chatbot')

    

def main():
    if "messages" not in st.session_state:
        st.session_state.messages = [{'role':'system','content':'''You are a Customer Chatbot which
        provides guides,tips and reviews about the Gacha Games:Genshin Impact',
        'Honkai Star Rail','Zenless Zone Zero',
        'Wuthering Waves','Blue Archive'''}]


    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("What is up?"):
        
        st.chat_message("user").markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})

        
        with st.chat_message("assistant"):

            with st.status('Typing...'):
                res = st.write_stream(agent_stream(agent))        
                
        st.session_state.messages.append({"role": "assistant", "content": res})

if __name__ == "__main__":
    main()