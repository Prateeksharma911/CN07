from cardValidationCheck import *
import unittest
class TestCuboid(unittest.TestCase):
    def test_validation(self):
        messageTrue="Test value is True but its False"
        messageFalse = "Test value is False but its True"
        self.assertFalse(cardValidCheck("4388576018402626"),messageTrue)
        self.assertTrue(cardValidCheck("4929294190436203"),messageFalse)
    def test_value(self):
        self.assertRaises(ValueError,cardValidCheck,"49292941")

if __name__ == '__main__':
    unittest.main()