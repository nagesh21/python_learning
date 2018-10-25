#myfileObj1=open("replace.txt","w")
myfileObj = open("replace.txt", "r")
line=myfileObj.readline()
print(line)
myfileObj.close()
myfileObj1=open("replace.txt","w")
for i in line:
	a=i.replace("test","Test")
	myfileObj1.write(a + "\n")
myfileObj1.close()
myfileObj.close()

