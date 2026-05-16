import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parent / "session 4 prime number checker.py"
SPEC = importlib.util.spec_from_file_location("prime_checker", MODULE_PATH)
prime_checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prime_checker)


class PrimeCheckerTests(unittest.TestCase):
    def test_is_prime_handles_basic_cases(self):
        self.assertFalse(prime_checker.is_prime(1))
        self.assertTrue(prime_checker.is_prime(2))
        self.assertTrue(prime_checker.is_prime(13))
        self.assertFalse(prime_checker.is_prime(12))

    def test_calculator_operations(self):
        self.assertEqual(prime_checker.calculator(2, 3, "add"), 5)
        self.assertEqual(prime_checker.calculator(5, 3, "subtract"), 2)
        self.assertEqual(prime_checker.calculator(2, 3, "multiply"), 6)
        self.assertEqual(prime_checker.calculator(6, 2, "divide"), 3)
        self.assertEqual(prime_checker.calculator(6, 0, "divide"), "cant divide by zero")
        self.assertEqual(prime_checker.calculator(1, 1, "mod"), "wrong operation")


if __name__ == "__main__":
    unittest.main()
