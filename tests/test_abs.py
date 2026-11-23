from pathlib import Path
import subprocess
import sys
import unittest


ABS_DIR = Path(__file__).resolve().parents[1] / "contests" / "abs"


class AtCoderBeginnersSelectionTests(unittest.TestCase):
    def assert_output(self, script: str, stdin: str, expected: str) -> None:
        result = subprocess.run(
            [sys.executable, str(ABS_DIR / script)],
            input=stdin,
            text=True,
            capture_output=True,
            timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected)

    def test_practice_1(self):
        self.assert_output("practice_1.py", "4\n7 11\nhello\n", "22 hello\n")

    def test_even_product(self):
        self.assert_output("abc086_a.py", "3 4\n", "Even\n")

    def test_odd_product(self):
        self.assert_output("abc086_a.py", "9 7\n", "Odd\n")
