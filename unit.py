import unittest
def factorial(x):
    for i in range(1, x):
        x *= i
    return x
def cos(x):
    x *= 3.1415926 / 180
    value = 1
    sign = -1
    for i in range(2, 100, 2):
        value += (x ** i / factorial(i) * sign)
        sign *= -1
    return round(value, 4)
class FunctionTestCase(unittest.TestCase):
    def test_fact(self):
       self.assertEqual(factorial(10), 3628800)
    def test_cos(self):
        self.assertEqual(cos(180), -1.0)
unittest.main()
