from Vehicle import Vehicle

class Airplane(Vehicle):

	# inisialisasi atribut private
	age = 0 # usia pesawat
	airplaneType = "" # tipe pesawat
	wingsLength = 0 # panjang sayap pesawat


	# konstruktor
	def __init__(self, age = 0, airplaneType = "", wingsLength = 0):
		self.age = age
		self.airplaneType = airplaneType
		self.wingsLength = wingsLength

	# getter dan setter
	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	def setAirplaneType(self, airplaneType):
		self.airplaneType = airplaneType

	def getAirplaneType(self):
		return self.airplaneType

	def setWingsLength(self, wingsLength):
		self.wingsLength = wingsLength

	def getWingsLength(self):
		return self.wingsLength

	# method print data pesawat
	def printAirplane(self):
		self.printVehicle()
		print("Age      			: " + str(self.age))
		print("Airplane Type			: " + str(self.airplaneType))
		print("Wings Length			: " + str(self.wingsLength) + " Meters")