from openai import AzureOpenAI
import os
from dotenv_vault import load_dotenv

load_dotenv()

api_version = "2024-12-01-preview"
client = AzureOpenAI(
  api_version=api_version,
  api_key = os.getenv("AZURE_OPENAI_KEY"),  
  base_url= os.getenv("EMBEDDINGS_ENDPOINT")
)

model_name = "text-embedding-ada-002"

def generate_embeddings(text, model):
    return client.embeddings.create(input = [text], model=model).data[0].embedding

print(generate_embeddings("Ancona", model_name))