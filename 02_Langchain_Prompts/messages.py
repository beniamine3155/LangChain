from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_retries=2)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Model Context Protocol")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)