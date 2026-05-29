from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY", "key-not-found"),
    base_url="https://api.groq.com/openai/v1"
)


response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
print(response.choices[0].message.content)
