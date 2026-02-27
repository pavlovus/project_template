import unittest
import os
from app.io.input import input_from_file_with_pandas, input_from_file

class TestFileInput(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_input_from_file_reads_text(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("Hello World")

        result = input_from_file(self.test_file)
        self.assertEqual(result, "Hello World")

    def test_input_from_file_empty(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("")

        result = input_from_file(self.test_file)
        self.assertEqual(result, "")

    def test_input_from_file_multiline(self):
        content = "Line1\nLine2\nLine3"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(content)

        result = input_from_file(self.test_file)
        self.assertEqual(result, content)

    def test_input_from_file_with_pandas_reads_text(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("Hello World")

        result = input_from_file_with_pandas(self.test_file)
        self.assertEqual(result.strip(), "Hello World")

    def test_input_from_file_with_pandas_empty(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("")

        result = input_from_file_with_pandas(self.test_file)
        self.assertEqual(result.strip(), "")

    def test_input_from_file_with_pandas_multiline(self):
        content = "Line1\nLine2\nLine3"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(content)

        result = input_from_file_with_pandas(self.test_file)
        self.assertEqual(result.strip(), content)

if __name__ == "__main__":
    unittest.main()