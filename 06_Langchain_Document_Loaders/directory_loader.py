from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path="/Users/beniaminenahid/Documents/Github Repo/LangChain/06_Langchain_Document_Loaders/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
