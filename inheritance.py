class person:
    name = ''
    age = ''    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getInfo(self):
        print(f"This person's name {self.name} {self.age} years old")

person1 = person('Hafizh', 13)
person1.getInfo()

person2 = person('Azzamy', 15)
person2.getInfo()

class student(person):
    def __init__(self, name, age, nis):
        super().__init__(name, age)   
        self.nis = nis

    def study(self, subject):
        print(f'{self.name} with NIS {self.nis} study {subject}')

def getInfo(self):
        print(f"This person's name {self.name} With NIS {self.nis}, {self.age} years old")

student1 = student('salma', 16, '20250101')
student1.getInfo()
student1.study('Math')



''''''''
#Tugas
''''''''



class Teacher(person):
    def __init__(self, name, age, nip):
        super().__init__(name, age)   
        self.nip = nip

    def mengajar(self, subject):
        print(f'{self.name} with NIP {self.nip} mengajar {subject}')

def getInfo(self):
        print(f"This person's name {self.name} With NIP {self.nip}, {self.age} years old")

student1 = Teacher('salma', 16, '12345678')
student1.getInfo()
student1.mengajar('Math')