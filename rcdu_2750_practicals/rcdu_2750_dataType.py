"""
# dataTypes : 
        List[] , Tuple() perentheses are optional, Dictionary{} ,Set , Sequence ,String(immutable)
# sequence :
         [List ,Tuple ,String] (It follows indexing)
# indexing : 
         starts from 0 
         its supports (in , not in ) during flow control
         """

newSting = "shubham"
for char in newSting:
    print(char)


list = ["s","h","u","b","h","a","m"] # this is list
print(" printing list : ",list)
for char in list:
    print(char)


tuple=("s","h","u","b","h","a","m") # this is tuple
print("printing tuple  : ",tuple)

for char in tuple:
    print(char)


print("Lenght of shubham : ",len(newSting))

print(newSting[0:2]) # it strat from 0 index and ends to index 2(-1)



zoo = ["elephant","tiger","rabbit"]
print("before appending : ",zoo)
zoo.append("Lion")               # .append use for appending data into list
print("After appending data : ",zoo)


newzoo=[zoo,"camel"]
print(newzoo)
newzoo.append(zoo)
newzoo.append("camel")
print(newzoo)


newzoo1 = ["elephant", "tiger", "mohit","karala"]
zooset= set(zoo)
newzooset= set(newzoo1)
print (zooset & newzooset)

print(zooset.intersection(newzooset))

# Dictionary :  {"key":"value"} pair
dict1 = {"name":"shubham", "course":"b.voc", "students":5 , "studentName":["a","b","c"]}
print(dict1.keys())
print(dict1.values())

for key , value in dict1.items():
    print(key, "and it's values =", value)

del dict1["students"]
print(dict1)

print(dict1.get("name"))