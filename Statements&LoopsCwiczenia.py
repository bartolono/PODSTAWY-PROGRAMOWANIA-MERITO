def exercise11():
    # Conditional Statements and Loops - Ćwiczenie 11
    # Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.
    # The element value in the i-th row and j-th column of the array should be i*j.
    def generate_2d_array(rows, columns):
        array_2d = []

        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(i * j)
            array_2d.append(row)

        return array_2d

    rows = 3
    columns = 4

    result = generate_2d_array(rows, columns)

    print("Result:", result)
    print("")
    return main()

def exercise12():
    # Conditional Statements and Loops - Ćwiczenie 12
    # Write a Python program that accepts a sequence of lines (blank line to terminate)
    # as input and prints the lines as output (all characters in lower case).
    def print_lowercase_lines():
        lines = []
        while True:
            line = input("Enter a line (blank line to terminate): ")
            if line.strip() == "":
                break
            lines.append(line.lower())

        for line in lines:
            print(line)

    print("Enter lines. Press Enter on a blank line to finish.")
    print_lowercase_lines()
    print("")
    return main()

def exercise13():
    # Conditional Statements and Loops - Ćwiczenie 13
    # Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input.
    # The program will print the numbers that are divisible by 5 in a comma separated sequence.
    def binary_divisible_by_5(numbers):
        numbers_list = numbers.split(',')
        divisible_by_5 = []

        for binary_num in numbers_list:
            decimal_num = int(binary_num, 2)
            if decimal_num % 5 == 0:
                divisible_by_5.append(binary_num)

        return ','.join(divisible_by_5)

    input_numbers = "0100,0011,1010,1001,1100,1001"

    result = binary_divisible_by_5(input_numbers)

    print("Sample Data:", input_numbers)
    print("Numbers divisible by 5:", result)
    print("")
    return main()

def exercise14():
    # Conditional Statements and Loops - Ćwiczenie 14
    # Write a Python program that accepts a string and calculates the number of digits and letters.
    def count_digits_and_letters(string):
        num_digits = 0
        num_letters = 0

        for char in string:
            if char.isdigit():
                num_digits += 1
            elif char.isalpha():
                num_letters += 1

        return num_letters, num_digits

    input_string = "Python 3.2"

    letters, digits = count_digits_and_letters(input_string)

    print("Sample Data:", input_string)
    print("Letters:", letters)
    print("Digits:", digits)
    print("")
    return main()

def exercise15():
    # Conditional Statements and Loops - Ćwiczenie 15
    # Write a Python program to check the validity of passwords input by users.
    import re

    def validate_password(password):
        has_lowercase = re.search("[a-z]", password)
        has_uppercase = re.search("[A-Z]", password)
        has_digit = re.search("[0-9]", password)
        has_special_char = re.search("[$#@]", password)

        is_valid = (
                has_lowercase and
                has_uppercase and
                has_digit and
                has_special_char and
                6 <= len(password) <= 16
        )

        return is_valid

    password = input("Enter your password: ")

    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is not valid. Please make sure it meets the requirements.")
    print("")
    return main()

def exercise16():
    # Conditional Statements and Loops - Ćwiczenie 16
    # Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number
    # is an even number. The numbers obtained should be printed in a comma-separated sequence.
    def find_even_digit_numbers():
        even_digit_numbers = []

        for num in range(100, 401):
            num_str = str(num)
            if all(int(digit) % 2 == 0 for digit in num_str):
                even_digit_numbers.append(num_str)

        return ','.join(even_digit_numbers)

    result = find_even_digit_numbers()

    print("Numbers with even digits between 100 and 400:", result)
    print("")
    return main()

def exercise17():
    # Conditional Statements and Loops - Ćwiczenie 17
    # Write a Python program to print the alphabet pattern 'A'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 0) or (
                    (row == 0 or row == 3) and (column > 1 and column < 5))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise18():
    # Conditional Statements and Loops - Ćwiczenie 18
    # Write a Python program to print the alphabet pattern 'D'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (
                    column == 5 and row != 0 and row != 6)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise19():
    # Conditional Statements and Loops - Ćwiczenie 19
    # Write a Python program to print the alphabet pattern 'E'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (
                    row == 3 and column > 1 and column < 5)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise20():
    # Conditional Statements and Loops - Ćwiczenie 20
    # Write a Python program to print the alphabet pattern 'G'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (
                    row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise21():
    # Conditional Statements and Loops - Ćwiczenie 21
    # Write a Python program to print the alphabet pattern 'L'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or (row == 6 and column != 0 and column < 6)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise22():
    # Conditional Statements and Loops - Ćwiczenie 22
    # Write a Python program to print the alphabet pattern 'M'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (
                    row == 3 and column == 3)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise23():
    # Conditional Statements and Loops - Ćwiczenie 23
    # Write a Python program to print the alphabet pattern 'O'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 0 and row != 6) or (
                    (row == 0 or row == 6) and column > 1 and column < 5)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise24():
    # Conditional Statements and Loops - Ćwiczenie 24
    # Write a Python program to print the alphabet pattern 'P'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or (
                    (column == 5 or column == 1) and (row == 1 or row == 2))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise25():
    # Conditional Statements and Loops - Ćwiczenie 25
    # Write a Python program to print the alphabet pattern 'R'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (
                    column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise26():
    # Conditional Statements and Loops - Ćwiczenie 26
    # Write a Python program to print the following patterns.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or
                    (column == 1 and (row == 1 or row == 2 or row == 6)) or
                    (column == 5 and (row == 0 or row == 4 or row == 5))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)

    row = 15
    col = 18
    result_str = ""

    for i in range(1, row + 1):
        if ((i <= 3) or (i >= 7 and i <= 9) or (i >= 13 and i <= 15)):
            for j in range(1, col):
                result_str = result_str + "o"
            result_str = result_str + "\n"
        elif (i >= 4 and i <= 6):
            for j in range(1, 5):
                result_str = result_str + "o"
            result_str = result_str + "\n"
        else:
            for j in range(1, 14):
                result_str = result_str + " "
            for j in range(1, 5):
                result_str = result_str + "o"
            result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise27():
    # Conditional Statements and Loops - Ćwiczenie 27
    # Write a Python program to print the alphabet pattern 'T'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 3 or (row == 0 and column > 0 and column < 6)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise28():
    # Conditional Statements and Loops - Ćwiczenie 28
    # Write a Python program to print the alphabet pattern 'U'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise29():
    # Conditional Statements and Loops - Ćwiczenie 29
    # Write a Python program to print the alphabet pattern 'X'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and (row > 4 or row < 2)) or
                    row == column and column > 0 and column < 6 or
                    (column == 2 and row == 4) or
                    (column == 4 and row == 2)):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

def exercise30():
    # Conditional Statements and Loops - Ćwiczenie 30
    # Write a Python program to print the alphabet pattern 'Z'.
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row + column == 6):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "

        result_str = result_str + "\n"

    print(result_str)
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
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
        '22': exercise22,
        '23': exercise23,
        '24': exercise24,
        '25': exercise25,
        '26': exercise26,
        '27': exercise27,
        '28': exercise28,
        '29': exercise29,
        '30': exercise30,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 11 do 30), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '88' wczyta ćwiczenie 88). Wpisz 'wyjdź' aby wyjść z programu: ")
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