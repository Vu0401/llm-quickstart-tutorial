from google import genai

client = genai.Client(api_key="")

result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents="What is the meaning of life?")

print(len(result.embeddings[0].values))