class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"
class Man(Person):
    gender ='Male'
    no_of_man =0
     
    def __init__(self,name,age,voice):
        super().__init__(name,age)
        self.voice = voice
        Man.no_of_men +=1

    def display(self):
        string = super().display()
        return string +f"and voice is {self.voice} and gender is {self.gender}"
man = Man("is islam",40,"hard")
print(man.display())
print(man.no_of_men)

