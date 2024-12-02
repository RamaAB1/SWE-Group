import tkinter as tk

WINDOW_TITLE = "Recipe"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300


class Recipe:
    def __init__(self):
        self.recipes = [
            {
                "title": "Omelet",
                "ingredients": [
                    "2 large eggs",
                    "1 tablespoon milk",
                    "Salt to taste",
                    "Black pepper to taste",
                    "1 teaspoon butter or oil",
                ],
                "instructions": """1. Crack the eggs into a bowl and whisk with milk, salt, and pepper.
2. Heat butter or oil in a non-stick pan over medium heat.
3. Pour the egg mixture into the pan and let it cook undisturbed for 1-2 minutes.
4. Fold the omelet in half and cook for another 1-2 minutes until fully set.
5. Serve hot.""",
            },
            {
                "title": "Tea",
                "ingredients": [
                    "1 cup water",
                    "1 teaspoon tea leaves (or 1 tea bag)",
                    "1 teaspoon sugar (optional)",
                    "Milk to taste (optional)",
                ],
                "instructions": """1. Bring water to a boil in a small saucepan.
2. Add tea leaves (or tea bag) and let it steep for 2-3 minutes.
3. If desired, add sugar and milk, then simmer for another minute.
4. Strain into a cup and serve hot.""",
            },
        ]

        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        self.search_label = tk.Label(self.window, text="Search", bg="#ea86b6")
        self.search_label.grid(column=0, row=0, padx=5)

        self.search_entry = tk.Entry(master=self.window, width=40)
        self.search_entry.grid(column=1, row=0, padx=5, pady=10)

        self.search_button = tk.Button(
            self.window,
            text="Search",
            highlightbackground="#ea86b6",
            command=self.__run_search_query,
        )
        self.search_button.grid(column=2, row=0, padx=5)

    def __run_search_query(self):
        query = self.search_entry.get().lower()
        ingredient_list = [ingredient.strip() for ingredient in query.split(",")]

        matching_recipes = [
            recipe
            for recipe in self.recipes
            if all(any(ingredient in ingredient_item.lower() for ingredient_item in recipe["ingredients"]) for ingredient in ingredient_list)
        ]

        if matching_recipes:
            recipe = matching_recipes[0]  
            recipe_label = recipe["title"]
            ingredients = recipe["ingredients"]
            instructions = recipe["instructions"]
        else:
            recipe_label = "Recipe Not Found"
            ingredients = ["No ingredients available."]
            instructions = "No instructions available."

        self.__show_recipe(recipe_label, ingredients, instructions)

    def __show_recipe(self, recipe_label, ingredients_list, instructions_text):
        ingredients = tk.Text(master=self.window, height=10, width=50, bg="#ffdada")
        ingredients.grid(column=1, row=4, pady=10)
        ingredients.delete("1.0", tk.END)

        ingredients.insert(tk.END, f"{recipe_label}\n\nIngredients:\n")
        for ingredient in ingredients_list:
            ingredients.insert(tk.END, f"- {ingredient}\n")

        instructions = tk.Text(master=self.window, height=10, width=50, bg="#daf8e3")
        instructions.grid(column=1, row=5, pady=10)
        instructions.delete("1.0", tk.END)

        instructions.insert(tk.END, "Instructions:\n")
        instructions.insert(tk.END, instructions_text)

    def run_search(self):
        self.window.mainloop()


if __name__ == "__main__":
    sugg_recipe = Recipe()
    sugg_recipe.run_search()
