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

    # we can change how the list is printed
    def print_list(self):
        current_node = self.head
        while current_node:
            ingredient = current_node.ingredient
            print(ingredient.ingredient_name + " " + ingredient.ingredient_expiry_date)
            current_node = current_node.next
            