# File handling 
fileText = "my name is shubham prajapati"
filename = "fileHandling.txt"
fileVar = open(filename,'w')
fileVar.write(fileText)
fileVar.close()

fileName = open(filename,'r')
for line in fileName.readline():
    print(line)