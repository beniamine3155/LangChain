from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI


load_dotenv()


model = ChatOpenAI()


# Setup Firebase Firestore
PROJECT_ID = "langchain-4b4a4"
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
COLLECTION_NAME = "chat_history"


# Initialize firestore client
client = firestore.Client(project=PROJECT_ID)


# Initialize firestore Chat Message History
chat_history = FirestoreChatMessageHistory(
    session_id = SESSION_ID,
    collection = COLLECTION_NAME,
    client=client
)


model = ChatOpenAI()

while True:
    human_msg = input("You: ")
    if human_msg.lower() == "exit":
        break
    chat_history.add_user_message(human_msg)
    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")





