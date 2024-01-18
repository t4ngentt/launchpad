from getpass import getpass
import os
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
import json

import yaml

print(os.getcwd())
with open('./config.yaml', 'r') as file:
    keydic = yaml.safe_load(file)

OPENAI_API_KEY = getpass()
os.environ["OPENAI_API_KEY"] = keydic['API_KEY']

memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")

def initaite_query(position, human_input):

    sllm = OpenAI(temperature=0.5)
    
    main_prompt = PromptTemplate(
    input_variables=['position', 'human_input', 'chat_history'],
    template="""You are a seasoned {position}. You are chatting with a user.
    
    Chat History:   

    {chat_history}
    User: {human_input}
    You (AI): 
    """
    )

    chain = LLMChain(llm=sllm,prompt = main_prompt, verbose=True, memory=memory)
    temp = chain.predict(position=position, human_input=human_input)
    print(temp)    

    file1 = open("./static/history.txt", "a") 
    file1.write('You: ' + human_input + "\nAI: " + temp + "\n----------------------------- \n")
    return temp