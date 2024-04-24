def exercise80():
    # String - Ćwiczenie 80
    # Write a Python program to count the number of substrings with the same first and last characters in a given string.
    def count_substrings_with_same_first_and_last_char(s):
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j]:
                    count += 1
        return count

    input_string = input("Enter a string: ")
    result = count_substrings_with_same_first_and_last_char(input_string)
    print("Number of substrings with the same first and last characters:", result)
    print("")
    return main()

def exercise81():
    # String - Ćwiczenie 81
    # Write a Python program to determine the index of a given string at which a certain substring starts.
    # If the substring is not found in the given string return 'Not found'.
    def find_substring_index(main_string, substring):
        index = main_string.find(substring)
        if index != -1:
            return index
        else:
            return 'Not found'

    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to find: ")

    result = find_substring_index(main_string, substring)
    print("Index of the substring:", result)
    print("")
    return main()

def exercise82():
    # String - Ćwiczenie 82
    # Write a Python program to wrap a given string into a paragraph with a given width.
    def wrap_into_paragraph(string, width):
        wrapped_string = ""
        start = 0
        while start < len(string):
            end = min(start + width, len(string))
            wrapped_string += string[start:end] + "\n"
            start = end
        return wrapped_string

    input_string = input("Input a string: ")
    width = int(input("Input the width of the paragraph: "))
    result = wrap_into_paragraph(input_string, width)
    print("Result:")
    print(result)
    return main()

def exercise83():
    # String - Ćwiczenie 83
    # Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
    def print_integer_formats(num):
        decimal = str(num)
        octal = oct(num)[2:]
        hexadecimal = hex(num)[2:].upper()
        binary = bin(num)[2:]
        print("Decimal Octal Hexadecimal (capitalized) Binary")
        print(f"{decimal} {octal} {hexadecimal} {binary}")

    input_integer = int(input("Input an integer: "))
    print_integer_formats(input_integer)
    print("")
    return main()

def exercise84():
    # String - Ćwiczenie 84
    # Write a Python program to swap cases in a given string.
    def swap_case(string):
        return string.swapcase()

    input_string1 = "Python Exercises"
    input_string2 = "Java"
    input_string3 = "NumPy"

    result1 = swap_case(input_string1)
    result2 = swap_case(input_string2)
    result3 = swap_case(input_string3)

    print(result1)
    print(result2)
    print(result3)
    print("")
    return main()

def exercise85():
    # String - Ćwiczenie 85
    # Write a Python program to convert a given Bytearray to a Hexadecimal string.
    def convert_bytearray_to_hex(byte_array):
        return ''.join(format(byte, '02x') for byte in byte_array)

    byte_array = bytearray([111, 12, 45, 67, 109])
    print("Original Bytearray:")
    print(list(byte_array))
    hex_string = convert_bytearray_to_hex(byte_array)
    print("Hexadecimal string:")
    print(hex_string)
    print("")
    return main()

def exercise86():
    # String - Ćwiczenie 86
    # Write a Python program to delete all occurrences of a specified character in a given string.
    def delete_occurrences(string, char):
        return string.replace(char, '')

    original_string = "Delete all occurrences of a specified character in a given string"
    specified_char = 'a'

    print("Original string:")
    print(original_string)

    modified_string = delete_occurrences(original_string, specified_char)

    print("Modified string:")
    print(modified_string)
    print("")
    return main()

def exercise87():
    # String - Ćwiczenie 87
    # Write a Python program to find the common values that appear in two given strings.
    def find_common_values(string1, string2):
        common_values = ''
        min_len = min(len(string1), len(string2))

        for i in range(min_len):
            if string1[i] == string2[i]:
                common_values += string1[i]
            else:
                break

        return common_values

    string1 = "Python3"
    string2 = "Python2.7"

    print("Original strings:")
    print(string1)
    print(string2)

    intersection = find_common_values(string1, string2)

    print("Intersection of two said Strings:")
    print(intersection)
    print("")
    return main()

def exercise88():
    # String - Ćwiczenie 88
    # Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
    def check_valid_string(string, min_length):
        has_upper = any(c.isupper() for c in string)
        has_lower = any(c.islower() for c in string)
        has_digit = any(c.isdigit() for c in string)
        meets_length = len(string) >= min_length

        if has_upper and has_lower and has_digit and meets_length:
            return ['Valid string.']
        else:
            return ['Invalid string.']

    input_string = input("Input the string: ")
    min_length = 8  # Tutaj miejsce na ustawienie minimalnej długości

    result = check_valid_string(input_string, min_length)
    print(result)
    print("")
    return main()

def exercise89():
    # String - Ćwiczenie 89
    # Write a Python program to remove unwanted characters from a given string.
    def remove_unwanted_characters(string, unwanted_chars):
        return ''.join(char for char in string if char not in unwanted_chars)

    def exercise():
        test_cases = [
            "Pyth*^on Exercis^es",
            "A%^!B#*CD"
        ]
        for string in test_cases:
            print("Original String:", string)
            result = remove_unwanted_characters(string, unwanted_chars="*^!#%")
            print("After removing unwanted characters:")
            print(result)
            print()

    exercise()
    return main()

def exercise90():
    # String - Ćwiczenie 90
    # Write a Python program to remove duplicate words from a given string.
    def remove_duplicate_words(string):
        words = string.split()
        unique_words = list(dict.fromkeys(words))
        return ' '.join(unique_words)

    original_string = "Python Exercises Practice Solution Exercises"

    print("Original String:")
    print(original_string)

    result = remove_duplicate_words(original_string)

    print("After removing duplicate words from the said string:")
    print(result)
    print("")
    return main()

