# I need these three tools before anything else
from dotenv import load_dotenv   # to read .env file
import os                        # to read environment variables
from openai import OpenAI        # to create the API client



# Step 1: load the .env file into the OS environment
# must happen before anything tries to read the key
load_dotenv()



# Step 2: build the client object — pre-configured with
# my key and Groq's server address
# "key-not-found" default helps me debug if .env isn't loaded
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY", "key-not-found"),
    base_url="https://api.groq.com/openai/v1"
)



# Step 3: send the actual request
# specify which model and what the conversation is
# store the structured response object in `response`
#create function sends the HTTP POST request to Groq's server 
#and waits for the response.
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)




# Step 4: navigate the response object to extract
# just the text of the reply and print it
print(response.choices[0].message.content)