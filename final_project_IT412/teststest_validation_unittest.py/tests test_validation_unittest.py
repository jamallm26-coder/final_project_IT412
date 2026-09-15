import unittest
import validation

class TestValidation(unittest.TestCase):

    def test_name(self):
        self.assertTrue(validation.validate_name("John"))
        self.assertFalse(validation.validate_name("John123"))

    def test_state(self):
        self.assertTrue(validation.validate_state("MI"))
        self.assertFalse(validation.validate_state("ZZ"))

    def test_zip(self):
        self.assertTrue(validation.validate_zip("48009"))
        self.assertFalse(validation.validate_zip("ABC"))

if __name__ == "__main__":
    unittest.main()
