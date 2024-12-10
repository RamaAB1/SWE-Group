import pandas as pd
from groq import Groq

zip_path = r"C:\Users\ramaa\Downloads\recipes.csv.zip" 
extract_to = "./recipes_data" 

dataset_path = "./recipes_data/recipes.csv"
try:
    df = pd.read_csv(dataset_path)
    # df['text'] = df['Name'] + " " + df['RecipeIngredientParts']

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
                    f"Query: {question}\nIf the user asks for a recipe, look at these and suggest two from the list if they are good match calling the first 10 elements in {df} list"
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

        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        else:
            response = ask_groq(user_input)
            print(f"Bot: {response}")

if df is not None:
    chat(df)
