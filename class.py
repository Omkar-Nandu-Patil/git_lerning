class personal_data:
	college = "Jain College"
	
	def __init__(self,name,roll,sem,branch):
		self.__name = name
		self.__roll = roll
		self.__sem = sem
		self.__branch = branch
		
	def DetaiOfStudent(self):
		print("Name  of the student = {}".format(self.__name))
		print("Roll number = {}".format(self.__roll))
		print("Sem =  {}".format(self.__sem))
		print("Branch =  {}".format(self.__branch))
	
	def __del__(self):
		print(" variables are deleted ")
		
s1=personal_data('Omkar',103,7,'ECE')

s1.DetaiOfStudent()		
print("name = {}".format(s1.__name))
