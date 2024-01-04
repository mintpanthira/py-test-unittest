import unittest
from funct_math import add, subtract, multiply, divide

class TestMyMath(unittest.TestCase):

    def setUp(self):
        self.x = 10
        self.y = 5
    
    def test_add(self):
        result = add(self.x, self.y)
        self.assertEqual(result, 15)  
        print(result)

    def test_subtract(self):
        result = subtract(self.x, self.y)
        self.assertEqual(result, 5)
        print(result)

    def test_multiply(self):
        result = multiply(self.x, self.y)
        self.assertEqual(result, 50)
        print(result)
    
    def test_divide(self):
        result = divide(self.x, self.y)
        self.assertEqual(result, 2)
        print(result)

    def test_divide_error(self):
        a = 10
        b = 0
        with self.assertRaises(ValueError):
            divide(a, b)


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        result = add(10, 10)
        self.assertEqual(result, 20)  

    def test_add_minos(self):
        result = add(-10, 5)
        self.assertEqual(result, -5)  
    
    def test_add_zero(self):
        result = add(-10, 10)
        self.assertEqual(result, 0)  
    
    def test_add_negative(self):
        result = add(-10, -10)
        self.assertEqual(result, -20)  

    def test_add_positive_negative(self):
        result = add(20, -10)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
