def chatbot():
    print("Welcome to the Recipe Suggestion Chatbot!")
    print("Please select an option:")
    print("1. view ingredient list")
    print("2. View expired items")
    print("3. Suggest recipes")
    print("4. Chat with the Chat bot ")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print(" Here are you ingredient list...")
           # Call the function to display the ingredient list
        elif choice == "2":
            print("Here are your expired items...")
            # Call the function to suggest recipes
        elif choice == "3":
            print("Here are some recipe suggestions...")
            # Call the function to display the expired items
        elif choice == "4":
            print("Chat with the Chat bot")
            # Call the function to run the chatbot
        elif choice == "5":
            print ("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the chatbot
chatbot()

