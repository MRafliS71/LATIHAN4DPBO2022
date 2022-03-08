class Person():

	# atribut private
	nik = "" # nomor induk kependudukan
	name = "" # nama
	age = "" # umur
	gender = "" # jenis kelamin

	# konstruktor
	def __init__(self, nik = "", name = "", gender = "", age = ""):
		self.nik = nik
		self.name = name
		self.gender = gender
		self.age = age

	# getter dan setter 
	def setNIK(self, nik):
		self.nik = nik

	def getNIK(self):
		return self.nik

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	def setGender(self, gender):
		self.gender = gender

	def getGender(self):
		return self.gender

	# method print data orang
	def printPerson(self):
		print("NIK          	: " + str(self.nik))
		print("Name         	: " + str(self.name))
		print("Age		: " + str(self.age))
		print("Gender       	: " + str(self.gender))