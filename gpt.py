from openai import OpenAI
client = OpenAI()

completion = client.embeddings.create(
  input=[
    "Hello Diego"
  ],
  model="text-embedding-ada-002"
)

print(completion.data[0].embedding)