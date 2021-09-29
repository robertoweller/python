import unittest

# unittest.TestCase.assertEqual(20, 20)

class Somar(unittest.TestCase):
    def test_principal(self):
        self.assertEqual(20.0, 20)


if __name__ == '__name__':
    unittest.main()
