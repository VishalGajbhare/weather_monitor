import unittest
from backend.database import init_db, insert_daily_summary

class TestDatabase(unittest.TestCase):
    def test_init_db(self):
        init_db()  # Test if DB initializes without errors
    
    def test_insert_daily_summary(self):
        init_db()
        insert_daily_summary("Delhi", "2023-10-23", 30.0, 35.0, 25.0, "Clear")  # Test insert

if __name__ == '__main__':
    unittest.main()
