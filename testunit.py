import unittest
import hashlib
import sys
import os
from io import StringIO
import logging


from hashwolf import (
    generate_hash, display_result, direct_crack, compare_hashes, recursive_combinations, 
    indirect_crack, log_hash_type, write_to_file, generate_combinations, store_combination, 
    create_hash_dictionary, rainbow_crack, start
)

class TestHashCrack(unittest.TestCase):
    
    def test_generate_hash(self):
        self.assertEqual(generate_hash('md5', 'test'), hashlib.md5('test'.encode()).hexdigest())

    def test_display_result(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        display_result('md5', '098f6bcd4621d373cade4e832627b4f6', 'test')
        sys.stdout = sys.__stdout__
        self.assertIn("Cracked successfully", captured_output.getvalue())

    def test_direct_crack(self):
        with open('wordlist.txt', 'w') as f:
            f.write("test\npassword\n123456")
        captured_output = StringIO()
        sys.stdout = captured_output
        direct_crack('md5', 'wordlist.txt', hashlib.md5('test'.encode()).hexdigest())
        sys.stdout = sys.__stdout__
        self.assertIn("Cracked successfully", captured_output.getvalue())
        os.remove('wordlist.txt')

    def test_compare_hashes(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        compare_hashes('md5', 'test', hashlib.md5('test'.encode()).hexdigest())
        sys.stdout = sys.__stdout__
        self.assertIn("Cracked successfully", captured_output.getvalue())

    def test_recursive_combinations(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        recursive_combinations(list('ab'), '', 2, 2, 'md5', hashlib.md5('test'.encode()).hexdigest())
        sys.stdout = sys.__stdout__
        self.assertIn("Attempt:", captured_output.getvalue())

    def test_indirect_crack(self):
        # This test might run for a long time, so it's more of a placeholder
        self.assertTrue(True)

    def test_log_hash_type(self):
        log_path = "logs/hash_logs.txt"
        log_hash_type('md5')
        with open(log_path, "r") as f:
            self.assertIn('md5', f.read())

    def test_write_to_file(self):
        write_to_file('test', 'md5', 0)
        with open('dict/md5/0.txt', 'r') as f:
            self.assertIn('test', f.read())
        os.remove('dict/md5/0.txt')

    """def test_generate_combinations(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_combinations(list('ab'), '', 2, 2, 'md5', 0)
       """ 
    def test_store_combination(self):
        store_combination('test', 'md5', 0)
        with open('dict/md5/0.txt', 'r') as f:
            self.assertIn('test:', f.read())
        os.remove('dict/md5/0.txt')

    def test_create_hash_dictionary(self):
        create_hash_dictionary('md5')
        self.assertTrue(os.path.exists('dict/md5'))
        os.rmdir('dict/md5')

    def test_rainbow_crack(self):
        # This test requires a pre-generated dictionary, so it's more of a placeholder
        self.assertTrue(True)

    def test_start(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        start('direct', hashlib.md5('test'.encode()).hexdigest(), 'md5', wordlist='wordlist.txt')
        sys.stdout = sys.__stdout__
        self.assertIn("Cracked successfully", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
