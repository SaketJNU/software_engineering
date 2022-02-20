'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
'''


class PracticalTwo:


    def __init__(self):
        pass


    def input_number(self):
        number = int(input("Please enter a number:  "))
        return number

    def show_message(self, n):
        reminder = n %2
        if reminder == 0:
            print("You have entered an even number.")
        else:
            print("You have entered an odd number.")


if __name__ == "__main__":
    pt = PracticalTwo()
    n = pt.input_number()
    pt.show_message(n)
