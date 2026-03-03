from Student import Student
from Teacher import Teacher
class Associate:
    # I will create the object of teacher and student in this class
    def __init__(self):
        self.student=Student("John")
        self.teacher=Teacher("Smith")
    # i m sending student object to teacher class to
    # call the teach method
    # this is the association between teacher and student class
    # association is a relationship between two classes where one
    # class uses the object of another class to perform some action
    # here teacher class is using the student class to perform the teach method
    # both the classes are independent of each other but they are associated with each other
    def startTeaching(self):
        self.teacher.teach(self.student)    
        
# 
if __name__=="__main__":
    associate=Associate()
    associate.startTeaching()
    
    