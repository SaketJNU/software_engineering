
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

def take_input():
    print("Enter the first number: ")
    first_number = int(input())
    print("Enter the second number: ")
    second_number = int(input())
    return first_number, second_number


if __name__ == "__main__":
    first_number, second_number = take_input()
    b = greater_of_two(first_number, second_number)
