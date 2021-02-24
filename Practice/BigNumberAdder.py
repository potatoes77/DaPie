class BigNumberAdder:
	sum = 0
	# constructor
	def __init__(self, num1, num2):
		self.num1 = num1 # Alt + enter on parameter
		self.num2 = num2 # Alt + enter on parameter

	def RegularAdder(self):
		self.sum = self.num1 + self.num2
		# return self.sum


math = BigNumberAdder(1000, 2000)
math.RegularAdder()
print(math.sum)


# 	# default constructor
# 	def __init__(self):
# 		self.geek = "MeepforMeeps"
#
# 	# a method for printing data members
# 	def print_Geek(self):
# 		print(self.geek)
#
#
# # creating object of the class
# obj = GeekforGeeks()
#
# # calling the instance method using the object obj
# obj.print_Geek()
