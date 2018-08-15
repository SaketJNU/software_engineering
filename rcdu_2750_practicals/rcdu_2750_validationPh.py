def isPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    
    if text[7] !='-':
        return False
    
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    
    return True




# text = input()
# print(isPhoneNumber(text))

text = "my phone number is 889-242-4782 and my office no is 121-232-4343"
textWord = text.split()

for tw in textWord:
    if isPhoneNumber(tw)==True:
        print("A new phone no {} is founded".format(tw))