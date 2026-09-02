import os
from google import genai

# Fetch secret API key from environment
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Calling the new Gemini super brain... ☎️")

response = client.models.generate_content(
    model='gemini-3.5-flash', 
    contents='Explain what artificial intelligence is in one sentence so a child can understand.'
)

print("Gemini super brain's response: ")
print(response.text)