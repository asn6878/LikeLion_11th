# LikeLion_11th

## 2 주차 과제는 second_week 파일내에 있으며, 코드리뷰 내용 수정 완료되었습니다.

* * *
## 코드리뷰 내용 (리뷰어 : 염동환)

1. 클래스별로 파일을 구분해서 관리하는 것도 좋을 것 같습니다.

2. Student class에 show라는 메소드를 추가함으로써, 학생 정보를 출력하는 코드가 매우 간결해져 가독성이 좋았습니다.

3. main에서 학생 정보를 입력받는 것을 student_generator()함수를 이용함으로써 코드가 간결해져 좋았습니다. 그런데, student_generator()함수의 코드를 보면 입력받은 정보들을 리스트(informations)에 받아 사용합니다. student_id, name..과 같이 각각의 변수를 만들어서 사용하는것이 헷갈릴 일이 없어 좋을 것 같다는 생각을 했습니다.(제 개인적인 생각입니당)

4. 학생이 추가될 때마다 정렬을 수행하므로 한번에 여러 학생이 추가되면 비효율적일 것 같습니다. 전체 학생을 출력할 때만 정렬하면 좋지않을까 생각했습니다

5. Impl에서 delete_student(), update_student()를 보면,..
```
for i in self.__std_list:
                if i.get_name() == name:
                    self.__std_list[self.__std_list.index(i)] = student
                    print(name+ " 학생의 정보를 변경하였습니다.")
                else:
                    print(name+" 학생이 존재하지 않습니다.")
```
부분에서 else문의 "~학생이 존재하지 않습니다." 라는 문장이 여러번 출력될 수 있을 것 같습니다. flag를 이용해서 한 번도 삭제가 일어나지 않은 경우 마지막에 한 번만 "~학생이 존재하지 않습니다." 라는 문자이 출력되게 하면 좋을 것 같습니다.

6.is_student_exist()가 제대로 동작하지 않을 것 같습니다.
학생 존재 여부를 확인하는 동작은 StudentManagerImpl에 구현되어 있습니다. 여기서 True 혹은 False를 리턴합니다. 이 메소드를 StudentManagerService에서 student_repo를 통해 호출하고, True혹은 False값을 전달받습니다. 그런데 StudentManagerService에서는 전달받은 이 값들을 리턴하지 않습니다. 따라서 Service의 메소드를 호출하는 메인에서는 True/False값을 전달받지 못할 것 같습니다. 
```
    def is_student_exsist(self, name):
        return self.__student_repo.is_student_exisist(name) 
```
위와 같이 수정해야 될 것 같습니다.


7. 학생 정보 수정 - 존재하지 않는 이름을 입력한 경우 
manager.is_student_exist(name)이 False를 반환하므로 아무런 동작도 하지 않고 넘어갑니다.
반면, "~학생이 존재하지 않습니다"를 출력해주는 코드는 update_student()에 있고, 이 메소드는 실행되지 않으므로 아무런 출력이 나오지 않습니다. 

전체적으로 변수명, 함수명 등이 이해하기 쉽게 작명되어 있어 코드를 읽기 좋았습니다. 또, 함수와 메소드들로 코드를 간결하게 작성해주셔서 가독성이 좋았던 것 같습니다. 좋은 코드를 보고 많이 공부할 수 있었습니다 감사합니다!

* * *


1. 각 클래스별로 파일 분리 완료.

2. 정렬이 불필요하게 많이 실행되던것을 수정 완료. -> 비교적 학생 추가 및 수정작업이 많을때에의 TimeComplexity 감소

3. delete_student 및 update_student의 반복문 문제 및 예외처리 오류 정정 완료.

4. is_student_exisist() 메소드 수정 완료.


