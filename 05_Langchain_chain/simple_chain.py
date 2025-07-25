from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template = PromptTemplate(
    template="Generate a summary based on the {topic} within 5 lines ",
    input_variables=['topic']
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_retries=2)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'topic':'MCP'})

print(result)

chain.get_graph().print_ascii()

