#char=str(input("Enter the string : "))
def myvowels(mystring):
	cons=""
	vowels=""

	for i in char.lower():
		if('a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i):
			vowels+= i
		else:
			cons+= i

	return vowels,cons	

#v,c=myvowels(char)
#print("Vowels : ",v)
#print("Consonants : ",c)




