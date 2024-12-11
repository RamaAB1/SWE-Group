import unittest

from VIEW_STORED_EXPIRED_ITEMS_NOTIFICATIONS import main


class TestSum(unittest.TestCase):
    def test_list_output(self):
        """
        Test the main function
        """
        result = main()
        output = ("Ingredient list:\Carrot 2025-1-1\n\n"
        "Expired list:\nApple 2024-11-1\nBanana 2024-12-1\nEgg 2024-11-11\n"
        "Flour 2024-11-24\nHoney 2024-11-30\nChocolate 2024-12-2\n")
        
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
