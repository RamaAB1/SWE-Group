import unittest
from datetime import datetime
from Extract_date import getDate

class Test_extract_date (unittest.TestCase):
    def test_example1 (self):
        today = str(datetime.now().day)
        excepted = "2025-09-" + today
        print(excepted)
        self.assertEqual(getDate("date1.jpeg"), excepted)

if __name__ == '__main__':
    unittest.main()
