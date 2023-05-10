from ManagerImpl import StudentManagerImpl

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
        return self.__student_repo.is_student_exsist(name)

    def sort_student(self):
        self.__student_repo.sort_student()