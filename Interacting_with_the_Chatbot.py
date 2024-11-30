
# example ingredients and recipes
ingredients = [
    {"name": "Milk", "expiry_date": "2024-12-01"},
    {"name": "Eggs", "expiry_date": "2024-12-03"},
    {"name": "Cheese", "expiry_date": "2024-12-05"},
]

recipes = {
    "Omelette": ["Eggs", "Milk", "Cheese"],
    "Pancakes": ["Eggs", "Milk"],
    "Cheese Toast": ["Cheese", "Bread"],
}


# Chatbot interaction
def chatbot_interaction(user_input):
    user_input = user_input.lower()

    if "ingredients" in user_input:
        if not ingredients:
            return "You have no ingredients stored."
        return "Here are your ingredients:\n" + "\n".join(
            [f"{item['name']} (Expires on: {item['expiry_date']})" for item in ingredients])

    if "do i have" in user_input: #change
        ingredient_name = user_input.replace("do i have", "").strip().capitalize()
        for item in ingredients:
            if item["name"].lower() == ingredient_name.lower():
                return f"Yes, you have {ingredient_name} (Expires on: {item['expiry_date']})."
        return f"No, you don't have {ingredient_name}."

    if "recipe" in user_input:
        available_ingredients = [item["name"] for item in ingredients]
        suggested_recipes = [
            recipe for recipe, req_ingredients in recipes.items()
            if all(ingredient in available_ingredients for ingredient in req_ingredients)
        ]
        if not suggested_recipes:
            return "Sorry, no recipes can be made with your current ingredients."
        return "Here are some recipes you can make:\n" + "\n".join(suggested_recipes)

    return "I'm sorry, I don't understand that. You can ask about ingredients, recipes, or check if you have a specific ingredient."


# Example
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot_interaction(user_input)
        print(f"Chatbot: {response}")

