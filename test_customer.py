import os
import csv
import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        # Run before each test
        self.test_file = "test_customers.csv"
        # Remove file if it exists so we start fresh
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_to_csv_creates_file(self):
        # Create a Customer and save to test file
        c = Customer("Angela", "Fernandez", "555-1234", "angela@email.com",
                     "123 Main St", "Simi Valley", "CA", "93065",
                     "4111111111111111", "12", "2025", "123", "93065")
        c.save_to_csv(self.test_file)

        # ✅ Check file exists
        self.assertTrue(os.path.isfile(self.test_file))

    def test_save_to_csv_writes_data(self):
        c = Customer("Angela", "Fernandez", "555-1234", "angela@email.com",
                     "123 Main St", "Simi Valley", "CA", "93065",
                     "4111111111111111", "12", "2025", "123", "93065")
        c.save_to_csv(self.test_file)

        # ✅ Read back the file
        with open(self.test_file, newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))
        
        # First row should be header
        self.assertEqual(reader[0][0], "First Name")
        # Second row should contain Angela
        self.assertEqual(reader[1][0], "Angela")
        self.assertEqual(reader[1][1], "Fernandez")

    def tearDown(self):
        # Run after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
