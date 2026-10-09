from langchain.agents import create_agent,AgentState
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver,MemorySaver
from  langchain.messages import HumanMessage,AIMessage

from pydantic import BaseModel
import streamlit as st

class Agent_State(AgentState):
    use_id: int

checkpointer = InMemorySaver()

model = init_chat_model(
    model = '',
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

#stream:

def agent_stream(agent):
    stream = agent.stream_events({'messages':[{
            'role': k['role'],'content': k['content']}
            for k in st.session_state.messages]}
            ,version='v3',config=config)

    for event in stream.messages:
        for delta in event.text:
            yield delta 


if "messages" not in st.session_state:
    st.session_state.messages = []


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



    