import streamlit as st 
# streamlit: Web based appmaking 
# lite python framework

st.title("AI Resume Maker")

st.Markdown("""## User can create or 
download AI created Resume based on high ATS
score""")


#===============AGENT CODE===============

import os
import time
import langchain
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
import pytesseract as pyt
from tavily import TavilyClient
from langchain.messages import SystemMessage, HumanMessage
import numpy as np
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader


#==================API KEY LOAD========================

GOOGLE_API_KEY = st.sidebar.text_input("GOOGLE_API_KEY",type="password")
GROQ_API_KEY = st.sidebar.text_input("GROQ_API_KEY",type="password")
TAVILY_API_KEY = st.sidebar.text_input("TAVILY_API_KEY",type="password")

# =============================MODEL BUILDING=========================
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite',
    google_api_key = GOOGLE_API_KEY
)

def search_recent_news_jobs():
  """this function helps to search
  recent newws or recent jons
  related to given search query
  suppose user write Python Developer jobs
  It should return trending news and jobs link"""
  client = TavilyClient(
      api_key = TAVILY_API_KEY
  )
  return client_search(query)





# agent creation
agent = create_agent(
model = model,
tools = [search_recent_news_jobs]
)


#===============Prompt Generator============================
def prompt_generator(agent):
  """this function helps to give detailed prompt
  followed by chain of thoughts and
  persona based prompting, mai9n task is to give
  detailed prompt to bulid Resume for
  students or experienced person
  Based on their given personal information."""

  prompt = """you are a senior HR resume analyzer,
  main task is to give
  detailed prompt to build Resume for
  Students or Experienced person Based on
  their given personal information.
  System Instruction i want model to generate resume
  in HTML format, include that in prompt"""
  response = agent.invoke(prompt)
  file_name = 'prompt.py'
  
    with open(file_name, 'w') as f:
    f.write(response.content[-1]['text'])
  return "Prompt file generated Successfully, agent can read it"


prompt_generator(model)

# tool 2:
# tool 2:
def resume_maker_prompt():
 """This function just gives
 updated prompt for model"""
 with open('prompt.py', 'r') as f:
  prompt = f.read()
 return prompt
  
resume_maker_prompt()
#========================generate resume====================
prompt = """You are a helpful AI assistant
with job resume maker, your task is to give
HTML format resume, with proper designing using recent CSS and JS
code, with professional design Format.
User will upload data and return HTML format resume
always use different color or style"""

final_prompt = prompt + resume_maker_prompt()

user_details = """user details: given below:
name->shaksham negi course->BCA age->20 gender->male email->shakshamsinghnegi@gmail.com college->iitm
skills->web programming with help of ai , python , java , full stack ,
"""
query = final_prompt + user_details

if st.button("Generate Resume")
  with st.spinner("running agent....")
  
    
    response = agent.invoke({'messages':[{'role': 'user', 'content':query}]})
    code = response['messages'][-1].content[-1]['text']

    st.markdown(code)
    st.html(code, width="stretch", unsafe_allow_javascript=True)

