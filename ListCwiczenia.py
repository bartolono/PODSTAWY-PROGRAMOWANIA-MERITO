def exercise81():
    # List - Ćwiczenie 81
    # Write a Python program to extract a given number of randomly selected elements from a given list.
    import random

    def select_random_elements(input_list, num_elements):
        if num_elements > len(input_list):
            raise ValueError("Number of elements to select cannot exceed the length of the list")

        random_elements = random.sample(input_list, num_elements)
        return random_elements

    original_list = [1, 1, 2, 3, 4, 4, 5, 1]
    num_selected = 3

    try:
        selected_elements = select_random_elements(original_list, num_selected)
        print("Original list:")
        print(original_list)
        print(f"Selected {num_selected} random numbers of the above list:")
        print(selected_elements)
    except ValueError as e:
        print(e)
    print("")
    return main()

def exercise82():
    # List - Ćwiczenie 82
    # Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
    from itertools import combinations

    def generate_combinations(input_list, r):
        comb = combinations(input_list, r)
        return list(comb)

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = 2

    combinations_list = generate_combinations(original_list, r)

    print("Original list:", original_list)
    print(f"Combinations of {r} distinct objects:")
    for combination in combinations_list:
        print(combination)
    print("")
    return main()

def exercise83():
    # List - Ćwiczenie 83
    # Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
    def round_and_multiply_sum(input_list):
        rounded_list = [round(num) for num in input_list]
        rounded_sum = sum(rounded_list)
        result = rounded_sum * len(input_list)
        return result

    original_list = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

    result = round_and_multiply_sum(original_list)

    print("Original list:", original_list)
    print("Result:", result)
    print("")
    return main()

def exercise84():
    # List - Ćwiczenie 84
    # Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the numbers by 5.
    # Print the unique numbers in ascending order separated by space.
    def process_numbers(input_list):
        rounded_list = [round(num) for num in input_list]
        min_value = min(rounded_list)
        max_value = max(rounded_list)
        multiplied_list = [num * 5 for num in rounded_list]
        unique_numbers = sorted(set(multiplied_list))
        return min_value, max_value, unique_numbers

    original_list = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

    min_value, max_value, unique_numbers = process_numbers(original_list)

    print("Minimum value:", min_value)
    print("Maximum value:", max_value)

    print("Result:")
    print(" ".join(map(str, unique_numbers)))
    print("")
    return main()

def exercise85():
    # List - Ćwiczenie 85
    # Write a Python program to create a multidimensional list (lists of lists) with zeros.
    def create_multidimensional_list(rows, cols):
        multidimensional_list = [[0] * cols for _ in range(rows)]
        return multidimensional_list

    rows = 3
    cols = 2

    multidimensional_list = create_multidimensional_list(rows, cols)

    print("Multidimensional list:", multidimensional_list)
    print("")
    return main()

def exercise86():
    # List - Ćwiczenie 86
    # Write a Python program to create a 3X3 grid with numbers.
    def create_3x3_grid():
        grid = [[j for j in range(1, 4)] for _ in range(3)]
        return grid

    grid = create_3x3_grid()

    print("3X3 grid with numbers:")
    for row in grid:
        print(row)
    print("")
    return main()

def exercise87():
    # List - Ćwiczenie 87
    # Write a Python program to read a matrix from the console and print the sum for each column.
    # As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
    def read_matrix(rows, cols):
        matrix = []
        print("Input elements row by row separated by space:")

        for _ in range(rows):
            row = input().strip().split()
            row = [int(x) for x in row]
            if len(row) != cols:
                raise ValueError("Number of elements in each row must match the number of columns")
            matrix.append(row)

        return matrix

    def calculate_column_sums(matrix):
        cols = len(matrix[0])
        sums = [0] * cols
        for row in matrix:
            for j, num in enumerate(row):
                sums[j] += num
        return sums

    try:
        rows = int(input("Input rows: "))
        cols = int(input("Input columns: "))

        matrix = read_matrix(rows, cols)

        column_sums = calculate_column_sums(matrix)

        print("Sum for each column:")
        for sum in column_sums:
            print(sum, end=" ")

    except ValueError as e:
        print(e)
    print("")
    print("")
    return main()

