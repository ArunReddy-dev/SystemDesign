class Department:
    __name=None
    professors=[]
    def __init__(self,name,professors):
        self.__name=name
        self.professors=professors
    def getName(self):
        return self.__name
    def show_professors(self):
        print("Department Name:",self.__name)
        for professor in self.professors:
            print(professor.getName())  
        