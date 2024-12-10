from datetime import datetime
from Extract_date import getDate

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
    
def array_to_linked_list(arr):
    
    list = Linked_list()
    for item in arr:
        list.insert_end(item)

    return list

def print_array (arr):
    for ingredient in arr:
        print (ingredient.toString())


ing1 = Ingredient('Apple', getDate("date1.jpeg"))
ing2 = Ingredient('Egg', getDate("date2.jpeg"))
ing3 = Ingredient('Carrot', getDate('date3.jpeg'))
ing4 = Ingredient('Banana', '2024-12-2')
ing5 = Ingredient('Flour', '2024-11-24')
ing6 = Ingredient('Honey', '2024-11-30')
ing7 = Ingredient('Milk', '2025-12-10')
ing8 = Ingredient('Orange', '2025-12-6')

list1 = Linked_list()
list1.insert_end(ing1)
list1.insert_end(ing2)
list1.insert_end(ing3)
list1.insert_end(ing4)
list1.insert_end(ing5)
list1.insert_end(ing6)
list1.insert_end(ing7)
list1.insert_end(ing8)
result = list1.manage_ingredients()

print("Ingredient list: ")
print_array(result[0])

print("\nExpired list:")
print_array(result[1])
