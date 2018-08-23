# WAP a program


def sum(a, b):
    return a+b


first_number = input("Enter the first number as a whole number: ")
second_number = input("Enter the second number as a whole number: ")
if first_number.isnumeric() and second_number.isnumeric():
    total = sum(int(first_number), int(second_number))
    print("*"*total, total, total + len(str(total)))
