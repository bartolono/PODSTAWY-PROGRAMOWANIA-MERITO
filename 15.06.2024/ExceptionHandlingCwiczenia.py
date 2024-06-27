def exercise1():
    # Exception Handling - Ćwiczenie 1
    # Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
    def safe_division(num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "Błąd: Dzielenie przez zero jest niedozwolone!"
        else:
            return f"Wynik dzielenia liczby {num1} z {num2} wynosi {result}."

    num1 = 100
    num2 = 0

    print(safe_division(num1, num2))
    print("")
    return main()

def exercise2():
    # Exception Handling - Ćwiczenie 2
    # Write a Python program that prompts the user to input an integer and raises a ValueError exception
    # if the input is not a valid integer.
    def get_integer_input(prompt="Wpisz liczbę całkowitą: "):
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            raise ValueError("Nieprawidłowa wartość: Wpisz poprawną liczbę całkowitą.")

    try:
        user_input = get_integer_input()
        print(f"Wpisałeś liczbę całkowitą: {user_input}")
    except ValueError as e:
        print(e)
    print("")
    return main()

def exercise3():
    # Exception Handling - Ćwiczenie 3
    # Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return f"Błąd: Plik '{file_path}' nie został znaleziony."

    file_path = "tenpliknieistnieje.txt"
    file_content = read_file(file_path)
    print(file_content)
    print("")
    return main()

def exercise4():
    # Exception Handling - Ćwiczenie 4
    # Write a Python program that prompts the user to input two numbers and raises a
    # TypeError exception if the inputs are not numerical.
    def get_numerical_input(prompt):
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            raise TypeError("Nieprawidłowa wartość: Wpisz fatkyczną liczbę (nie literę/znak).")

    try:
        num1 = get_numerical_input("Wpisz pierwszą liczbę: ")
        num2 = get_numerical_input("Wpisz drugą liczbę: ")
        print(f"Pierwsza liczba to: {num1}")
        print(f"Druga liczba to: {num2}")
    except TypeError as e:
        print(e)
    print("")
    return main()

def exercise5():
    # Exception Handling - Ćwiczenie 5
    # Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
    def read_file(file_path):
        try:
            with open(file_path, 'w') as file:
                content = file.read()
                return content
        except PermissionError:
            return f"Błąd: Odmowa uprawnień do otwarcia pliku '{file_path}'."

    file_path = "test.txt"  # Plik utworzony z ustawieniem "Tylko do odczytu"
    file_content = read_file(file_path)
    print(file_content)
    print("")
    return main()

def exercise6():
    # Exception Handling - Ćwiczenie 6
    # Write a Python program that executes an operation on a list and handles an IndexError exception
    # if the index is out of range.
    def get_list_element(lst, index):
        try:
            element = lst[index]
            return element
        except IndexError:
            return f"Błąd: Indeks {index} jest poza zakresem listy."

    my_list = [1, 2, 3, 4, 5]
    index_to_access = 10

    result = get_list_element(my_list, index_to_access)
    print(result)
    print("")
    return main()

def exercise7():
    # Exception Handling - Ćwiczenie 7
    # Write a Python program that prompts the user to input a number and handles a
    # KeyboardInterrupt exception if the user cancels the input.
    def get_user_input(prompt="Wpisz cyfrę: "):
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("Nieprawidłowa wartość: Wpisz fatkyczną liczbę (nie literę/znak).")
        except KeyboardInterrupt:
            print("\nDane wejściowe zostało anulowane przez użytkownika.")
            return None

    try:
        number = get_user_input()
        if number is not None:
            print(f"Wpisałeś cyfrę: {number}")
        else:
            print("Żadna cyfra nie została wpisana.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    print("")
    return main()

def exercise8():
    # Exception Handling - Ćwiczenie 8
    # Write a Python program that executes division and handles an ArithmeticError exception
    # if there is an arithmetic error.
    def safe_division(num1, num2):
        try:
            result = num1 / num2
            return f"Wynik dzielenia liczby {num1} z {num2} wynosi {result}."
        except ArithmeticError as e:
            return f"Błąd: Wystąpił błąd arytmetyczny - {e}."

    num1 = 100
    num2 = 0

    result = safe_division(num1, num2)
    print(result)
    print("")
    return main()

def exercise9():
    # Exception Handling - Ćwiczenie 9
    # Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
    def read_file(file_path):
        try:
            with open(file_path, 'r', encoding='ascii') as file:
                content = file.read()
                return content
        except UnicodeDecodeError:
            return f"Błąd: Wystąpił problem podczas odczytu pliku pod adresem '{file_path}'."

    file_path = "test.txt"
    file_content = read_file(file_path)
    print(file_content)
    print("")
    return main()

def exercise10():
    # Exception Handling - Ćwiczenie 10
    # Write a Python program that executes a list operation and handles an
    # AttributeError exception if the attribute does not exist.
    def perform_list_operation(lst):
        try:
            length = lst.length
            return f"Długość listy wynosi: {length}"
        except AttributeError as e:
            return f"Błąd: AttributeError - {e}"

    my_list = [1, 2, 3, 4, 5]

    result = perform_list_operation(my_list)
    print(result)
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
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 1 do 10), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '5' wczyta ćwiczenie 5). Wpisz 'wyjdź' aby wyjść z programu: ")
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