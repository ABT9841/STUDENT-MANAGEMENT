# #  Just use simple encapuslation
# student course management system
# # encapsulating student class into course

class Student:
    def __init__(self,name,marks): # this is used for instanitaing meaning when assigning value to an object created . this will run automatically
        self.name = name  # it ties up this attributes(varaibales and properties) to the object  not the class
        self.marks = marks

    def get_marks(self): # here without self it doesnt know which object we are refering to. 
        return self.marks

# Creating a class Course

class Course:
    def __init__(self,name,max_student): 
        self.name = name
        self.max_student = max_student
        self.students=[] # created a list to add the student object to it.[ here s1 and s2 are appended]
 
 # to add the student object to the course 
    def add_student(self,student): # here student is an student object we are passing
        if self.max_student > len(self.students):
            self.students.append(student)
            return True
        return False
    
# to find the average marks of student
    def average_marks(self):
        value = 0
        for i in self.students: # here i represent to the current object,not an index
            value += i.get_marks()

        return value / len(self.students)
            



# instantiating   student class
s1 = Student("Alish",95)
s2 = Student("Ram",90)
s3 = Student("Anish",99)  # when i try to print object it refrences to the memomory location. refrences means accesing the object through varaiable

# instatiating course class and encapsulating student using add_student method
course1 = Course("Science",2)
course1.add_student(s1) # adding the s1 object now course1 object have access to all its attributes and methods.
course1.add_student(s2)
course1.add_student(s3) # returns false due to limit called max_student
print(course1.name)
print(course1.students[0].name) # here i am accessing the class inside class (encapsulated class) and accsing the attribute of the object which is stored in list at index0
print("THE AVERAGE MARKS OF THE STUDENT IS",course1.average_marks())
