class Student:
    def __init__(self, std_num, name, age, major, gpa):
        self.__stdnum = std_num
        self.__name = name
        self.__age = age
        self.__major = major
        self.__gpa = gpa

    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa

    def show(self):
        print("------------------------------")
        print("학번:",self.__stdnum)
        print("이름:",self.__name)
        print("나이:",self.__age)
        print("전공:",self.__major)
        print("학점:",self.__gpa)

    def __str__(self):
        return self.__name
    
