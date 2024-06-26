import unittest
import re
from datetime import datetime
import os
import tempfile
import sqlite3
import threading

# Unit Test - Ćwiczenie 1
# Write a Python unit test program to check if a given number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class TestPrimeFunction(unittest.TestCase):
    def test_is_prime(self):
        # Prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        # Non-prime numbers
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(22))
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(26))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(28))
        self.assertFalse(is_prime(30))

# Unit Test - Ćwiczenie 2
# Write a Python unit test program to check if a list is sorted in ascending order.
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

class TestSortingFunction(unittest.TestCase):
    def test_is_sorted(self):
        # Lists that are sorted
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([-5, -1, 0, 3, 8]))
        self.assertTrue(is_sorted([]))
        self.assertTrue(is_sorted([42]))
        # Lists that are not sorted
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([10, 1, 2, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 3, 5, 4]))
        self.assertFalse(is_sorted([3, 3, 2, 2, 1]))

# Unit Test - Ćwiczenie 3
# Write a Python unit test program that checks if two lists are equal.
def lists_are_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(a == b for a, b in zip(list1, list2))


class TestListEqualityFunction(unittest.TestCase):
    def test_lists_are_equal(self):
        # Lists that are equal
        self.assertTrue(lists_are_equal([1, 2, 3], [1, 2, 3]))
        self.assertTrue(lists_are_equal([], []))
        self.assertTrue(lists_are_equal([1], [1]))
        self.assertTrue(lists_are_equal(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertTrue(lists_are_equal([True, False], [True, False]))
        # Lists that are not equal
        self.assertFalse(lists_are_equal([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(lists_are_equal([1, 2, 3], [1, 2, 4]))
        self.assertFalse(lists_are_equal([1, 2, 3], [3, 2, 1]))
        self.assertFalse(lists_are_equal([], [1]))
        self.assertFalse(lists_are_equal(['a', 'b'], ['a', 'c']))
        self.assertFalse(lists_are_equal([True, False], [False, True]))

# Unit Test - Ćwiczenie 4
# Write a Python unit test program to check if a string is a palindrome.
def is_palindrome(s):
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

class TestPalindromeFunction(unittest.TestCase):
    def test_is_palindrome(self):
        # Palindromes
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_palindrome(""))
        # Non-palindromes
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("Python"))

# Unit Test - Ćwiczenie 5
# Write a Python unit test program to check if a file exists in a specified directory.
def file_exists(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

class TestFileExistenceFunction(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.existing_file = os.path.join(self.test_dir.name, 'existing_file.txt')
        with open(self.existing_file, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_file_exists(self):
        # Test case where the file exists
        self.assertTrue(file_exists(self.test_dir.name, 'existing_file.txt'))

        # Test case where the file does not exist
        self.assertFalse(file_exists(self.test_dir.name, 'non_existent_file.txt'))

        # Test case where the directory does not exist
        self.assertFalse(file_exists('non_existent_dir', 'existing_file.txt'))

# Unit Test - Ćwiczenie 6
# Write a Python unit test that checks if a function handles floating-point calculations accurately.
def add_floats(a, b):
    return a + b

class TestFloatingPointCalculations(unittest.TestCase):
    def test_add_floats(self):
        # Floating-point addition
        self.assertAlmostEqual(add_floats(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(add_floats(-1.5, 1.5), 0.0, places=7)
        self.assertAlmostEqual(add_floats(1.123456, 2.654321), 3.777777, places=7)
        self.assertAlmostEqual(add_floats(1e-7, 2e-7), 3e-7, places=14)
        self.assertAlmostEqual(add_floats(1.0000001, -0.0000001), 1.0, places=7)
        # Edge cases
        self.assertAlmostEqual(add_floats(0.0, 0.0), 0.0, places=7)
        self.assertAlmostEqual(add_floats(1e10, 1e-10), 1e10, places=7)

# Unit Test - Ćwiczenie 7
# Write a Python unit test program to check if a function handles multi-threading correctly.
class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

def increment_counter(counter, num_increments):
    threads = []
    for _ in range(num_increments):
        thread = threading.Thread(target=counter.increment)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

class TestMultiThreading(unittest.TestCase):
    def test_increment_counter(self):
        counter = Counter()
        num_increments = 1000

        increment_counter(counter, num_increments)

        self.assertEqual(counter.value, num_increments)

# Unit Test - Ćwiczenie 8
# Write a Python unit test program to check if a database connection is successful.
def connect_to_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

class TestDatabaseConnection(unittest.TestCase):
    def test_connect_to_database_success(self):
        db_name = ":memory:"
        conn = connect_to_database(db_name)
        self.assertIsNotNone(conn)
        conn.close()

    def test_connect_to_database_failure(self):
        db_name = "/invalid/path/to/database.db"
        conn = connect_to_database(db_name)
        self.assertIsNone(conn)

# Unit Test - Ćwiczenie 9
# Write a Python unit test program to check if a database query returns the expected results.
def execute_query(conn, query):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Query execution failed: {e}")
        return None

class TestDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.create_table()
        self.insert_data()

    def tearDown(self):
        self.conn.close()

    def create_table(self):
        create_table_query = """
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
        execute_query(self.conn, create_table_query)

    def insert_data(self):
        insert_data_query = """
        INSERT INTO test_table (name) VALUES
        ('Alice'),
        ('Bob'),
        ('Charlie');
        """
        execute_query(self.conn, insert_data_query)

    def test_query_results(self):
        query = "SELECT * FROM test_table;"
        expected_results = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
        results = execute_query(self.conn, query)
        self.assertEqual(results, expected_results)

    def test_empty_query_results(self):
        query = "DELETE FROM test_table;"
        execute_query(self.conn, query)
        query = "SELECT * FROM test_table;"
        expected_results = []
        results = execute_query(self.conn, query)
        self.assertEqual(results, expected_results)

# Unit Test - Ćwiczenie 10
# Write a Python unit test program to check if a function correctly parses and validates input data.
def parse_and_validate_date(date_str):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'

    if not re.match(date_pattern, date_str):
        return False

    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestParseAndValidateDateFunction(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(parse_and_validate_date("2023-06-25"))
        self.assertTrue(parse_and_validate_date("2000-01-01"))
        self.assertTrue(parse_and_validate_date("1999-12-31"))
        self.assertTrue(parse_and_validate_date("2024-02-29"))

    def test_invalid_dates(self):
        self.assertFalse(parse_and_validate_date("2023-13-25"))
        self.assertFalse(parse_and_validate_date("2023-06-32"))
        self.assertFalse(parse_and_validate_date("2023-2-29"))
        self.assertFalse(parse_and_validate_date("2023/06/25"))
        self.assertFalse(parse_and_validate_date("25-06-2023"))
        self.assertFalse(parse_and_validate_date("2021-02-29"))

    def test_invalid_format(self):
        self.assertFalse(parse_and_validate_date("June 25, 2023"))
        self.assertFalse(parse_and_validate_date("20230625"))
        self.assertFalse(parse_and_validate_date("2023-06"))
        self.assertFalse(parse_and_validate_date("2023-06-25-12"))

if __name__ == '__main__':
    unittest.main()