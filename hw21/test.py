import unittest
import os
from index import FileContextManager

# Task 2
# Writing tests for context manager
# Take your implementation of the context manager class 
# from Task 1 and write tests for it. Try to cover 
# as many use cases as you can, positive ones when a file exists 
# and everything works as designed. And also, write tests 
# when your class raises errors or you have errors in the runtime context suite.

class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        with open('test_log.txt', 'w') as file:
            file.write('File test_log.txt is opened\n')

    def tearDown(self):
        os.remove('test_log.txt')

    def test_read_file(self):
        with FileContextManager('test_log.txt', 'r') as file:
            file_content = file.read()
            self.assertIn('File test_log.txt is opened', file_content)

    def test_get_count(self):
        with FileContextManager('test_log.txt', 'r') as file:
            with FileContextManager('test_log.txt', 'r') as file:
                self.assertEqual(FileContextManager.counter, 2)

    def test_file_is_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with FileContextManager('not_existing_file.txt', 'r') as file:
                pass


if __name__ == '__main__':
    unittest.main()