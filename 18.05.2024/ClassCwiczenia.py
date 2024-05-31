def exercise1a():
    # Class, Basic exercises - Ćwiczenie 1
    # Write a Python program to import a built-in array module and display the namespace of the said module.
    import array
    for name in array.__dict__:
        print(name)
    print("")
    return main()

def exercise2a():
    # Class, Basic exercises - Ćwiczenie 2
    # Write a Python program to create a class and display the namespace of that class.
    class py_solution:
        def sub_sets(self, sset):
            return self.subsetsRecur([], sorted(sset))

        def subsetsRecur(self, current, sset):
            if sset:
                return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
            return [current]

    for name in py_solution.__dict__:
        print(name)
    print("")
    return main()

def exercise3a():
    # Class, Basic exercises - Ćwiczenie 3
    # Write a Python program to create an instance of a specified class and display the namespace of the said instance.
    class Student:
        def __init__(self, student_id, student_name, class_name):
            self.student_id = student_id
            self.student_name = student_name
            self.class_name = class_name

    student = Student('V12', 'Frank Gibson', 'V')
    print(student.__dict__)
    print("")
    return main()

def exercise4a():
    # Class, Basic exercises - Ćwiczenie 4
    # 'builtins' module provides direct access to all 'built-in' identifiers of Python.
    # Write a Python program that imports the abs() function using the builtins module,
    # displays the documentation of the abs() function and finds the absolute value of -155.
    import builtins
    help(builtins.abs)
    print(builtins.abs(-155))
    print("")
    return main()

def exercise5a():
    # Class, Basic exercises - Ćwiczenie 5
    # Define a Python function student(). Using function attributes display the names of all arguments.
    def student(student_id, student_name, student_class):
        return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'

    print(student('S122', 'Wilson Medina', 'VI'))
    print("")
    return main()

def exercise6a():
    # Class, Basic exercises - Ćwiczenie 6
    # Write a Python function student_data () that will print the ID of a student (student_id).
    # If the user passes an argument student_name or student_class the function will print the student name and class.
    def student_data(student_id, **kwargs):
        print(f'\nStudent ID: {student_id}')
        if 'student_name' in kwargs:
            print(f"Student Name: $ {kwargs['student_name']}")

        if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")

    student_data(student_id='SV12', student_name='Jean Garner')
    student_data(student_id='SV12', student_name='Jean Garner', student_class='V')
    print("")
    return main()

def exercise7a():
    # Class, Basic exercises - Ćwiczenie 7
    # Write a simple Python class named Student and display its type. Also,
    # display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
    class Student:
        pass

    print(type(Student))
    print(Student.__dict__.keys())
    print(Student.__module__)
    print("")
    return main()

def exercise8a():
    # Class, Basic exercises - Ćwiczenie 8
    # Write a Python program to create two empty classes, Student and Marks.
    # Now create some instances and check whether they are instances of the said classes or not.
    # Also, check whether the said classes are subclasses of the built-in object class or not.
    class Student:
        pass

    class Marks:
        pass

    student1 = Student()
    marks1 = Marks()
    print(isinstance(student1, Student))
    print(isinstance(marks1, Student))
    print(isinstance(marks1, Marks))
    print(isinstance(student1, Marks))
    print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
    print(issubclass(Student, object))
    print(issubclass(Marks, object))
    print("")
    return main()

def exercise9a():
    # Class, Basic exercises - Ćwiczenie 9
    # Write a Python class named Student with two attributes student_name, marks.
    # Modify the attribute values of the said class and print the original and modified values of the said attributes.
    class Student:
        student_name = 'Terrance Morales'
        marks = 93

    print(f"Student Name: {getattr(Student, 'student_name')}")
    print(f"Marks: {getattr(Student, 'marks')}")
    setattr(Student, 'student_name', 'Angel Brooks')
    setattr(Student, 'marks', 95)
    print(f"Student Name: {getattr(Student, 'student_name')}")
    print(f"Marks: {getattr(Student, 'marks')}")
    print("")
    return main()

def exercise10a():
    # Write a Python class named Student with two attributes student_id, student_name.
    # Add a new attribute student_class and display the entire attribute and the values of the class.
    # Now remove the student_name attribute and display the entire attribute with values.
    class Student:
        student_id = 'V10'
        student_name = 'Jacqueline Barnett'

    print("Original attributes and their values of the Student class:")
    for attr, value in Student.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')
    print("\nAfter adding the student_class, attributes and their values with the said class:")
    Student.student_class = 'V'
    for attr, value in Student.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')
    print("\nAfter removing the student_name, attributes and their values from the said class:")
    del Student.student_name
    # delattr(Student, 'student_name')
    for attr, value in Student.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')
    print("")
    return main()

