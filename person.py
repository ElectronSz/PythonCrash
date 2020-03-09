class Person:
    fname = ""
    lname = ""
    age = 0

    # def __init__(self, fname, lname, age):
    #     self.fname = fname
    #     self.lname = lname
    #     self.age = age

    def setFname(self, fname):
        self.fname = fname

    def setLname(self, lname):
        self.lname = lname
    
    def setAge(self, age):
        self.age = age

    def getFullName(self):
        return self.fname +" "+self.lname

person = Person()
person.setFname("Musa")
person.setLname("Masuku")

print(person.fname)