class Ingredient:
    def __init__(self, ingredient_name, ingredient_expiry_date):
        self.ingredient_name = ingredient_name
        self.ingredient_expiry_date = ingredient_expiry_date

    def toString (self):
        return (self.ingredient_name + " " + self.ingredient_expiry_date)

class Node:
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_end(self, ingredient):
        new_node = Node(ingredient)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_node(self, ingredient):
        current_node = self.head

        if current_node.ingredient == ingredient:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.ingredient != ingredient:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            ingredient = current_node.ingredient
            print(ingredient.toString())
            current_node = current_node.next
    
    def linked_list_to_array(self):
        arr = []
        current_node = self.head

        while current_node:
            ingredient = current_node.ingredient
            arr.append(ingredient)
            current_node = current_node.next

        return arr
    
def print_array (arr):
    for ingredient in arr:
        print (ingredient.toString())

ing1 = Ingredient('Apple', '2024-11-1')
ing2 = Ingredient('Banana', '2024-12-8')
ing3 = Ingredient('Carrot', '2024-8-2')
ing4 = Ingredient('Egg', '2023-11-11')
ing5 = Ingredient('Flour', '2024-10-24')
ing6 = Ingredient('Honey', '2024-11-25')
ing7 = Ingredient('Milk', '2024-9-5')
ing8 = Ingredient('Orange', '2023-12-3')
ing9 = Ingredient('Strawberry', '2025-10-1')
ing10 = Ingredient('Blueberries', '2025-7-1')
ing11 = Ingredient('Salmon', '2025-12-2')
ing12 = Ingredient('Chicken', '2025-4-11')
ing13 = Ingredient('Butter', '2025-6-24')
ing14 = Ingredient('Sea bass', '2025-11-30')
ing15 = Ingredient('Eggplant', '2025-8-5')
ing16 = Ingredient('Onion', '2025-12-3')
ing17 = Ingredient('broccoli', '2024-11-28')
ing18 = Ingredient('Shrimp', '2025-7-1')
ing19 = Ingredient('Yogurt', '2024-12-25')
ing20 = Ingredient('Pineapple', '2024-12-22')
ing21 = Ingredient('Fresh cream', '2023-11-10')
ing22 = Ingredient('Mushroom', '2025-11-30')
ing23 = Ingredient('Oats', '2024-12-5')
ing24 = Ingredient('Lentil', '2025-12-3')

list = Linked_list()
list.insert_end(ing1)
list.insert_end(ing2)
list.insert_end(ing3)
list.insert_end(ing4)
list.insert_end(ing5)
list.insert_end(ing6)
list.insert_end(ing7)
list.insert_end(ing8)
list.insert_end(ing9)
list.insert_end(ing10)
list.insert_end(ing11)
list.insert_end(ing12)
list.insert_end(ing12)
list.insert_end(ing14)
list.insert_end(ing15)
list.insert_end(ing16)
list.insert_end(ing17)
list.insert_end(ing18)
list.insert_end(ing19)
list.insert_end(ing20)
list.insert_end(ing21)
list.insert_end(ing22)
list.insert_end(ing23)
list.insert_end(ing24)
