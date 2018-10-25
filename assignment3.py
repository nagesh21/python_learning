char=input()
cons=""
vowels=""
for i in char.lower():
	if('a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i):
		vowels+= i
	else:
		cons+= i

print ("Vowels is the string :",vowels)
print("Consonants in the string :",cons)


