myfileObj = open("rangefile.txt","w")
#l=[1,2,3,4,5]
#for i in l:
for i in range(5):
#	myfileObj.write("Line Number : "+str(i)+"\n")
	myfileObj.write("Line Number : " +str(myfileObj.tell())+ "\n")
#For Reading file values

myfileObj=open("rangefile.txt","r")
lines=myfileObj.read()
print(lines)
myfileObj.close()

