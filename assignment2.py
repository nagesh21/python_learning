Epsilon="Hub1 building of SEZ Karle town park st 23, 560045, mob number = 8888888888"

name=Epsilon.split()
print(name)

for j in name:
	repl=j.strip(",./t ")


	if repl.isnumeric():
		if len(repl)==6:
			print("Pin code :",repl)

		elif len(repl)==10:
			print("Mobile :",repl)

	

