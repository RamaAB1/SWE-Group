import pandas as pd
from groq import Groq

dataset_path = "./recipes.csv" # Change based on the directory where recipes.csv is saved
try:
    df = pd.read_csv(dataset_path)
    
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")

def ask_groq(question):
    client = Groq(api_key="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")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful cooking assistant. Only answer questions about food and recipes and its okay to reply for greetings ,If the user asks irrelevant, respond with 'This is out of my scope."           
                               }
                ,
                {
                    "role": "user",
                    "content": 
                    f"Query: {question}\nIf the user asks for a recipe, first check the first 10 elements in {df} list if you find similarity between the search and one or two of the elements then give the recipes name ingredients and time taken to cook. However, if you couldn't find a match answer from your own knowledge"
                    f"if the recipes are not relevant then use your knowledge"
                      f"List recipe name, ingredients, instructions, estimate cooking time only.",
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred while using the Groq API: {e}"

def chat(dataframe):
    print("Welcome to the Food Assistant!")
    print("Ask about recipes or general food-related questions.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        else:
            response = ask_groq(user_input)
            print(f"Bot: {response}")

if df is not None:
    chat(df)
