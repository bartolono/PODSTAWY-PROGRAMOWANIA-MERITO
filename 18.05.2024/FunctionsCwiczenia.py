def exercise1():
    # Functions - Ćwiczenie 1
    # Write a Python function to find the maximum of three numbers.
    def max_of_three(a, b, c):
        return max(a, b, c)

    print(max_of_three(3, 6, -5))
    print("")
    return main()

def exercise2():
    # Functions - Ćwiczenie 2
    # Write a Python function to sum all the numbers in a list.
    def sum_list(numbers):
        return sum(numbers)

    print(sum_list([8, 2, 3, 0, 7]))
    print("")
    return main()

def exercise3():
    # Functions - Ćwiczenie 3
    # Write a Python function to multiply all the numbers in a list.
    def multiply_list(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

    print(multiply_list([8, 2, 3, -1, 7]))
    print("")
    return main()

def exercise4():
    # Functions - Ćwiczenie 4
    # Write a Python program to reverse a string.
    def reverse_string(s):
        return s[::-1]

    print(reverse_string("1234abcd"))
    print("")
    return main()

def exercise5():
    # Functions - Ćwiczenie 5
    # Write a Python function to calculate the factorial of a number (a non-negative integer).
    # The function accepts the number as an argument.
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    n = int(input("Input a number to compute the factorial: "))
    print(factorial(n))
    print("")
    return main()

def exercise6():
    # Functions - Ćwiczenie 6
    # Write a Python function to check whether a number falls within a given range.
    def is_in_range(n, start, end):
        if n in range(start, end):
            print(f"{n} is in the range {start}-{end}.")
        else:
            print(f"{n} is outside the range {start}-{end}.")

    is_in_range(5, 3, 9)
    print("")
    return main()

def exercise7():
    # Functions - Ćwiczenie 7
    # Write a Python function that accepts a string and counts the number of upper and lower case letters.
    def count_upper_lower(s):
        upper_count = sum(1 for char in s if char.isupper())
        lower_count = sum(1 for char in s if char.islower())
        return upper_count, lower_count

    upper, lower = count_upper_lower('The quick Brown Fox')
    print(f"No. of Upper case characters: {upper}")
    print(f"No. of Lower case characters: {lower}")
    print("")
    return main()

def exercise8():
    # Functions - Ćwiczenie 8
    # Write a Python function that takes a list and returns a new list with distinct elements from the first list.
    def unique_list(l):
        return list(set(l))

    print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
    print("")
    return main()

def exercise9():
    # Functions - Ćwiczenie 9
    # Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    print(is_prime(11))
    print(is_prime(13))
    print(is_prime(16))
    print(is_prime(17))
    print(is_prime(97))
    print("")
    return main()

def exercise10():
    # Functions - Ćwiczenie 10
    # Write a Python program to print the even numbers from a given list.
    def even_numbers(l):
        return [num for num in l if num % 2 == 0]

    print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("")
    return main()

def exercise11():
    # Functions - Cwiczenie 11
    # Write a Python function to check whether a number is "Perfect" or not.
    def is_perfect(n):
        if n < 1:
            return False
        divisors_sum = sum(i for i in range(1, n) if n % i == 0)
        return divisors_sum == n

    print(is_perfect(6))
    print(is_perfect(28))
    print(is_perfect(10))
    print("")
    return main()

def exercise12():
    # Functions - Ćwiczenie 12
    # Write a Python function that checks whether a passed string is a palindrome or not.
    def is_palindrome(s):
        return s == s[::-1]

    print(is_palindrome("aza"))
    print(is_palindrome("hello"))
    print("")
    return main()

def exercise13():
    # Functions - Ćwiczenie 13
    # Write a Python function that prints out the first n rows of Pascal's triangle.
    def pascal_triangle(n):
        trow = [1]
        y = [0]

        for x in range(max(n, 0)):
            print(trow)
            trow = [l + r for l, r in zip(trow + y, y + trow)]

        return n >= 1

    pascal_triangle(6)
    print("")
    return main()

def exercise14():
    # Functions - Ćwiczenie 14
    # Write a Python function to check whether a string is a pangram or not.
    import string

    def is_pangram(s):
        alphabet = set(string.ascii_lowercase)
        return alphabet <= set(s.lower())

    print(is_pangram("The quick brown fox jumps over the lazy dog"))
    print(is_pangram("Hello World"))
    print("")
    return main()

def exercise15():
    # Functions - Ćwiczenie 15
    # Write a Python program that accepts a hyphen-separated sequence of words as
    # input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
    def sort_hyphenated_sequence(sequence):
        items = sequence.split('-')
        items.sort()
        return '-'.join(items)

    sequence = input()
    print(sort_hyphenated_sequence(sequence))
    print("")
    return main()

def exercise16():
    # Functions - Ćwiczenie 16
    # Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30
    # (both included).
    def squares_list():
        return [i ** 2 for i in range(1, 31)]

    print(squares_list())
    print("")
    return main()

def exercise17():
    # Functions - Ćwiczenie 17
    # Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
    def make_bold(func):
        def wrapper():
            return "<b>" + func() + "</b>"

        return wrapper

    def make_italic(func):
        def wrapper():
            return "<i>" + func() + "</i>"

        return wrapper

    def make_underline(func):
        def wrapper():
            return "<u>" + func() + "</u>"

        return wrapper

    @make_bold
    @make_italic
    @make_underline
    def hello():
        return "Hello, world!"

    print(hello())
    print("")
    return main()

def exercise18():
    # Functions - Ćwiczenie 18
    # Write a Python program to execute a string containing Python code.
    def execute_code(code):
        exec(code)

    code_string = "print('hello world')"
    execute_code(code_string)

    code_string = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is:',mutiply(2,3))
"""
    execute_code(code_string)
    print("")
    return main()

def exercise19():
    # Functions - Ćwiczenie 19
    # Write a Python program to access a function inside a function.
    def test(a):
        def add(b):
            nonlocal a
            a += 1
            return a + b

        return add

    func = test(4)
    print(func(4))
    print("")
    return main()

def exercise20():
    # Functions - Ćwiczenie 20
    # Write a Python program to detect the number of local variables declared in a function.
    def local_variables_count():
        a = 1
        b = 2
        c = "w3resource"
        print("Python Exercises")

    print(local_variables_count.__code__.co_nlocals)
    print("")
    return main()

def exercise21():
    # Functions - Ćwiczenie 21
    # Write a Python program that invokes a function after a specified period of time.
    import time
    import math

    def delayed_execution(milliseconds, func, *args):
        time.sleep(milliseconds / 1000)
        return func(*args)

    print("Square root after specific milliseconds:")
    print(delayed_execution(1000, math.sqrt, 16))
    print(delayed_execution(2000, math.sqrt, 100))
    print(delayed_execution(3000, math.sqrt, 25100))
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
        '1': exercise1,
        '2': exercise2,
        '3': exercise3,
        '4': exercise4,
        '5': exercise5,
        '6': exercise6,
        '7': exercise7,
        '8': exercise8,
        '9': exercise9,
        '10': exercise10,
        '11': exercise11,
        '12': exercise12,
        '13': exercise13,
        '14': exercise14,
        '15': exercise15,
        '16': exercise16,
        '17': exercise17,
        '18': exercise18,
        '19': exercise19,
        '20': exercise20,
        '21': exercise21,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 1 do 21), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '18' wczyta ćwiczenie 18). Wpisz 'wyjdź' aby wyjść z programu: ")
        if exercise_name == 'wyjdź':
            break

        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            result = exercise_function()
            if result is not None:
                print(result)
            else:
                break
        else:
            print("Nie znaleziono ćwiczenia.")

if __name__ == "__main__":
    main()