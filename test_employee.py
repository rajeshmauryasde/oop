import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Rajesh", "Kumar", 0, None)
        self.assertEqual(e.get_full_name(), "Rajesh, Kumar")


if __name__ == '__main__':
    unittest.main()
