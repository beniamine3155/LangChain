from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_retries=2)

template1 = PromptTemplate(
    template="Generate a detailed report based on the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Education System of Bangladesh'})

print(result)

chain.get_graph().print_ascii()
