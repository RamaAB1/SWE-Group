from Manage import list, print_array
from Suggested_recipes import suggest

def chatbot():

    print("Welcome to the Recipe Suggestion Chatbot!")
    print("Please select an option:")
    print("1. View ingredient list")
    print("2. View expired items")
    print("3. Suggest recipes")
    print("4. Chat with the Chat bot ")
    print("5. Exit")

    ingredients_list = list.manage_ingredients()

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print(" Here are you ingredient list...")
            print_array (ingredients_list[0])
        elif choice == "2":
            print("Here are your expired items...")
            print_array (ingredients_list[1])
        elif choice == "3":
            print("Here are some recipe suggestions...")
            print (suggest())
        elif choice == "4":
            print("Chat with the Chat bot")
            from Food_recipes import df , chat
            chat(df)
        elif choice == "5":
            print ("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

chatbot()
