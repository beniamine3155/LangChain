from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0, max_retries=2)

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)