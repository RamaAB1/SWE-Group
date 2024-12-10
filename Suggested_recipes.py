import os

from groq import Groq

ingredients = ["rice","chicken","tomato"]

client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"go to {ingredients} and find one suitable recipes, give me the time taken, ingredients",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
