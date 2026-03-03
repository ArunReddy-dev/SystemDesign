class Teacher:
    __name=None
    def __init__(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def teach(self,Student):
        print(f"{self.__name} is teaching {Student.getName()}")
        