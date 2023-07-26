import unittest

class Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def can_vote(self):
        return self.__age > 18

class MyTests(unittest.TestCase):
    def setUp(self):
        self.person = Person("person1", "pune", 18)

    def test_can_vote(self):
        assert self.person.can_vote() == True

if __name__ == '__main__':
    unittest.main()
