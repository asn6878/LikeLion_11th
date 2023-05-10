from ManagerRepo import StduentManagerRepo
from Student import Student

class StudentManagerImpl(StduentManagerRepo):
    def __init__(self):
        self.__std_list = []

    def add_student(self, student: Student):
        self.__std_list.append(student)
        print(student.get_name(),"학생이 추가되었습니다.")
    
    def list_student(self):
        if self.__std_list:
            # 리스트 내 학생들의 상태를 보여주기 전, 학점순으로 정렬 진행.
            self.sort_student()
            for i in self.__std_list:
                i.show()
        else:
            print("시스템에 학생이 존재하지 않습니다!!!")
    
    def search_student(self, name):
        if self.__std_list:
            for i in self.__std_list:
                if i.get_name() == name:
                    i.show()
                    return None    
            print(name+" 학생이 존재하지 않습니다.")
        else:
            print("시스템에 학생이 존재하지 않습니다!!!")
    
    def delete_student(self, name):
        flag = False
        if self.__std_list:
            for i in self.__std_list:
                if i.get_name() == name:
                    self.__std_list.pop(self.__std_list.index(i))
                    print(name+ " 학생이 삭제 되었습니다.")
                    flag = True
            if not flag :
                print(name+ "학생이 시스템에 존재하지 않습니다.")
        else :
            print("시스템에 학생이 존재하지 않습니다!!!")

    def update_student(self, name, student):
        if self.is_student_exsist(name):
            for i in self.__std_list:
                if i.get_name() == name:
                    self.__std_list[self.__std_list.index(i)] = student
            print(name+ " 학생의 정보를 변경하였습니다.")
        else :
            print(name+ "학생이 시스템에 존재하지 않습니다.")


    def sort_student(self):
        self.__std_list.sort(key=lambda x:x.get_gpa())

    def is_student_exsist(self, name):
        flag = False
        for i in self.__std_list:
            if i.get_name() == name:
                flag = True
        return flag