def exercise88():
    # List - Ćwiczenie 88
    # Write a Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal.
    # Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
    def read_square_matrix(size):
        matrix = []
        print("Input elements row by row separated by space:")

        for _ in range(size):
            row = input().strip().split()
            row = [int(x) for x in row]
            if len(row) != size:
                raise ValueError("Number of elements in each row must match the size of the matrix")
            matrix.append(row)

        return matrix

    def calculate_primary_diagonal_sum(matrix):
        size = len(matrix)
        diagonal_sum = 0
        for i in range(size):
            diagonal_sum += matrix[i][i]
        return diagonal_sum

    try:
        size = int(input("Input the size of the matrix: "))

        matrix = read_square_matrix(size)

        diagonal_sum = calculate_primary_diagonal_sum(matrix)

        print("Sum of matrix primary diagonal:")
        print(diagonal_sum)

    except ValueError as e:
        print(e)
    print("")
    return main()

def exercise89():
    # List - Ćwiczenie 89
    # Write a Python program to Zip two given lists of lists.
    def zip_lists_of_lists(list1, list2):
        zipped_list = [x + y for x, y in zip(list1, list2)]
        return zipped_list

    list1 = [[1, 3], [5, 7], [9, 11]]
    list2 = [[2, 4], [6, 8], [10, 12, 14]]

    zipped_list = zip_lists_of_lists(list1, list2)

    print("Original list: ")
    print(list1)
    print(list2)
    print("Zipped list:")
    for sublist in zipped_list:
        print(sublist)
    print("")
    return main()

def exercise90():
    # List - Ćwiczenie 90
    # Write a Python program to count the number of lists in a given list of lists.
    def count_lists_in_list_of_lists(list_of_lists):
        count = 0
        for sublist in list_of_lists:
            if isinstance(sublist, list):
                count += 1
        return count

    list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

    count1 = count_lists_in_list_of_lists(list1)
    count2 = count_lists_in_list_of_lists(list2)

    print("Original list:")
    print(list1)
    print("Number of lists in said list of lists:")
    print(count1)

    print("Original list:")
    print(list2)
    print("Number of lists in said list of lists:")
    print(count2)
    print("")
    return main()

def exercise91():
    # List - Ćwiczenie 91
    # Write a Python program to find a list with maximum and minimum lengths.
    def find_max_min_lengths(input_list):
        max_length = float('-inf')
        min_length = float('inf')
        max_length_list = None
        min_length_list = None

        for sublist in input_list:
            length = len(sublist)
            if length > max_length:
                max_length = length
                max_length_list = sublist
            if length < min_length:
                min_length = length
                min_length_list = sublist

        return (max_length, max_length_list), (min_length, min_length_list)

    original_lists = [[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]],
                      [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]],
                      [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]]

    for i, lst in enumerate(original_lists):
        max_length, min_length = find_max_min_lengths(lst)
        print("Original list:")
        print(lst)
        print("List with maximum length of lists:")
        print(max_length)
        print("List with minimum length of lists:")
        print(min_length)
    print("")
    return main()

def exercise92():
    # List - Ćwiczenie 92
    # Write a Python program to check if a nested list is a subset of another nested list.
    def checkSubset(input_list1, input_list2):
        return all(map(input_list1.__contains__, input_list2))

    original_lists = [([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]),
                      ([[[1, 2], [2, 3]], [[3, 4], [5, 6]]], [[[3, 4], [5, 6]]]),
                      ([[[1, 2], [2, 3]], [[3, 4], [5, 7]]], [[[3, 4], [5, 6]]])]

    for lists_pair in original_lists:
        list1, list2 = lists_pair
        print("Original list:")
        print(list1)
        print(list2)
        print("If one of the said list is a subset of another:")
        print(checkSubset(list1, list2))
    print("")
    return main()

def exercise93():
    # List - Ćwiczenie 93
    # Write a Python program to count the number of sublists that contain a particular element.
    def count_element_in_sublists(input_list, element):
        count = 0
        for sublist in range(len(input_list)):
            if element in input_list[sublist]:
                count += 1
        return count

    list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]

    print("Original list: ")
    print(list1)
    print("Count 1 in sublists: ")
    print(count_element_in_sublists(list1, 1))
    print("Count 7 in sublists: ")
    print(count_element_in_sublists(list1, 7))

    list1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

    print("Original list: ")
    print(list1)
    print("Count 'A' in sublists: ")
    print(count_element_in_sublists(list1, 'A'))
    print("Count 'E' in sublists: ")
    print(count_element_in_sublists(list1, 'E'))
    print("")
    return main()

