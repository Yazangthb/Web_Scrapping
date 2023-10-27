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

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
llm_model = "text-davinci-002"


def get_completion(prompt, model=llm_model):
    # messages = [{"role": "user", "content": prompt}]
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine for your needs
        prompt="What is 1+1?",
        max_tokens=100  # Adjust this as needed

    )
    return response.choices[0].text
print(get_completion("What is 1+1?"))
#
llm = ChatOpenAI(temperature=0, model="text-davinci-002")
def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm).run(content)
#

schema = {
    "properties": {
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
    },
    "required": ["news_article_title", "news_article_summary"],
}


# Load HTML
urls = ["https://eduwiki.innopolis.university/index.php/BSc:_Introduction_To_Machine_Learning"]

def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(docs, tags_to_extract=["span"])
    print("Extracting content with LLM")
    print(docs_transformed[0])
    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=10,
                                                                    chunk_overlap=0)
    splits = splitter.split_documents(docs_transformed)
    print(splits[0].page_content)
    print("stop if you want")
    time.sleep(3)
    # Process the first split
    extracted_content = extract(
        schema=schema, content=splits[0].page_content
    )
    pprint.pprint(extracted_content)
    return extracted_content


extracted_content = scrape_with_playwright(urls, schema=schema)