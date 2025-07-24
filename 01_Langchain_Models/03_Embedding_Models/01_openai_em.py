from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Now ai agent is the cutting edge technology")

print(str(result))