def exercise11a():
    # Class, Basic exercises - Ćwiczenie 11a
    # Write a Python class named Student with two attributes: student_id, student_name.
    # Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
    class Student:
        student_id = 'V10'
        student_name = 'Jacqueline Barnett'

        def display():
            print(f'Student id: {Student.student_id}\nStudent Name: {Student.student_name}')

    print("Original attributes and their values of the Student class:")
    Student.display()
    print("")
    return main()

def exercise12a():
    # Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes.
    # Print all the attributes of the student1, student2 instances with their values in the given format.
    class Student:
        school = 'Forward Thinking'
        address = '2626/Z Overlook Drive, COLUMBUS'

    student1 = Student()
    student2 = Student()
    student1.student_id = "V12"
    student1.student_name = "Ernesto Mendez"
    student2.student_id = "V12"
    student2.marks_language = 85
    student2.marks_science = 93
    student2.marks_math = 95
    students = [student1, student2]
    for student in students:
        print('\n')
        for attr in student.__dict__:
            print(f'{attr} -> {getattr(student, attr)}')
    print("")
    return main()

def exercise1b():
    # Class, Basic application - Ćwiczenie 1
    # Write a Python class to convert an integer to a Roman numeral.
    class IntegerToRoman:
        def int_to_roman(self, num):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
            ]
            roman_num = ''
            i = 0
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num

    converter = IntegerToRoman()
    print(converter.int_to_roman(1))
    print(converter.int_to_roman(4000))
    print("")
    return main()

def exercise2b():
    # Class, Basic application - Ćwiczenie 2
    # Write a Python class to convert a Roman numeral to an integer.
    class RomanToInteger:
        def roman_to_int(self, s):
            roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            integer = 0
            for i in range(len(s)):
                if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                    integer += roman[s[i]] - 2 * roman[s[i - 1]]
                else:
                    integer += roman[s[i]]
            return integer

    print(RomanToInteger().roman_to_int('MMMCMLXXXVI'))
    print(RomanToInteger().roman_to_int('MMMM'))
    print(RomanToInteger().roman_to_int('C'))
    print("")
    return main()

def exercise3b():
    # Class, Basic application - Ćwiczenie 3
    # Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
    # These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
    class ParenthesesValidator:
        def is_valid(self, s):
            stack = []
            mapping = {")": "(", "}": "{", "]": "["}
            for char in s:
                if char in mapping:
                    top_element = stack.pop() if stack else '#'
                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)
            return not stack

    validator = ParenthesesValidator()
    print(validator.is_valid("(){}[]"))
    print(validator.is_valid("()[{)}"))
    print(validator.is_valid("()"))
    print("")
    return main()

def exercise4b():
    # Class, Basic application - Ćwiczenie 4
    # Write a Python class to get all possible unique subsets from a set of distinct integers.
    class UniqueSubsets:
        def subsets(self, nums):
            return self.backtrack([], sorted(nums))

        def backtrack(self, current, nums):
            if nums:
                return self.backtrack(current, nums[1:]) + self.backtrack(current + [nums[0]], nums[1:])
            return [current]

    print(UniqueSubsets().subsets([4, 5, 6]))
    print("")
    return main()

def exercise5b():
    # Class, Basic application - Ćwiczenie 5b
    # Write a Python class to find a pair of elements (indices of the two numbers)
    # from a given array whose sum equals a specific target number.
    class PairSum:
        def find_pair(self, nums, target):
            num_map = {}
            for i, num in enumerate(nums):
                if target - num in num_map:
                    return (num_map[target - num], i)
                num_map[num] = i

    print("index1=%d, index2=%d" % PairSum().find_pair([10, 20, 10, 40, 50, 60, 70], 50))
    # On website there is an error - the output should be [2, 3] not [3, 4]
    print("")
    return main()

def exercise6b():
    # Class, Basic application - Ćwiczenie 6
    # Write a Python class to find the three elements that sum to zero from a set of n real numbers.
    class ThreeSumZero:
        def three_sum(self, nums):
            nums.sort()
            result = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            return result

    print(ThreeSumZero().three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))
    print("")
    return main()

def exercise7b():
    # Class, Basic application - Ćwiczenie 7
    # Write a Python class to implement pow(x, n).
    class Power:
        def pow(self, x, n):
            if n == 0:
                return 1
            temp = self.pow(x, int(n / 2))
            if n % 2 == 0:
                return temp * temp
            else:
                if n > 0:
                    return x * temp * temp
                else:
                    return (temp * temp) / x

    print(Power().pow(2, -3))
    print(Power().pow(3, 5))
    print(Power().pow(100, 0))
    print("")
    return main()

