from Person import Person
from Job import Job

class Driver(Person, Job):

	# inisialisasi atribut private
	licenseID = "" # nomor sim
	activeUntil = "" # masa berlaku sim
	vehicleType = "" # tipe kendaraan sim

	# konstruktor
	def __init__(self, licenseID = "", activeUntil = "", vehicleType = ""):
		self.licenseID = licenseID
		self.activeUntil = activeUntil
		self.vehicleType = vehicleType

	# getter dan setter 
	def setLicenseID(self, licenseID):
		self.licenseID = licenseID

	def getLicenseID(self):
		return self.licenseID

	def setActiveUntil(self, activeUntil):
		self.activeUntil = activeUntil

	def getActiveUntil(self):
		return self.activeUntil

	def setVehicleType(self, vehicleType):
		self.vehicleType = vehicleType

	def getVehicleType(self):
		return self.vehicleType

	# method print data pengemudi
	def printDriver(self):
		self.printPerson()
		self.printJob()
		print("License ID   	: " + str(self.licenseID))
		print("Active Until 	: " + str(self.activeUntil))
		print("Vehicle Type 	: " + str(self.vehicleType))