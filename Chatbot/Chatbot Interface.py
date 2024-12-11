from Manage import manage_ingredients, print_array
from Base_code import list 
from Suggested_recipe import suggest
from Food_recipes import df 

def chatbot():
    print("Welcome to the Recipe Suggestion Chatbot!")
    print("Please select an option:")
    print("1. View ingredient list")
    print("2. View expired items")
    print("3. Suggest recipes")
    print("4. Chat with the Chat bot ")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print(" Here are you ingredient list...")
            print_array (list.manage_ingredients[0])
        elif choice == "2":
            print("Here are your expired items...")
            print_array (list.manage_ingredients[1])
        elif choice == "3":
            print("Here are some recipe suggestions...")
            print (suggest)
        elif choice == "4":
            print("Chat with the Chat bot")
            chat(df)
        elif choice == "5":
            print ("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

chatbot()
