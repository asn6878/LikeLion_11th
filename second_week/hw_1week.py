from abc import *

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

class StduentManagerRepo(metaclass=ABCMeta):
    @abstractmethod
    def add_student(self, student): # 학생 추가
        pass

    @abstractmethod
    def list_student(self): # 전체 학생 조회
        pass

    @abstractmethod
    def search_student(self, name): # 학생 조회
        pass

    @abstractmethod
    def delete_student(self, name): # 학생 제거
        pass

    @abstractmethod
    def update_student(self, name, student): # 학생 수정
        pass

class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManagerImpl()

    def add_student(self, student): # 학생 추가
        self.__student_repo.add_student(student)

    def recieve_student(self): # 학생 출력
        self.__student_repo.recieve_student()

    def list_student(self): # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        self.__student_repo.delete_student(name)

    def update_student(self, name, student): # 학생 수정
        self.__student_repo.update_student(name, student)
    
    def is_student_exsist(self, name):
        self.__student_repo.is_student_exisist(name)

    def sort_student(self):
        self.__student_repo.sort_student()

class StudentManagerImpl(StduentManagerRepo):
    def __init__(self):
        self.__std_list = []

    def add_student(self, student: Student):
        self.__std_list.append(student)
        print(student.get_name(),"학생이 추가되었습니다.")
    
    def list_student(self):
        if self.__std_list:
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
        if self.__std_list:
            for i in self.__std_list:
                if i.get_name() == name:
                    self.__std_list.pop(self.__std_list.index(i))
                    print(name+ " 학생 삭제가 완료 되었습니다.")
                else :
                    print(name+" 학생이 존재하지 않습니다.")
        else:
            print("시스템에 학생이 존재하지 않습니다!!!")

    def update_student(self, name, student):
        if self.__std_list:
            for i in self.__std_list:
                if i.get_name() == name:
                    self.__std_list[self.__std_list.index(i)] = student
                    print(name+ " 학생의 정보를 변경하였습니다.")
                else:
                    print(name+" 학생이 존재하지 않습니다.")
        else:
            print("시스템에 학생이 존재하지 않습니다!!!")

    def sort_student(self):
        self.__std_list.sort(key=lambda x:x.get_gpa())

    # 학생의 존재 여부를 확인하기 위해 추가구현한 메소드
    def is_student_exisist(self, name):
        for i in self.__std_list:
            if i.get_name() == name:
                return True
            else:
                return False

# Student 인스턴스 생성 함수
def student_generator(info: list):
    student = Student(info[0], info[1], info[2], info[3], info[4])
    return student

def main(manager: StudentManagerService):
    while(True):
        print("===============")
        print("1. 학생 추가")
        print("2. 전체 학생 조회")
        print("3. 학생 조회")
        print("4. 학생 제거")
        print("5. 학생 수정")
        print("6. 종료")
        try:
            select = int(input())
        except(ValueError):
            print("정수를 입력해 주세요.")
            continue
        if select == 1:
            informations = []
            informations.append(input("학번: "))
            informations.append(input("이름: "))
            informations.append(input("나이: "))
            informations.append(input("전공: "))
            informations.append(input("학점: "))
            student = student_generator(informations)
            manager.add_student(student)
            # 학생 신규 추가 후 학점 기준 정렬 실행
            manager.sort_student()
        elif select == 2:
            manager.list_student()
        elif select == 3:
            manager.search_student(input("이름: "))
        elif select == 4:
            name = input("삭제할 학생의 이름: ")
            manager.delete_student(name)
        elif select == 5:
            name = input("수정할 학생의 이름: ")
            if manager.is_student_exsist(name) == True:
                informations = []
                informations.append(input("학번: "))
                informations.append(input("이름: "))
                informations.append(input("나이: "))
                informations.append(input("전공: "))
                informations.append(input("학점: "))
                student = student_generator(informations)
                manager.update_student(name,student)
        elif select == 6:
            print("시스템 종료")
            break
        else:
            print("없는 메뉴입니다. 다시 입력해주세요.")

if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)