# Creating only function

def even_odd(number):
    if number % 2 == 0:
        print("Entered number {0} is an Even number".format(number))  # Indentation
    else:
        print("Entered number {0} is an Odd number".format(number))


if __name__ == "__main__":                      #  Self-Executable
    c = 1
    while c ==1:
        n =  int(input("Enter the number = "))       # for getting input for key-board
        even_odd(n)
        c = int(input("Enter 1 to continue = "))