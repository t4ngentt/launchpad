from getpass import getpass
import os
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

import yaml

print(os.getcwd())
with open('./config.yaml', 'r') as file:
    keydic = yaml.safe_load(file)

OPENAI_API_KEY = getpass()
os.environ["OPENAI_API_KEY"] = keydic['API_KEY']

def initaite_query(position, query):
    sllm = OpenAI(temperature=0.5)
    
    main_prompt = PromptTemplate(
    input_variables=['position','query'],
    template="Answer the following question as a seasoned {position}. Answer in human language.: {query}"
    )

    chain = LLMChain(llm=sllm,prompt = main_prompt, verbose=True)
    temp = chain.predict(position=position, query=query)
    print(temp)
    return (temp)