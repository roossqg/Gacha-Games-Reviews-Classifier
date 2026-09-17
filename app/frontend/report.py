import streamlit as st
from ollama import chat

from Models import rag_report
from llm_report_chat import report_generate