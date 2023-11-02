import difflib

from bs4 import BeautifulSoup
import requests
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



urls = ["https://taqaspace.com/courses/"]

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
print(splits[0].page_content)
import re


# Define a regular expression pattern to match URLs
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
text = splits[0].page_content
# Use the findall method to extract all URLs from the input string
links = re.findall(url_pattern, splits[0].page_content)
def get_website_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        txt = soup.get_text()
        cleaned_text = '\n'.join([line for line in txt.splitlines() if line.strip()])
        return cleaned_text
    except:
        return url + "(unable to scrape)"
# Print the extracted links
print(text)
for link in links:
    print(link)
    data = get_website_title(link)
    print(data)
    text = text.replace(link, data)

# print(text)