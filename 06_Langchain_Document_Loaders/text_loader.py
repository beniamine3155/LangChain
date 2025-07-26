from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_retries=2)

template = PromptTemplate(
    template="write a summary of the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('fruit.txt', encoding='utf-8')

docs = loader.load()

chain = template | model | parser

result = chain.invoke({'poem':docs[0].page_content})
print(result)

