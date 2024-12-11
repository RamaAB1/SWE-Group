import os

from groq import Groq

ingredients = ["rice","chicken","tomato"]

def suggest():
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"go to {ingredients} and find one suitable recipes, give me the time taken, ingredients",
        }
    ],
    model="llama3-8b-81 92",
)
return chat_completion.choices[0].message.content