def exercise91():
    # String - Ćwiczenie 91
    # Write a Python program to convert a given heterogeneous list of scalars into a string.
    def convert_to_string(lst):
        return ','.join(str(item) for item in lst)

    original_list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

    print("Original list:")
    print(original_list)

    print("Convert the heterogeneous list of scalars into a string:")
    print(convert_to_string(original_list))
    print("")
    return main()

def exercise92():
    # String - Ćwiczenie 92
    # Write a Python program to find string similarity between two given strings.
    from difflib import SequenceMatcher

    def string_similarity(string1, string2):
        similarity = SequenceMatcher(None, string1, string2).ratio()
        return similarity

    test_cases = [
        ("Python Exercises", "Python Exercises"),
        ("Python Exercises", "Python Exercise"),
        ("Python Exercises", "Python Ex."),
        ("Python Exercises", "Python"),
        ("Java Exercises", "Python")
    ]

    for i, (string1, string2) in enumerate(test_cases, start=1):
        print(f"Original string {i}:")
        print(string1)
        print(string2)
        similarity = string_similarity(string1, string2)
        print("Similarity between two said strings:")
        print(similarity)
        print()
    return main()

def exercise93():
    # String - Ćwiczenie 93
    # Write a Python program to extract numbers from a given string.

    import re

    def extract_numbers(string):
        return [int(num) for num in re.findall(r'\d+', string)]

    original_string = "red 12 black 45 green"

    print("Original string:")
    print(original_string)

    print("Extract numbers from the said string:")
    print(extract_numbers(original_string))
    print("")
    return main()

def exercise94():
    # String - Ćwiczenie 94
    # Write a Python program to convert a hexadecimal color code to a
    # tuple of integers corresponding to its RGB components.

    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')  # Remove '#' if present
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)

    hex_color_codes = [
        "#ffa501",  # Orange
        "#FFFFFF",  # White
        "#000000",  # Black
        "#FF0000",  # Red
        "#000080",  # Navy
        "#C0C0C0"   # Silver
    ]

    for hex_code in hex_color_codes:
        print(hex_to_rgb(hex_code))
    print("")
    return main()

def exercise95():
    # String - Ćwiczenie 95
    # Write a Python program to convert the values of RGB components
    # to a hexadecimal color code.
    def rgb_to_hex(r, g, b):
        hex_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
        return hex_code

    rgb_components = [
        (255, 165, 1),   # Orange
        (255, 255, 255), # White
        (0, 0, 0),       # Black
        (0, 0, 128),     # Navy
        (192, 192, 192)  # Silver
    ]

    for r, g, b in rgb_components:
        print(rgb_to_hex(r, g, b))
    print("")
    return main()

def exercise96():
    # String - Ćwiczenie 96
    # Write a Python program to convert a given string to Camelcase.
    def to_camel_case(string):
        words = string.split('_')
        return ''.join(word.capitalize() for word in words)

    strings = [
        "javascript",
        "foo_bar",
        "FooBar",
        "foo.bar",
        "foo-bar",
        "foobar",
        "foo Bar"
    ]

    for string in strings:
        print(to_camel_case(string))
    print("")
    return main()

def exercise97():
    # String - Ćwiczenie 97
    # Write a Python program to convert a given string to Snake case.
    def to_snake_case(string):
        string = string.replace('-', '_').replace('.', '_').replace(' ', '_')
        return string.lower()

    strings = [
        "java_script",
        "foo_bar",
        "FooBar",
        "foo.bar",
        "foo-bar",
        "foobar",
        "foo Bar"
    ]

    for string in strings:
        print(to_snake_case(string))
    print("")
    return main()

def exercise98():
    # String - Ćwiczenie 98
    # Write a Python program to decapitalize the first letter of a given string.
    def decapitalize_first_letter(string):
        return string[:1].lower() + string[1:]

    strings = [
        "Java Script",
        "Python"
    ]

    for string in strings:
        print(decapitalize_first_letter(string))
    print("")
    return main()

def exercise99():
    # String - Ćwiczenie 99
    # Write a Python program to split a multi-line string into a list of lines.
    def split_multiline_string(string):
        return string.splitlines()

    original_string = """This
    is a
    multiline
    string."""

    print("Original string:")
    print(original_string)

    print("Split the said multiline string into a list of lines:")
    print(split_multiline_string(original_string))
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
        '80': exercise80,
        '81': exercise81,
        '82': exercise82,
        '83': exercise83,
        '84': exercise84,
        '85': exercise85,
        '86': exercise86,
        '87': exercise87,
        '88': exercise88,
        '89': exercise89,
        '90': exercise90,
        '91': exercise91,
        '92': exercise92,
        '93': exercise93,
        '94': exercise94,
        '95': exercise95,
        '96': exercise96,
        '97': exercise97,
        '98': exercise98,
        '99': exercise99,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 80 do 99), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '88' wczyta ćwiczenie 88). Wpisz 'wyjdź' aby wyjść z programu: ")
        if exercise_name == 'wyjdź':
            break

        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            result = exercise_function()
            print(result)
        else:
            print("Nie znaleziono ćwiczenia.")

if __name__ == "__main__":
    main()