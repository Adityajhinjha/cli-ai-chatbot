import os
from openai import OpenAI
from dotenv import load_dotenv
import json 

load_dotenv()  # Load environment variables from .env file


MEMORY_FILE = "memory.json"
# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Load previous memory if it exists
try:
    with open(MEMORY_FILE, "r") as file:
        conversation = json.load(file)

except FileNotFoundError:

    #Conversation Memory
    conversation = [
        {
            "role":"system",
            "content":"You are a helpful assistant."
        }
    ]

print("Chat Started...")
print("Type 'exit' to end the conversation. \n")

#Chat loop

while True:
    #Take user input
    user_input = input("You: ")

    #Exit condition
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    #Add message to memory
    conversation.append({
        "role":"user",
        "content": user_input
    })

    # Send request
    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=conversation,
        temperature=0.7,
        max_tokens=100
    )

    # Extract and print assistant reply
    reply = response.choices[0].message.content

    print("Assistant:", reply)

    conversation.append({
        "role":"assistant",
        "content": reply
    })

    # Save memory
    with open(MEMORY_FILE, "w") as file:
        json.dump(conversation, file, indent = 4)