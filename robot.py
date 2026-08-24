import os
from google import genai

# 1. රහස් පාස්වර්ඩ් එක පරිසර විචල්‍යයෙන් (environment variable) ලබාගන්නවා
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("රොබෝ අලුත් Gemini සුපිරි මොළයට කෝල් කරනවා... ☎️")

# 2. අලුත් ෆැක්ටරියේ ඉන්න 'gemini-3.5-flash' රොබෝව පාවිච්චි කරමු!
response = client.models.generate_content(
    model='gemini-3.5-flash', 
    contents='කෘතිම බුද්ධිය කියන්නේ මොකක්ද කියලා පොඩි ළමයෙක්ට තේරෙන්න එක වාක්‍යයකින් කියන්න.'
)

# 3. උත්තරේ බලමු
print("Gemini සුපිරි මොළයේ උත්තරේ: ")
print(response.text)