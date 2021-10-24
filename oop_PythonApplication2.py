

class Student:
    no_of_students = 0
    def __init__(self, name="", grade=0):
        self.__name=[""]
        self.__grade=[]
        Student.no_of_students += 1
    def get_name(self):
        return self.__name 
    def set_name(self,name):
      self.__name=(name)
    def describe(self): 
       print(f"my name is {self.__name} and my grade is {self.__grade}")

    def get_grade(self):
        return self.__grade 
    def set_grade(self, grade):
       self.__grade=grade
name=input("Enter your name : ")
grade=int(input("Enter your grade : "))
std1=Student()
std1.set_name(name)
std1.set_grade(grade)
std1.describe()


Student=input("please enter name you want to search?:")
is_here =False
if is_here:
  print("try again")
else:
  print("yessssss")

Student=input("here?:")
is_Exist=True
if is_Exist:
       print("not here")
else:
        print("hrer")


#print(student_1.get_name()) 
#student_1.set_name("ahmed")
#student_1.set_age(25)
#student_1.describe()
#addStudent()

#name=input("Enter your name : ")
#grade=int(input("Enter your grade : "))
#std1=Student()
#std1.set_name(name)
#std1.set_grade(grade)
#std1.describe()





