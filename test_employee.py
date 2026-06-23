import unittest
import app


class TestEmployee(unittest.TestCase):

    def test_load_data_returns_list(self):
        data = app.load_data()
        self.assertIsInstance(data, list)

    def test_employee_count_is_valid(self):
        data = app.load_data()
        self.assertGreaterEqual(len(data), 0)

    def test_file_name_exists(self):
        self.assertEqual(app.FILE_NAME, "employees.json")


if __name__ == "__main__":
    unittest.main()