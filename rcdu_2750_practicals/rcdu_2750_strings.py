"""
Strings are amongst the most popular types in Python. 
We can create them simply by enclosing characters in quotes. 
Python treats single quotes the same as double quotes. 
Creating strings is as simple as assigning a value to a variable.
"""

import string
name = "shubham"
print("Data in upper case : ",name.upper()) # upper() for UPPER case strings conversion

lower = "PRAJAPATI" 
print("Data in lower case : ",lower.lower()) # lower() for lower case strings conversion

takeData = input("Please enter any data : ")
print("Here is the user input data : ",takeData) # input() for taking data from user

# NOTE -> input() takes data in string if you want to do some functionality with numeric please 
# convert that data in your dataType like : int float etc.


# Let's take a look of some in-built string functions

print(string.ascii_uppercase) # ascii_uppercase gives A-Z 

print(string.digits)  # it gives 0-9


# string formatter 
"""
% c -> character 
% s -> string
% i ,d-> signed integer deciaml integer
% u -> unsigned decimal integer
% x -> hex decimal integer (lowercase)
% X -> hex decimal integer (UPPERCASE)
% o -> octal decimal integers 
% e -> exponantial notation (lowercase, e^3)
% E -> exponantial notation (10^3)
% f -> floating point numbers
"""


print("hexa decimal : ",string.hexdigits) # string.hexdigits gives hexadecimal number
print("only printable no : ",string.printable ) # printable characters only
print("Octa decimal no : ",string.octdigits) # Octa decimal no's

print(type(name.isalnum()),name.isalnum()) # checks alphanumeric

print(type(name.isnumeric()),name.isnumeric()) # checks numeric
print(type(name.isdigit()),name.isdigit()) # checks digit

print("Split func : ",name.split()) # Splits stings 
print("Starts With ",name.startswith('s')) # Checks starting char of string return boolean

number = " my number is 97748826478" 

print(number.split()) # Basically returns list 

print(number.strip()) # removes unprintable charaters from both side left and right
print(number.rstrip()) # removes unprintable charaters right side only
splitn= number.split()

for onew in splitn:
    if (onew.strip()).isdigit():
        if len(onew.strip())== 11:
            print("No", onew.strip())



str1 = "abcdxyzabc"
print(str1.replace('a','k')) # occurance of 'a' by 'k' 
str2 = str1.replace('a','k')
print(str2.replace('acd','shu'))
print(str1.capitalize()) # Capitalize capital only first char of an string

# Method 1st
newName = "shubham     kumar  prajapati"
splitName = newName.split()
print(splitName)
print(splitName[0][0].upper() + ". "+ splitName[1][0].upper() + ". "+ splitName[2].capitalize())
wordlen = len(splitName)
print("Length of  list : ",wordlen)

# Method 2nd
count = 0
newname = ""
for aw in splitName:
    count +=1
    if count < wordlen:
        newname += aw[0].upper()+ ". "
    else :
        newname += aw[0].upper()+aw[1:]
print("By method 2nd : ",newname)