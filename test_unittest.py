import unittest

class testCase(unittest.TestCase):
    def testAddition(self):
        result = 10 + 3
        self.assertEqual(result, 13)  

    def testSubtraction(self):
        result = 10 - 5
        self.assertEqual(result, 5)  
    
    def testMultiply(self):
        result = 5 * 2
        self.assertEqual(result, 10)

    def testDivide(self):
        result = 20 / 2
        self.assertEqual(result, 10)
        
if __name__ == '__main__':
    unittest.main()
