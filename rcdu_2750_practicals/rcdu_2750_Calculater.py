class Calculator():
    def __init__(self):
        pass

    def addition(sefl,number, number2):
        return number+number2

    def mult(self, number, number2):
        return number*number2

    def sub(self, number, number2):
        return number-number2

    
    def div(self, number, number2):
        return number/number2
        

    def mathOps(self):
        test = 'Y'

        while test=='Y' or test=='y':

            number = int(input("Enter First No = "))
            number2 = int(input("Enter Second No = "))
            
            print("Choice of Operations : \n 1. For Addition \n 2. For Multi  \n 3. For Sub \n 4 For Division \n")
            choice = int(input("Enter Your Choice : "))
            output = 0.0
            if choice == 1 :
                output = self.addition(number,number2)
            
            elif choice == 2 :
                output = self.mult(number,number2)

            elif choice == 3 :
                output = self.sub(number,number2)
            
            elif choice == 4 :
                output = self.div(number,number2)

            else :
                output = "Invailid Input"

            print("Output is ", output)


            test = input("  Do you want to continue ? \n Press 'Y' for Yes \n Enter Your choice : ")



if __name__ == "__main__" :
    matho =  Calculator()
    matho.mathOps()