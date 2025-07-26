from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader("/Users/beniaminenahid/Documents/Github Repo/LangChain/06_Langchain_Document_Loaders/LLM.pdf")


docs = loader.load()

print(len(docs))

print(docs[24].page_content)
print(docs[1].metadata)