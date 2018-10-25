myfileObj = open("myfile.txt", "a") # r, w , a
#l = [1,2,3,4]
myfileObj.write("Hi This is the content in my file.\n")
myfileObj.write("Adding some more things in file \n")
myfileObj.write("I am trying to use append mode for my file\n")
#myfileObj.close()


myfileObj = open("myfile.txt", "r") # r, w , a
line1=myfileObj.read()
print(line1)


#line1 = myfileObj.readline()
#myfileObj.tell()
#print(help(myfileObj.readlines))
#content = myfileObj.readlines(70)
#for i in content:
#        print(i)

#myfileObj.seek(34)
#print( myfileObj.tell())
#
#line2 = myfileObj.readline()
#print(line2)
#print( myfileObj.tell())
#
#line3 = myfileObj.readline()
#print(line3)
#print( myfileObj.tell())
myfileObj.close()
