# 1st version
# # import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # Load environment variables from .env
# load_dotenv()

# # Initialize OpenAI client – this will use the key from OPENAI_API_KEY env
# client = OpenAI()

# def ask_llm(docs, question):
#     context = "\n".join(docs)
#     prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.3
#     )
#     return completion.choices[0].message.content


import requests
import os

# Set your OpenRouter API key here
OPENROUTER_API_KEY = "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"

def ask_llm(docs, question):
    context = "\n".join(docs)
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:8501",  # Required
        "X-Title": "DocuChat Pro"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # You can change model here
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"
