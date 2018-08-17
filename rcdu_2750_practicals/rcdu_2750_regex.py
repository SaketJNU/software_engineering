import re
re_object = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
text = "my phone number is 889-242-4782 and my office no is 121-232-4343"
textReg = re_object.findall(text)
print(textReg)