def exercise8b():
    # Class, Basic application - Ćwiczenie 8
    # Write a Python class to reverse a string word by word.
    class ReverseWords:
        def reverse_words(self, s):
            return ' '.join(reversed(s.split()))

    print(ReverseWords().reverse_words("hello .py"))
    print("")
    return main()

def exercise9b():
    # Class, Basic application - Ćwiczenie 9
    # Write a Python class that has two methods: get_String and print_String ,
    # get_String accept a string from the user and print_String prints the string in upper case.
    class StringManipulation:
        def get_String(self):
            self.s = input("")

        def print_String(self):
            print(self.s.upper())

    s = StringManipulation()
    s.get_String()
    s.print_String()
    print("")
    return main()

def exercise10b():
    # Class, Basic application - Ćwiczenie 10b
    # Write a Python class named Rectangle constructed from length and width and a method that
    # will compute the area of a rectangle.
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    rect = Rectangle(12, 10)
    print(rect.area())
    print("")
    return main()

def exercise11b():
    # Class, Basic application - Ćwiczenie 11
    # Write a Python class named Circle constructed from a radius and two methods
    # that will compute the area and the perimeter of a circle.
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return self.radius ** 2 * 3.14

        def perimeter(self):
            return 2 * self.radius * 3.14

    circle = Circle(8)
    print(circle.area())
    print(circle.perimeter())
    print("")
    return main()

def exercise12b():
    # Class, Basic application - Ćwiczenie 12
    # Write a Python program to get the class name of an instance in Python.
    class MyClass:
        pass

    obj = MyClass()
    print(type(obj).__name__)
    print("")
    return main()

def exercise1c():
    # Class, Real-life problems - Ćwiczenie 1
    # Write a Python class Employee with attributes like emp_id, emp_name, emp_salary,
    # and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
    class Employee:
        def __init__(self, emp_id, emp_name, emp_salary, emp_department):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.emp_salary = emp_salary
            self.emp_department = emp_department

        def calculate_emp_salary(self, hours_worked):
            if hours_worked > 50:
                overtime = hours_worked - 50
                overtime_amount = overtime * (self.emp_salary / 50)
                return self.emp_salary + overtime_amount
            return self.emp_salary

        def assign_department(self, new_department):
            self.emp_department = new_department

        def print_employee_details(self):
            print(f"ID: {self.emp_id}")
            print(f"Name: {self.emp_name}")
            print(f"Salary: {self.emp_salary}")
            print(f"Department: {self.emp_department}")
            print("----------------------\n")

    employee1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
    employee2 = Employee("E7499", "JONES", 45000, "RESEARCH")
    employee3 = Employee("E7900", "MARTIN", 50000, "SALES")
    employee4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

    print("Original Employee Details:\n")
    employee1.print_employee_details()
    employee2.print_employee_details()
    employee3.print_employee_details()
    employee4.print_employee_details()

    employee1.assign_department("OPERATIONS")
    employee4.assign_department("SALES")

    employee2.emp_salary = employee2.calculate_emp_salary(52)
    employee4.emp_salary = employee4.calculate_emp_salary(60)

    print("Updated Employee Details:\n")
    employee1.print_employee_details()
    employee2.print_employee_details()
    employee3.print_employee_details()
    employee4.print_employee_details()
    return main()

def exercise2c():
    # Class, Real-life problems - Ćwiczenie 2
    # Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders,
    # and methods like add_item_to_menu, book_tables, and customer_order.
    class Restaurant:
        def __init__(self):
            self.menu_items = {}
            self.book_table = []
            self.customer_orders = []

        def add_item_to_menu(self, item, price):
            self.menu_items[item] = price

        def book_tables(self, table_number):
            self.book_table.append(table_number)

        def customer_order(self, table_number, order):
            order_details = {'table_number': table_number, 'order': order}
            self.customer_orders.append(order_details)

        def print_menu_items(self):
            for item, price in self.menu_items.items():
                print("{}: ${}".format(item, price))

        def print_table_reservations(self):
            for table in self.book_table:
                print("Table {}".format(table))

        def print_customer_orders(self):
            for order in self.customer_orders:
                print("Table {}: {}".format(order['table_number'], order['order']))

    restaurant = Restaurant()

    restaurant.add_item_to_menu("Cheeseburger", 9.99)
    restaurant.add_item_to_menu("Caesar Salad", 8)
    restaurant.add_item_to_menu("Grilled Salmon", 19.99)
    restaurant.add_item_to_menu("French Fries", 3.99)
    restaurant.add_item_to_menu("Fish & Chips:", 15)

    restaurant.book_tables(1)
    restaurant.book_tables(2)
    restaurant.book_tables(3)

    restaurant.customer_order(1, "Cheeseburger")
    restaurant.customer_order(1, "Grilled Salmon")
    restaurant.customer_order(2, "Fish & Chips")
    restaurant.customer_order(2, "Grilled Salmon")

    print("\nPopular dishes in the restaurant along with their prices:")
    restaurant.print_menu_items()
    print("\nTable reserved in the Restaurant:")
    restaurant.print_table_reservations()
    print("\nPrint customer orders:")
    restaurant.print_customer_orders()
    print("")
    return main()

