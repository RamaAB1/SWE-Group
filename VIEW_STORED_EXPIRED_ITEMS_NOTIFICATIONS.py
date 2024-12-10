from datetime import datetime, timedelta

# Example ingredient
ingredient_names = [
    {"name": "Milk", "expiry_date": "2024-12-01"},
    {"name": "Eggs", "expiry_date": "2024-12-03"},
    {"name": "Cheese", "expiry_date": "2024-12-05"},
    {"name": "Tomato", "expiry_date": "2024-12-07"},
    {"name": "Lettuce", "expiry_date": "2024-12-02"},
    {"name": "Chicken", "expiry_date": "2024-12-08"},
    {"name": "Fish", "expiry_date": "2024-12-06"},
    {"name": "Yogurt", "expiry_date": "2024-12-04"},
    {"name": "Bread", "expiry_date": "2024-12-09"},
    {"name": "Butter", "expiry_date": "2024-12-10"},
]


ingredients = []
expired_items = []
notifications = []


def generate_ingredients(num_ingredients):
    ingredients = []
    for i in range(num_ingredients):
        ingredient = ingredient_names[i % len(ingredient_names)]
        ingredients.append(ingredient)
    return ingredients

#Change
def update_expired_items():
    today = datetime.now().date()
    global ingredients, expired_items
    expired_items = [
        item for item in ingredients if datetime.strptime(item["expiry_date"], "%Y-%m-%d").date() < today
    ]
    ingredients = [
        item for item in ingredients if item not in expired_items
    ]


def generate_notifications():
    today = datetime.now().date()
    global notifications
    notifications = [
        f"Reminder: {item['name']} will expire on {item['expiry_date']}!"
        for item in ingredients
        if (datetime.strptime(item["expiry_date"], "%Y-%m-%d").date() - today).days <= 3 #Ask group about the day of the notification
    ]


def view_stored_items():
    if not ingredients:
        return "No items are currently stored."
    return "\n".join([f"{item['name']} (Expires on: {item['expiry_date']})" for item in ingredients])


def view_expired_items():
    if not expired_items:
        return "No expired items."
    return "\n".join([f"{item['name']} (Expired on: {item['expiry_date']})" for item in expired_items])


def view_notifications():
    if not notifications:
        return "No notifications."
    return "\n".join(notifications)


if __name__ == "__main__":
    print("Generating 5 ingredients...")
    ingredients = generate_ingredients(5)

    print("\nStored Items:")
    print(view_stored_items())

    print("\nUpdating expired items...")
    update_expired_items()

    print("\nStored Items After Update:")
    print(view_stored_items())

    print("\nExpired Items:")
    print(view_expired_items())

    print("\nGenerating notifications...")
    generate_notifications()

    print("\nNotifications:")
    print(view_notifications())
