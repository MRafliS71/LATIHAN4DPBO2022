from Person import Person
from Job import Job
from Driver import Driver

# Input dummy data test untuk person
print("====== DUMMY DATA TEST FOR PERSON ======")
print("")
person1 = Person()
person1.setNIK("327771381031")
person1.setName("Doni")
person1.setAge("23")
person1.setGender("Male")
person1.printPerson()

print("")
person3 = Person()
person3.setNIK("327631931371")
person3.setName("Tika")
person3.setAge("25")
person3.setGender("Female")
person3.printPerson()

print("")
person5 = Person()
person5.setNIK("32755498488412")
person5.setName("Soap")
person5.setAge("45")
person5.setGender("Male")
person5.printPerson()

print("")
person4 = Person()
person4.setNIK("32554741444456")
person4.setName("Joe Biden")
person4.setAge("60")
person4.setGender("Male")
person4.printPerson()

print("")
person2 = Person()
person2.setNIK("327498584844548")
person2.setName("Lady Gaga")
person2.setAge("53")
person2.setGender("Female")
person2.printPerson()

# Input dummy data test untuk job
print("")
print("====== DUMMY DATA TEST FOR JOB ======")

print("")
job1 = Job()
job1.setNIP("19955155580")
job1.setCompanyName("Coca Cola")
job1.setPosition("Marketing Specialist")
job1.printJob()

print("")
job2 = Job()
job2.setNIP("1988455681254")
job2.setCompanyName("Alibaba Group")
job2.setPosition("Manager Technology")
job2.printJob()

print("")
job4 = Job()
job4.setNIP("1968854498848")
job4.setCompanyName("Kopi Kenangan")
job4.setPosition("Head of Barista")
job4.printJob()

print("")
job5 = Job()
job5.setNIP("195545478948")
job5.setCompanyName("Borma")
job5.setPosition("Cashier")
job5.printJob()

print("")
job3 = Job()
job3.setNIP("1988889915656")
job3.setCompanyName("3Second")
job3.setPosition("Senior Designer Specialist")
job3.printJob()

# Input dummy data test untuk Driver
print("")
print("====== DUMMY DATA TEST FOR DRIVER ======")

print("")
driver2 = Driver()
driver2.setNIK("327894425555")
driver2.setName("Carl Johnson")
driver2.setAge("38")
driver2.setGender("Male")
driver2.setNIP("198689495")
driver2.setCompanyName("Maxxi")
driver2.setPosition("Driver")
driver2.setLicenseID("0035")
driver2.setActiveUntil("11/08/2035")
driver2.setVehicleType("Random")
driver2.printDriver()

print("")
driver3 = Driver()
driver3.setNIK("32749649545890")
driver3.setName("Han Solo")
driver3.setAge("46")
driver3.setGender("Male")
driver3.setNIP("1965548948")
driver3.setCompanyName("Intergalaxtic")
driver3.setPosition("Driver")
driver3.setLicenseID("0188")
driver3.setActiveUntil("17/04/2040")
driver3.setVehicleType("Millenium Falcon")
driver3.printDriver()

print("")
driver1 = Driver()
driver1.setNIK("327849554449")
driver1.setName("Bruce Wayne")
driver1.setAge("53")
driver1.setGender("Male")
driver1.setNIP("1985554555")
driver1.setCompanyName("Wayne Enterprise")
driver1.setPosition("Driver")
driver1.setLicenseID("0144")
driver1.setActiveUntil("24/09/2044")
driver1.setVehicleType("Batmobile")
driver1.printDriver()

print("")
driver4 = Driver()
driver4.setNIK("32327459961")
driver4.setName("Lightning Mcqueen")
driver4.setAge("34")
driver4.setGender("Male")
driver4.setNIP("19594984")
driver4.setCompanyName("Rustteez")
driver4.setPosition("Primary Driver")
driver4.setLicenseID("0096")
driver4.setActiveUntil("07/04/2077")
driver4.setVehicleType("Nascar")
driver4.printDriver()

print("")
driver5 = Driver()
driver5.setNIK("32711165194")
driver5.setName("Maggie Payton")
driver5.setAge("46")
driver5.setGender("Female")
driver5.setNIP("198848915")
driver5.setCompanyName("Volkswagen")
driver5.setPosition("Driver")
driver5.setLicenseID("0053")
driver5.setActiveUntil("07/09/2029")
driver5.setVehicleType("Beetle")
driver5.printDriver()