class Vehicle():
	
	# insialisasi atribut private
	name = "" # nama kendaraan
	fuelType = "" # tipe bahan bakar 
	maxPassengers = 0 # kapasitas penumpang
	terrain = "" # medan kendaraan
	speed = 0 # kecepatan kendaraan

	# konstruktor
	def __init__(self, name = "", fuelType = "", maxPassengers = 0, terrain = "", speed = 0):
		self.name = name
		self.fuelType = fuelType
		self.maxPassengers = maxPassengers
		self.terrain = terrain
		self.speed = speed

	# getter dan setter 
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setFuelType(self, fuelType):
		self.fuelType = fuelType

	def getFuelType(self):
		return self.fuelType

	def setMaxPassengers(self, maxPassengers):
		self.maxPassengers = maxPassengers

	def getMaxPassengers(self):
		return self.maxPassengers

	def setTerrain(self, terrain):
		self.terrain = terrain

	def getTerrain(self):
		return self.terrain

	def setSpeed(self, speed):
		self.speed = speed

	def getSpeed(self):
		return self.speed

	# method print
	def printVehicle(self):
		print("Name				: " + str(self.name))
		print("Fuel Type           		: " + str(self.fuelType))
		print("Maximum Passengers  		: " + str(self.maxPassengers))
		print("Terrain           		: " + str(self.terrain))
		print("Speed				: " + str(self.speed) + " Km/h")