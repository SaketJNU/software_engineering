# Write a program to find the max of two numbers
"""
print("Enter the first number: ")
first_number = int(input())
print("Enter the second number: ")
second_number = int(input())
if first_number > second_number:
    print("Entered number {} is greater than {}". format(first_number, second_number))
elif first_number == second_number:
    print("Entered number", first_number, " and ", second_number, " are same")
else:
    print("Entered number {} is smaller than {}".format(first_number, second_number))
"""
def greater_of_two(first_number, second_number):
    bigger_number = 0
    if first_number > second_number:
        bigger_number = first_number
        print("Entered number {} is greater than {}".format(first_number, second_number))
    elif first_number == second_number:
        bigger_number = first_number
        print("Entered number", first_number, " and ", second_number, " are same")
    else:
        bigger_number = second_number
        print("Entered number {} is smaller than {}".format(first_number, second_number))

if __name__ == "__main__":
    print("Enter the first number: ")
    first_number = int(input())
    print("Enter the second number: ")
    second_number = int(input())
    b = greater_of_two(first_number, second_number)

    ## Executable

    # Saket_JNU