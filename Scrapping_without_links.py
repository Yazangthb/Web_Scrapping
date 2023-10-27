import difflib
from langchain.chains import SimpleSequentialChain
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
import time
import openai
import os
import openai
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

openai.api_key =  "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"
llm_model = "gpt-3.5-turbo-0301"
llm = ChatOpenAI(temperature=0.0, model=llm_model)

first_prompt = ChatPromptTemplate.from_template(
    "Given the text which represents a scrapped website by the span components \
 identify the what is the purpose of the website\
text : {text} "
)
chain_one = LLMChain(llm=llm, prompt=first_prompt,output_key="main_purpose")

second_prompt= ChatPromptTemplate.from_template("Given the text which represents the main purpose of a website \
 identify the main users of this websites\
text : {main_purpose} ")
chain_two = LLMChain(llm=llm, prompt=second_prompt,output_key="main_users")

third_prompt= ChatPromptTemplate.from_template("Given a scrapped website with the main users of it\
provide an appropriate schema that has a number of json objects equal to the number of types of users\
and in each json object there should be keys as the important information title for the type of user\
 and values should be filled with the needed information for each key from the scrapped website data\
 The main users: {main_users} \
The scrapped website :{text}")

chain_three = LLMChain(llm=llm, prompt=third_prompt,output_key="json")
fourth_prompt= ChatPromptTemplate.from_template("""Given a scrapped website with the list of the main users of it and the list of important information for each user type\
provide an appropriate schema that has a number of json objects equal to the number of types of users\
and in each json object there should be keys and values, each key is an element of the list of important information for the user\
 and the values for those keys should be the information from the scrapped website with the actual link where the information can be found if the website has a link about such information\
 The main users: {main_users} \
The list of important information:{list} \                                                
The scrapped website :{text}""")
chain_four = LLMChain(llm=llm, prompt=fourth_prompt,output_key="json")
fourth_prompt= ChatPromptTemplate.from_template("""Given a scrapped website with the list of the main users of it and the list of important information for each user type\
provide an appropriate schema that has a number of json objects equal to the number of types of users\
and in each json object there should be keys and values, each key is an element of the list of important information for the user\
 and the values for those keys should be filled with both:1) the information from the scrapped website 2) the actual link where the information can be found if the website has a link for this information\
 The main users: {main_users} \
The list of important information:{list} \
The scrapped website :{text}""")
chain_four = LLMChain(llm=llm, prompt=fourth_prompt,output_key="json")
#


overall_chain = SequentialChain(

chains=[chain_one, chain_two, chain_three],
    input_variables=["text"],
    output_variables=["main_purpose", "main_users"
      ,"json"],
    verbose=True
)
def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    with get_openai_callback() as cb:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        print(cb)
    return response['choices'][0]['message']['content']

urls = ["https://taqaspace.com/courses/"]

def scrape_with_playwright(urls,):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()


    docs_transformed = bs_transformer.transform_documents(docs)
    print(docs_transformed)
    print(docs_transformed)
    print("Extracting content with LLM")
    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_overlap=10)
    splits = splitter.split_documents(docs_transformed)
    extracted_content = overall_chain(splits[0].page_content)
    pprint.pprint(extracted_content)
    return extracted_content
# prompt = "fill the schema inside the square brackets[] with the information from the text between brackets() ({text}). [{schema}]"
extracted_content = scrape_with_playwright(urls)
print(extracted_content)