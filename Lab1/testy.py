import unittest

def add(numbers):
    sum = 0
    if numbers == (""):
        return 0
    num = numbers.replace("\n", ",")
    liczby = num.split(",")

    for i in liczby:
        if i.isdigit() == True:
            sum += int(i)
        else:
            raise ValueError("not correct input")
    return sum



class TestApp(unittest.TestCase):

    def test1(self):
        self.assertEqual(add("1,2"), 3)

    def test2(self):
        self.assertEqual(add(""), 0)

    def test3(self):
        self.assertEqual(add("1,2,3"), 6)

    def test4(self):
        with self.assertRaises(ValueError):
            add("1,a")

    def test5(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test6(self):
        with self.assertRaises(ValueError):
            add("1,\n")



