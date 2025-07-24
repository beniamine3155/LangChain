from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = llm.invoke("What is the difference between chatModel and llm??")

print(result)