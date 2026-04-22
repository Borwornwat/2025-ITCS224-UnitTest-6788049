import unittest
def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    else:
        return f"Invalid age: {age}"

class test_child_age(unittest.TestCase):
    def test_is_child(self):
        for number in range(0,10):
            with self.subTest(number=number):
                print(f"\n{number} is considered as a child.")
                self.assertEqual(categorize_by_age(number), "Child")
    def test_is_adolescent(self):
        for number in range(10,19):
            with self.subTest(number=number):
                print(f"\n{number} is considered as a adolescent.")
                self.assertEqual(categorize_by_age(number), "Adolescent")
    def test_is_adult(self):
        for number in range(19,66):
            with self.subTest(number=number):
                print(f"\n{number} is considered as a adult.")
                self.assertEqual(categorize_by_age(number), "Adult")


if __name__ == "__main__":
    unittest.main(verbosity=2)