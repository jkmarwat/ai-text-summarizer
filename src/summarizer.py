from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

text = input("Paste text to summarize:\n")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": f"Summarize this:\n{text}"}]
)

print("\nSummary:\n")
print(response.choices[0].message.content)