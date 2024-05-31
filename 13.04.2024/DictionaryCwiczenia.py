def exercise61():
    # Dictionary - Ćwiczenie 61
    # Write a Python program to count the frequency of a dictionary.
    from collections import Counter

    original_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

    frequency_dict = Counter(original_dict.values())

    print("Original Dictionary:")
    print(original_dict)
    print("Count the frequency of the said dictionary:")
    print(frequency_dict)
    print("")
    return main()

def exercise62():
    # Dictionary - Ćwiczenie 62
    # Write a Python program to extract values from a given dictionary and create a list of lists from those values.
    original_dict = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
                     {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
                     {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
                     {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
                     {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

    list_of_lists = [[student['student_id'], student['name'], student['class']] for student in original_dict]

    print("Original Dictionary:")
    print(original_dict)
    print("Extract values from the dictionary and create a list of lists using those values:")
    print(list_of_lists)

    list_of_lists_alternative_1 = [[student['student_id'], student['name']] for student in original_dict]
    list_of_lists_alternative_2 = [[student['name'], student['class']] for student in original_dict]

    print(list_of_lists_alternative_1)
    print(list_of_lists_alternative_2)
    print("")
    return main()

def exercise63():
    # Dictionary - Ćwiczenie 63
    # Write a Python program to convert a given list of lists to a dictionary.
    original_list = [[1, 'Jean Castro', 'V'],
                     [2, 'Lula Powell', 'V'],
                     [3, 'Brian Howell', 'VI'],
                     [4, 'Lynne Foster', 'VI'],
                     [5, 'Zachary Simon', 'VII']]

    result_dict = {sublist[0]: sublist[1:] for sublist in original_list}

    print("Original list of lists:")
    print(original_list)
    print("Convert the said list of lists to a dictionary:")
    print(result_dict)
    print("")
    return main()

def exercise64():
    # Dictionary - Ćwiczenie 64
    # Write a Python program that creates key-value list pairings within a dictionary.
    original_dict = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'],
                     5: ['Zachary Simon']}

    key_value_pairings = [dict((key, value[0]) for key, value in original_dict.items())]

    print("Original dictionary:")
    print(original_dict)
    print("A key-value list pairings of the said dictionary:")
    print(key_value_pairings)
    print("")
    return main()

def exercise65():
    # Dictionary - Ćwiczenie 65
    # Write a Python program to get the total length of all values in a given dictionary with string values.
    original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

    total_length = sum(len(value) for value in original_dict.values())

    print("Original dictionary:")
    print(original_dict)
    print("Total length of all values of the said dictionary with string values:")
    print(total_length)
    print("")
    return main()

def exercise66():
    # Dictionary - Ćwiczenie 66
    # Write a Python program to check if a specific key and a value exist in a dictionary.
    def test(dictt, key, value):
        if any(sub[key] == value for sub in dictt):
            return True
        return False

    original_list = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
                     {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
                     {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
                     {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
                     {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

    print("Original dictionary:")
    print(original_list)
    print("Check if a specific Key and a value exist in the said dictionary:")
    print(test(original_list, 'student_id', 1))
    print(test(original_list, 'name', 'Brian Howell'))
    print(test(original_list, 'class', 'VII'))
    print(test(original_list, 'class', 'I'))
    print(test(original_list, 'name', 'Brian Howelll'))
    print(test(original_list, 'student_id', 11))
    print("")
    return main()

def exercise67():
    # Dictionary - Ćwiczenie 67
    # Write a Python program to invert a given dictionary with non-unique hashable values.
    original_dict = {'Ora Mckinney': 8, 'Mathew Gilbert': 8,
                     'Theodore Holland': 7, 'Mae Fleming': 7, 'Ivan Little': 7}

    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict.setdefault(value, []).append(key)

    print("Inverted dictionary:")
    print(inverted_dict)
    print("")
    return main()

def exercise68():
    # Dictionary - Ćwiczenie 68
    # Write a Python program to combine two or more dictionaries, creating a list of values for each key.
    dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
    dict2 = {'x': 300, 'y': 'Red', 'z': 600}

    combined_dict = {}

    def merge_dicts(dicts):
        result = {}
        for d in dicts:
            for key, value in d.items():
                result.setdefault(key, []).append(value)
        return result

    combined_dict = merge_dicts([dict1, dict2])

    print("Original dictionaries:")
    print(dict1)
    print(dict2)
    print("Combined dictionaries, creating a list of values for each key:")
    print(combined_dict)
    print("")
    return main()

def exercise69():
    # Dictionary - Ćwiczenie 69
    # Write a Python program to group the elements of a given list based on the given function.
    from collections import defaultdict
    from math import floor

    def test(lst, fn):
        d = defaultdict(list)

        for el in lst:
            key = fn(el)

            d[key].append(el)

        return dict(d)

    original_list1 = [7, 23, 3.2, 3.3, 8.4]

    print("Original list & function:")
    print(original_list1, " Function name: floor:")
    print("Group the elements of the said list based on the given function:")
    print(test(original_list1, floor))

    original_list2 = ['Red', 'Green', 'Black', 'White', 'Pink']

    print("Original list & function:")
    print(original_list2, " Function name: len:")
    print("Group the elements of the said list based on the given function:")
    print(test(original_list2, len))
    print("")
    return main()

def exercise70():
    # Dictionary - Ćwiczenie 70
    # Write a Python program to map the values of a given list to a dictionary using a function,
    # where the key-value pairs consist of the original value as the key and the result of the function as the value.
    def square(x):
        return x ** 2

    given_list = [1, 2, 3, 4]

    result_dict = {x: square(x) for x in given_list}

    print("Result dictionary:")
    print(result_dict)
    print("")
    return main()

def exercise71():
    # Dictionary - Ćwiczenie 71
    # Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
    def retrieve_value(data, selectors):
        for selector in selectors:
            if isinstance(data, dict):
                data = data.get(selector)
            elif isinstance(data, list) and len(data) > selector:
                data = data[selector]
            else:
                return None
        return data

    sample_dict = {'first': {'nested': {'name': 'Russell'}}, 'second': [1, 2, 3]}

    selector_list1 = ['first', 'nested', 'name']
    selector_list2 = ['second', 1]

    value1 = retrieve_value(sample_dict, selector_list1)
    value2 = retrieve_value(sample_dict, selector_list2)

    print("Value of the nested key:")
    print(value1)
    print(value2)
    print("")
    return main()

def exercise72():
    # Dictionary - Ćwiczenie 72
    # Write a Python program to invert a dictionary with unique hashable values.
    original_dict = {'Theodore': 10, 'Mathew': 11, 'Roxanne': 9}

    inverted_dict = {value: key for key, value in original_dict.items()}

    print("Inverted dictionary:")
    print(inverted_dict)
    print("")
    return main()

def exercise73():
    # Dictionary - Ćwiczenie 73
    # Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
    original_list = [
        {'name': 'Theodore', 'age': 18},
        {'name': 'Mathew', 'age': 22},
        {'name': 'Roxanne', 'age': 20},
        {'name': 'David', 'age': 18}
    ]

    specified_key = 'age'

    values_list = [d[specified_key] for d in original_list]

    print("Original list of dictionaries:")
    print(original_list)
    print("Convert a list of dictionaries into a list of values corresponding to the specified key:")
    print(values_list)
    print("")
    return main()

def exercise74():
    # Dictionary - Ćwiczenie 74
    # Write a Python program to create a dictionary with the same keys as the given dictionary
    # and values generated by running the given function for each value.
    original_dict = {
        'Theodore': {'user': 'Theodore', 'age': 45},
        'Roxanne': {'user': 'Roxanne', 'age': 15},
        'Mathew': {'user': 'Mathew', 'age': 21}
    }

    def get_age(data):
        return data['age']

    result_dict = {key: get_age(value) for key, value in original_dict.items()}

    print("Original dictionary elements:")
    print(original_dict)
    print("Dictionary with the same keys:")
    print(result_dict)
    print("")
    return main()

def exercise75():
    # Dictionary - Ćwiczenie 75
    # Write a Python program to find all keys in a dictionary that have the given value.
    original_dict = {
        'Theodore': 19,
        'Roxanne': 20,
        'Mathew': 21,
        'Betty': 20
    }

    specified_value = 20

    keys_with_value = [key for key, value in original_dict.items() if value == specified_value]

    print("Original dictionary elements:")
    print(original_dict)
    print("Find all keys in the said dictionary that have the specified value:")
    print(keys_with_value)
    print("")
    return main()

def exercise76():
    # Dictionary - Ćwiczenie 76
    # Write a Python program to combine two lists into a dictionary.
    # The elements of the first one serve as keys and the elements of the second one serve as values.
    # Each item in the first list must be unique and hashable.
    keys_list = ['a', 'b', 'c', 'd', 'e', 'f']
    values_list = [1, 2, 3, 4, 5]

    combined_dict = dict(zip(keys_list, values_list))

    print("Original lists:")
    print(keys_list)
    print(values_list)
    print("Combine the values of the said two lists into a dictionary:")
    print(combined_dict)
    print("")
    return main()

def exercise77():
    # Dictionary - Ćwiczenie 77
    # Write a Python program to transform a dictionary into a list of tuples.
    original_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

    list_of_tuples = list(original_dict.items())

    print("Original Dictionary:")
    print(original_dict)
    print("Convert the said dictionary to a list of tuples:")
    print(list_of_tuples)
    print("")
    return main()

def exercise78():
    # Dictionary - Ćwiczenie 78
    # Write a Python program to create a flat list of all the keys in a flat dictionary.
    original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

    keys_list = list(original_dict.keys())

    print("Original dictionary elements:")
    print(original_dict)
    print("Create a flat list of all the keys of the said flat dictionary:")
    print(keys_list)
    print("")
    return main()

def exercise79():
    # Dictionary - Ćwiczenie 79
    # Write a Python program to create a flat list of all the values in a flat dictionary.
    original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

    values_list = list(original_dict.values())

    print("Original dictionary elements:")
    print(original_dict)
    print("Create a flat list of all the values of the said flat dictionary:")
    print(values_list)
    print("")
    return main()

def exercise80():
    # Dictionary - Ćwiczenie 80
    # Write a Python program to find the key of the maximum value in a dictionary.
    original_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

    max_key = max(original_dict, key=original_dict.get)
    min_key = min(original_dict, key=original_dict.get)

    print("Original dictionary elements:")
    print(original_dict)
    print("Finds the key of the maximum and minimum value of the said dictionary:")
    print((max_key, min_key))
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
        '61': exercise61,
        '62': exercise62,
        '63': exercise63,
        '64': exercise64,
        '65': exercise65,
        '66': exercise66,
        '67': exercise67,
        '68': exercise68,
        '69': exercise69,
        '70': exercise70,
        '71': exercise71,
        '72': exercise72,
        '73': exercise73,
        '74': exercise74,
        '75': exercise75,
        '76': exercise76,
        '77': exercise77,
        '78': exercise78,
        '79': exercise79,
        '80': exercise80,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 61 do 80), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '88' wczyta ćwiczenie 88). Wpisz 'wyjdź' aby wyjść z programu: ")
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