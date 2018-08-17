import re
# text = "%20 Geo 20 % is my hdjkhf **?? /// andj  "
# re_obj = re.compile(r'a-zA-z)

# Multiple keys start from here ..


re_obj = re.compile(r'saket |shubham')   # Pipeline sing '|' 
name = re_obj.findall('saket kumar and shubham')
print("Multiple Keys Matching",name)

reObj = re.compile(r'Shu(bham|ku|ch)')
newName = reObj.search('Shubham kumar') # single search 
print("Single search",newName)

# Multiple Keys ends here !


# Optional Maching start here !
re_obj2 = re.compile(r'sak(et)?ch') #first checks outer part if matches then matches optional part 
newName3 = re_obj2.search('saketch kumar')
print("optional matching",newName3)

# Optional Maching ends here !


#Multiple Matching start here !
re_obj4 = re.compile(r'Bat(wo)*man') # '*' works even on zero occurrence
name5 = re_obj4.search('I am a Batman')
name6 = re_obj4.search('I am a Batwoman')
name7 = re_obj4.search('I am a Batwowowoman')

print(name5,name6,name7)

re_obj5 = re.compile(r'Bat(wo)+man') # '+' works with minimum one occurrence
name8 = re_obj5.search('I am a Batwoman')
print(name8)


re_obj6 = re.compile(r'(wo){3}')
name8 = re_obj6.search('wowowo this is ')
name9 = re_obj6.search('wowo this is ')
name10 = re_obj6.search('wowowowo this is ')

print(name8,name9,name10)


# Gridy matching 
re_obj7 = re.compile(r'(wo){1,1}')
name11 = re_obj7.findall('wo wowo wowowo  this is ')
print(name11)


# Charater Classes
"""
\d = Matches digits. Equivalent to [0-9].
\D = Matches nondigits.
\A = Matches beginning of string.	
\Z = Matches end of string. If a newline exists, it matches just before newline.
\z = Matches end of string.
\G = Matches point where last match finished.
\w = Matches word characters.
\W = Matches nonword characters.
\s = Matches whitespace. Equivalent to [\t\n\r\f].
^ = Matches beginning of line.
$ = Matches end of line.
. = Matches any single character except newline. Using m option allows it to match newline as well.

more information https://www.tutorialspoint.com/python/python_reg_expressions.htm

"""

re_obj12= re.compile(r'[aeiouAEIOU]')
obj=re_obj12.findall('This is my own class room I am')
print(obj)


re_obj13= re.compile(r'[^aeiou AEIOU]')
obj13=re_obj13.findall('This is my own class room I am')
print(obj13)


re_obj15 = re.compile(r'\d$')
char3 = re_obj15.search('This is ')
char4 = re_obj15.search('This is 84')

print(char3,char4)


reWildCard = re.compile(r'.at')
char5 = reWildCard.findall('ccccat is wearing hat and sat on the mat @at.')
print(char5)