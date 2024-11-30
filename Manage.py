from datetime import datetime

class Ingredient:
    def __init__(self, ingredient_name, ingredient_expiry_date):
        self.ingredient_name = ingredient_name
        self.ingredient_expiry_date = ingredient_expiry_date


class Node:
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_begin(self, ingredient):
        new_node = Node(ingredient)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

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
            print(ingredient.ingredient_name + " " + ingredient.ingredient_expiry_date)
            current_node = current_node.next

    def manage_ingredients(self):
        current = self.head
        today = datetime.now()
        expired_list = Linked_list()

        while current:
            ingredient = current.ingredient
            expiry_date = datetime.strptime(ingredient.ingredient_expiry_date, "%Y-%m-%d")

            difference = expiry_date - today
            difference_in_s = difference.total_seconds()

            days = difference.days
            days = divmod(difference_in_s, 86400)[0] + 1

            if expiry_date < today:
                self.remove_node(ingredient)
                expired_list.insert_end(ingredient)

            elif 0 <= days <= 3:
                self.remove_node(ingredient)
                self.insert_begin(ingredient)

            current = current.next

        print('Ingredient list: ')
        self.print_list()

        print('\nExpired list: ')
        expired_list.print_list()
        # return ingredient_list


ing1 = Ingredient('Apple', '2024-11-1')
ing2 = Ingredient('Banana', '2024-12-1')
ing3 = Ingredient('Carrot', '2025-1-1')
ing4 = Ingredient('Egg', '2024-11-11')
ing5 = Ingredient('Flour', '2024-11-24')
ing6 = Ingredient('Honey', '2024-11-30')
ing7 = Ingredient('Chocolate', '2024-12-2')

ingredient_list = Linked_list()
ingredient_list.insert_end(ing1)
ingredient_list.insert_end(ing2)
ingredient_list.insert_end(ing3)
ingredient_list.insert_end(ing4)
ingredient_list.insert_end(ing5)
ingredient_list.insert_end(ing6)
ingredient_list.insert_end(ing7)

ingredient_list.manage_ingredients()
