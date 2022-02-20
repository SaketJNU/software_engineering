# Class for even-odd computation

class EvenOdd:

    def __init__(self):
        pass

    def even_odd(self):
        number = int(input("Enter the number= "))  # for getting input for key-board
        if number % 2 == 0:
            print("Entered number {0} is an Even number".format(number))  # Indentation
        else:
            print("Entered number {0} is an Odd number".format(number))



if __name__ == "__main__":
    eo = EvenOdd()                # Object of Even-Odd Class
    eo.even_odd()                 # Calling the even_odd() method of class