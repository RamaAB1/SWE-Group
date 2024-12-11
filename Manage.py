from datetime import datetime

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


    def manage_ingredients(self):
        current = self.head
        today = datetime.now()
        expired_list = Linked_list()

        while current:
            ingredient = current.ingredient
            if (ingredient.ingredient_expiry_date != "Image not found" and ingredient.ingredient_expiry_date is not None):
                expiry_date = datetime.strptime(ingredient.ingredient_expiry_date, "%Y-%m-%d")

                if expiry_date < today:
                    self.remove_node(ingredient)
                    expired_list.insert_end(ingredient)

            #removes ingredient if date or image was not found
            #can be changed to allow the user to add ingredient manually
            else:
                self.remove_node(ingredient)
            
            current = current.next

        ing_sort = self.linked_list_to_array()
        ing_sort.sort(key = lambda ing: datetime.strptime(ing.ingredient_expiry_date, "%Y-%m-%d"))

        exp_sort = expired_list.linked_list_to_array()
        exp_sort.sort(key = lambda ing: datetime.strptime(ing.ingredient_expiry_date, "%Y-%m-%d"))

        return ing_sort, exp_sort

def print_array (arr):
    for ingredient in arr:
        print (ingredient.toString())
