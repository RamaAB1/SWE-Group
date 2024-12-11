import unittest

from numpy import array_equal
from Manage import Ingredient, Linked_list

class Test_manage (unittest.TestCase):

    #Test list of ingredients that are all expired
    def test_list_all_expired (self):
        ing1 = Ingredient('Apple', '2024-11-1')
        ing2 = Ingredient('Banana', '2024-12-8')
        ing3 = Ingredient('Carrot', '2024-8-2')
        ing4 = Ingredient('Egg', '2023-11-11')
        ing5 = Ingredient('Flour', '2024-10-24')
        ing6 = Ingredient('Honey', '2024-11-25')
        ing7 = Ingredient('Milk', '2024-9-5')
        ing8 = Ingredient('Orange', '2023-12-3')

        list1 = Linked_list()
        list1.insert_end(ing1)
        list1.insert_end(ing2)
        list1.insert_end(ing3)
        list1.insert_end(ing4)
        list1.insert_end(ing5)
        list1.insert_end(ing6)
        list1.insert_end(ing7)
        list1.insert_end(ing8)

        manage_list = list1.manage_ingredients()
        ingredients_list = manage_list[0]
        expired_list = manage_list[1]
        
        self.assertTrue (array_equal(ingredients_list, []))
        self.assertTrue(array_equal(expired_list, [ing4, ing8, ing3, ing7, ing5, ing1, ing6, ing2]))


    #Test list of ingredients that are all not expired
    def test_list_all_available (self):
        ing1 = Ingredient('Apple', '2025-10-1')
        ing2 = Ingredient('Banana', '2025-7-1')
        ing3 = Ingredient('Carrot', '2025-12-2')
        ing4 = Ingredient('Egg', '2025-4-11')
        ing5 = Ingredient('Flour', '2025-6-24')
        ing6 = Ingredient('Honey', '2025-11-30')
        ing7 = Ingredient('Milk', '2025-8-5')
        ing8 = Ingredient('Orange', '2025-12-3')

        list1 = Linked_list()
        list1.insert_end(ing1)
        list1.insert_end(ing2)
        list1.insert_end(ing3)
        list1.insert_end(ing4)
        list1.insert_end(ing5)
        list1.insert_end(ing6)
        list1.insert_end(ing7)
        list1.insert_end(ing8)

        manage_list = list1.manage_ingredients()
        ingredients_list = manage_list[0]
        expired_list = manage_list[1]
        
        self.assertTrue(array_equal(ingredients_list, [ing4, ing5, ing2, ing7, ing1, ing6, ing3, ing8]))
        self.assertTrue (array_equal(expired_list, []))

    #Test list of expired and available ingredients
    def test_list_available_expired (self):
        ing1 = Ingredient('Apple', '2024-11-28')
        ing2 = Ingredient('Banana', '2025-7-1')
        ing3 = Ingredient('Carrot', '2024-12-25')
        ing4 = Ingredient('Egg', '2024-12-22')
        ing5 = Ingredient('Flour', '2023-11-10')
        ing6 = Ingredient('Honey', '2025-11-30')
        ing7 = Ingredient('Milk', '2024-12-5')
        ing8 = Ingredient('Orange', '2025-12-3')

        list1 = Linked_list()
        list1.insert_end(ing1)
        list1.insert_end(ing2)
        list1.insert_end(ing3)
        list1.insert_end(ing4)
        list1.insert_end(ing5)
        list1.insert_end(ing6)
        list1.insert_end(ing7)
        list1.insert_end(ing8)

        manage_list = list1.manage_ingredients()
        ingredients_list = manage_list[0]
        expired_list = manage_list[1]
        
        self.assertTrue(array_equal(ingredients_list, [ing4, ing3, ing2, ing6, ing8]))
        self.assertTrue (array_equal(expired_list, [ing5, ing1, ing7]))


if __name__ == '__main__':
    unittest.main()
