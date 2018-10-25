class employee():
	def __init__(self,name_arg="None",empid_arg=0):
		self.name=name_arg
		self.empid = empid_arg
		self.designation="Engineer"
		pass

	def __str__(self):	
		return(self.name+ " , " +str(self.empid)+ " , " + self.designation)

	def promote(self,designation_arg):
		self.designation=designation_arg
	


a=employee("Nagesh",689652)
a.promote("Sr.Engineer")
print(a)

