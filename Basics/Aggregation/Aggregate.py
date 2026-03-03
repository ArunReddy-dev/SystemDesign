from Professor import Professor
from Department import Department
class Aggregate:
    def __init__(self):
        # I will create the object of professor and department in this class
        # this is the aggregation between professor and department class
        # aggregation is a relationship between two classes where one class has a reference to another class
        # here department class has a reference to professor class to show the professors of the department
        # both the classes are independent of each other but they are aggregated with each other
        self.professors=Professor("Smith"),Professor("John")
        self.department=Department("Computer Science",self.professors)
    def showDepartment(self):
        self.department.show_professors()
if __name__=="__main__":
    aggregate=Aggregate()
    aggregate.showDepartment()
    
        