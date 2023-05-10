from Student import *
from ManagerImpl import StudentManagerImpl
from ManagerService import StudentManagerService

# Student 인스턴스 생성 함수

def student_generator():
    informations = []
    informations.append(input("학번: "))
    informations.append(input("이름: "))
    informations.append(input("나이: "))
    informations.append(input("전공: "))
    informations.append(input("학점: "))
    student = Student(informations[0], informations[1], informations[2], informations[3], informations[4])
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
            student = student_generator()
            manager.add_student(student)
        elif select == 2:
            manager.list_student()
        elif select == 3:
            manager.search_student(input("이름: "))
        elif select == 4:
            name = input("삭제할 학생의 이름: ")
            result = manager.delete_student(name)
            if result :
                print(name+" 학생의 삭제가 완료 되었습니다.")
        elif select == 5:
            name = input("수정할 학생의 이름: ")
            if manager.is_student_exsist(name):
                student = student_generator()
                manager.update_student(name,student)
            else:
                print(name+ "학생이 시스템에 존재하지 않습니다.")
        elif select == 6:
            print("시스템 종료")
            break
        else:
            print("없는 메뉴입니다. 다시 입력해주세요.")

if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)