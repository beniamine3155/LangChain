from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
   ('system', 'You are a helpful {domain} expert'),
   ('human', 'Explain the simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'doctor', 'topic':'Cancer'})

print(prompt)