class SumTwo:

    def __init__(self):
        pass

    def sum_two(self):
        a = int(input("Enter the first number = "))
        b = int(input("Enter the second number = "))
        c = a + b
        print("Sum of {} and {} is {}".format(a,b,c))
        return


if __name__ == "__main__":
    st = SumTwo()
    st.sum_two()