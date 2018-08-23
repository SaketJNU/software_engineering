# WAP for maximum length unique substring

raw_string = input("Enter a alphanumeric string: ")
if raw_string.isalnum():
    sub_string = ""
    temp = raw_string[0]
    for c in raw_string[1:]:
        if c not in temp:
            temp = temp + str(c)
        else:
            if len(temp) > len(sub_string):
                sub_string = temp
                temp = c
    if len(temp) > len(sub_string):
        sub_string = temp
    print("Maximum length substring is = {}".format(sub_string))
else:
    print("Entered string {} is not an alpha-numeric string.".format(raw_string))