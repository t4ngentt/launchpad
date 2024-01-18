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

    directory_path = './static/txt/'
    file_path = os.path.join(directory_path, position + '.txt')

    if (position + '.txt') not in os.listdir(directory_path):
        with open(file_path, 'w') as file:
            pass
        file.close()
    
    else:
        return restart_conversation(position, human_input)

    sllm = OpenAI(temperature=0.5)
    
    main_prompt = PromptTemplate(
    input_variables=['position', 'human_input', 'chat_history'],
    template="""You are a {position}. You need to personify {position}. If required , use appropriate language according to the personality. You are chatting with another user.
    
    Chat History:   

    {chat_history}
    User: {human_input}
    You (AI): 
    """
    )

    chain = LLMChain(llm=sllm,prompt = main_prompt, verbose=True, memory=memory)
    temp = chain.predict(position=position, human_input=human_input)
    print(temp)    

    file1 = open("./static/txt/"+position+".txt", "a") 
    file1.write('You: ' + human_input + "\n" + position + ": " + temp + "\n----------------------------- \n")
    file1.close()
    return temp


def restart_conversation(position, human_input):
    file1 = open("./static/txt/"+position+".txt", "r") 
    history = file1.read()
    file1.close()
    sllm = OpenAI(temperature=0.5)
    template =history+ """ 
    
    The user now wants to resume to chat with you. You are a {position}. You need to personify {position}. If required , use appropriate language according to the personality.
    
    Chat History:   

    {chat_history}
    User: {human_input}
    You (AI): 
    """
    main_prompt = PromptTemplate(
    input_variables=['position', 'human_input', 'chat_history'], template=template
    )

    chain = LLMChain(llm=sllm,prompt = main_prompt, verbose=True, memory=memory)
    temp = chain.predict(position=position, human_input=human_input)
    print(temp)    

    file1 = open("./static/txt/"+position+".txt", "a") 
    file1.write('You: ' + human_input + "\n" + position + ": " + temp + "\n----------------------------- \n")
    return temp