def exercise94():
    # List - Ćwiczenie 94
    # Write a Python program to count the number of unique sublists within a given list.
    def count_unique_sublists(input_list):
        unique_sublists = {}
        for sublist in input_list:
            sublist_tuple = tuple(sublist)
            unique_sublists[sublist_tuple] = unique_sublists.get(sublist_tuple, 0) + 1
        return unique_sublists

    original_lists = [([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]),
                      ([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])]

    for lst in original_lists:
        print("Original list:")
        print(lst)
        print("Number of unique lists of the said list:")
        print(count_unique_sublists(lst))
    print("")
    return main()

def exercise95():
    # List - Ćwiczenie 95
    # Write a Python program to sort each sublist of strings in a given list of lists.
    def sort_sublists(input_list):
        def custom_sort(sublist):
            return (len(sublist), sublist)

        sorted_list = sorted(input_list, key=custom_sort)
        return sorted_list

    original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

    sorted_list = sort_sublists(original_list)

    print("Original list:")
    print(original_list)
    print("Sort the list of lists by length and value:")
    print(sorted_list)
    print("")
    return main()

def exercise96():
    # List - Ćwiczenie 96
    # Write a Python program to sort a given list of lists by length and value.
    def sort_list_of_lists(input_list):
        def custom_sort(sublist):
            return (len(sublist), sublist)

        sorted_list = sorted(input_list, key=custom_sort)
        return sorted_list

    original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

    sorted_list = sort_list_of_lists(original_list)

    print("Original list:")
    print(original_list)
    print("Sort the list of lists by length and value:")
    print(sorted_list)
    print("")
    return main()

def exercise97():
    # List - Ćwiczenie 97
    # Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
    def remove_sublists_outside_range(input_list, start, end):
        filtered_list = [sublist for sublist in input_list if (min(sublist) >= start and max(sublist) <= end)]
        return filtered_list

    original_list = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]

    start_range = 13
    end_range = 17

    filtered_list = remove_sublists_outside_range(original_list, start_range, end_range)

    print("Original list:")
    print(original_list)
    print("After removing sublists from a given list of lists, which contains an element outside the given range:")
    print(filtered_list)
    print("")
    return main()

def exercise98():
    # List - Ćwiczenie 98
    # Write a Python program to scramble the letters of a string in a given list.
    import random

    def scramble_string(string):
        chars = list(string)
        random.shuffle(chars)
        scrambled_string = ''.join(chars)
        return scrambled_string

    original_list = ['Python', 'list', 'exercises', 'practice', 'solution']

    scrambled_list = [scramble_string(word) for word in original_list]

    print("Original list:")
    print(original_list)
    print("After scrambling the letters of the strings of the said list:")
    print(scrambled_list)
    print("")
    return main()

def exercise99():
    # List - Ćwiczenie 99
    # Write a Python program to find the maximum and minimum values in a given heterogeneous list.
    def find_max_min_heterogeneous(input_list):
        numeric_values = [x for x in input_list if isinstance(x, (int, float))]
        max_value = max(numeric_values)
        min_value = min(numeric_values)
        return max_value, min_value

    original_list = ['Python', 3, 2, 4, 5, 'version']

    max_value, min_value = find_max_min_heterogeneous(original_list)

    print("Original list:")
    print(original_list)
    print("Maximum and Minimum values in the said list:")
    print((max_value, min_value))
    print("")
    return main()

def exercise100():
    # List - Ćwiczenie 100
    # Write a Python program to extract common index elements from more than one given list.
    def common_index_elements(*lists):
        common_elements = []
        for i in range(len(lists[0])):
            if all(lists[j][i] == lists[0][i] for j in range(1, len(lists))):
                common_elements.append(lists[0][i])
        return common_elements

    list1 = [1, 1, 3, 4, 5, 6, 7]
    list2 = [0, 1, 2, 3, 4, 5, 7]
    list3 = [0, 1, 2, 3, 4, 5, 7]

    common_elements = common_index_elements(list1, list2, list3)

    print("Original lists:")
    print(list1)
    print(list2)
    print(list3)
    print("Common index elements of the said lists:")
    print(common_elements)
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
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
        '100': exercise100,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 81 do 100), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '88' wczyta ćwiczenie 88). Wpisz 'wyjdź' aby wyjść z programu: ")
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