def exercise3c():
    # Class, Real-life problems - Ćwiczenie 3
    # Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name,
    # and methods like deposit, withdraw, and check_balance.
    class BankAccount:
        def __init__(self, account_number, date_of_opening, balance, customer_name):
            self.account_number = account_number
            self.date_of_opening = date_of_opening
            self.balance = balance
            self.customer_name = customer_name

        def deposit(self, amount):
            self.balance += amount
            print(f"${amount} has been deposited in your account.")

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"${amount} has been withdrawn from your account.")

        def check_balance(self):
            print(f"Current balance is ${self.balance}.")

        def print_customer_details(self):
            print("Name:", self.customer_name)
            print("Account Number:", self.account_number)
            print("Date of opening:", self.date_of_opening)
            print(f"Balance: ${self.balance}\n")

    ac_no_1 = BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
    ac_no_2 = BankAccount(1234, "11-03-2011", 2000, "Astrid Rugile")
    ac_no_3 = BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
    ac_no_4 = BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
    ac_no_5 = BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

    print("Customer Details:")
    ac_no_1.print_customer_details()
    ac_no_2.print_customer_details()
    ac_no_3.print_customer_details()
    ac_no_4.print_customer_details()
    ac_no_5.print_customer_details()

    print("=============================")
    ac_no_4.print_customer_details()
    ac_no_4.deposit(1000)
    ac_no_4.check_balance()
    ac_no_4.withdraw(5000)
    ac_no_4.withdraw(3400)
    ac_no_4.check_balance()
    print("")
    return main()

def exercise4c():
    # Class, Real-life problems - Ćwiczenie 4
    # Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price,
    # and methods like add_item, update_item, and check_item_details.
    # Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary
    # containing the item_name, stock_count, and price.
    class Inventory:
        def __init__(self):
            self.inventory = {}

        def add_item(self, item_id, item_name, stock_count, price):
            self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

        def update_item(self, item_id, stock_count, price):
            if item_id in self.inventory:
                self.inventory[item_id]["stock_count"] = stock_count
                self.inventory[item_id]["price"] = price
            else:
                print("Item not found in inventory.")

        def check_item_details(self, item_id):
            if item_id in self.inventory:
                item = self.inventory[item_id]
                return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
            else:
                return "Item not found in inventory."

    inventory = Inventory()
    inventory.add_item("I001", "Laptop", 100, 500.00)
    inventory.add_item("I002", "Mobile", 110, 450.00)
    inventory.add_item("I003", "Desktop", 120, 500.00)
    inventory.add_item("I004", "Tablet", 90, 550.00)
    print("Item Details:")
    print(inventory.check_item_details("I001"))
    print(inventory.check_item_details("I002"))
    print(inventory.check_item_details("I003"))
    print(inventory.check_item_details("I004"))
    print("\nUpdate the price of item code - 'I001':")
    inventory.update_item("I001", 100, 505.00)
    print(inventory.check_item_details("I001"))
    print("\nUpdate the stock of item code - 'I003':")
    inventory.update_item("I003", 115, 500.00)
    print(inventory.check_item_details("I003"))
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
        '1a': exercise1a,
        '2a': exercise2a,
        '3a': exercise3a,
        '4a': exercise4a,
        '5a': exercise5a,
        '6a': exercise6a,
        '7a': exercise7a,
        '8a': exercise8a,
        '9a': exercise9a,
        '10a': exercise10a,
        '11a': exercise11a,
        '12a': exercise12a,
        '1b': exercise1b,
        '2b': exercise2b,
        '3b': exercise3b,
        '4b': exercise4b,
        '5b': exercise5b,
        '6b': exercise6b,
        '7b': exercise7b,
        '8b': exercise8b,
        '9b': exercise9b,
        '10b': exercise10b,
        '11b': exercise11b,
        '12b': exercise12b,
        '1c': exercise1c,
        '2c': exercise2c,
        '3c': exercise3c,
        '4c': exercise4c,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 1a do 12a, od 1b do 12b, od 1c do 4c), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '11b' wczyta ćwiczenie 11b). Wpisz 'wyjdź' aby wyjść z programu: ")
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