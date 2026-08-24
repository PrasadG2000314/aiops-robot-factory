import os
from google import genai

# සේප්පුවෙන් රහස් පාස්වර්ඩ් එක ගන්නවා
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("රොබෝ අලුත් Gemini සුපිරි මොළයට කෝල් කරනවා... ☎️")

response = client.models.generate_content(
    model='gemini-3.5-flash', 
    contents='කෘතිම බුද්ධිය කියන්නේ මොකක්ද කියලා පොඩි ළමයෙක්ට තේරෙන්න එක වාක්‍යයකින් කියන්න.'
)

print("Gemini සුපිරි මොළයේ උත්තරේ: ")
print(response.text)