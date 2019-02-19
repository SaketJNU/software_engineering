def sum_two(a, b):
   return a + b

if __name__ == "__main__":
   a = int(input("Enter the first number: "))
   b = int(input("Enter the second number: "))
   print("Sum of {} and {} is {}".format(a, b, sum_two(a,b)))
