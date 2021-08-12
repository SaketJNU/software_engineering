''' 1.	Create a program that asks user to enter their name and their age.
Print out a message addressed to them that tells them the
year that they will turn 100 years old.
'''


class PracticalOne:

    def __init__(self):
        pass

    def show_message(self, name, age):
        print("Hi {}, after 100 years, you will be {} old.".format(name, age + 100))
        return

    def input_values(self):
        name = input("Please enter your name:  ")
        age = int(input("Please enter your age:  "))
        return name, age

if __name__ == "__main__":                            # Self Executable
    po = PracticalOne()                             # Object creation for class
    n, a = po.input_values()
    po.show_message(n,a)
