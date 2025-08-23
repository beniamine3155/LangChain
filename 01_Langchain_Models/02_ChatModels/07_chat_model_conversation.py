from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# load the openai api key from .env file
load_dotenv()

# create a default chatopenai model
model = ChatOpenAI()

chat_history = []

chat_history.append(SystemMessage(content="You are a helpful Assistant"))

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI Message: {response}")


print("------Message History------")
print(chat_history)
