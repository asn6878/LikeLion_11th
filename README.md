# LikeLion_11th

## 4 주차 과제는 django_project_1 입니다.
> 😵 Template의 CSS가 뒤죽박죽입니다. 사실 GPT를 사용해서 이것저것 넣어본것이기도 하고, 아직 CSS를 많이 다뤄보지 않아 해당 프로젝트로 연습중입니다. 시간되는대로 템플릿 언어를 사용한 파일정리 및 코드 분리를 해볼 예정입니다..!😂

> ### reviewer 서민지님
> 1. css를 잘 활용하였다. template언어의 base extends를 활용해 정리하면 더 깔끔할것 같다.
> 2. admin.py 의 커스터마이징 한부분이 좋았다.
> 3. Today 모델이 신박했다.
> 4. post외의 다른 모델들의 CRUD에 대한 테스트 또한 추가되었으면 좋았을거 같다.


이번 과제는 지난주차에 모델링한 `models.py` 을 기반으로 CRUD, Create(Post 생성), Read(Post 한개 조회), Update(Post 업데이트), Delete(Post 삭제) + List(전체조회)를 구현하고, 테스트케이스 `Test.py`를 작성하는 과제입니다.
간단한 게시글을 작성할 수 있는 게시판기능을 구현하였습니다. 

> ### ▶ POST 전체 조회 List
> ![image](https://github.com/asn6878/LikeLion_11th/assets/79460319/be15a4c3-af06-4a1c-a856-153505413ecd)<br>
> (url = 'post/') (view = index) (template = index.html) 
> `Post` 객체내의 데이터를 모두 나타낸다. 글 제목을 클릭해 해당 글의 **detail (READ 글 조회)** 로 이동이 가능하다.

> ### ▶ POST 생성 Create
> ![image](https://github.com/asn6878/LikeLion_11th/assets/79460319/9b7af955-3b09-48cd-a00f-25c61c442491)<br>
> (url = 'post/create/') (view = post_create) (template = create.html)
> 알맞은 값을 입력후, 글작성 버튼을 클릭시 `Post` 객체가 생성되고, Post 전체 조회 화면으로 리디렉션된다.

> ### ▶ POST 조회 Read
> ![image](https://github.com/asn6878/LikeLion_11th/assets/79460319/0447dc72-3711-4933-b509-6ff6dec24631)<br>
> (url = 'post/<int:pk>/') (view = post_receive) (template = detail.html)
> id(Post의 pk)에 해당하는 `Post`의 내용을 확인할 수 있는 창이다.

> ### ▶ POST 업데이트 Update
> ![image](https://github.com/asn6878/LikeLion_11th/assets/79460319/558c732b-0d92-4f57-bdc1-27bd80e83b2d)<br>
> (url = 'post/update/<int:pk>/') (view = post_update) (template = update.html)
> id(Post의 pk)에 해당하는 `Post`의 내용을 수정할 수 있는 창이다. 수정 버튼을 클릭시 Post 전체 조회 화면으로 리디렉션된다.

> ### ▶ POST 삭제 Delete
> ![image](https://github.com/asn6878/LikeLion_11th/assets/79460319/27799bd4-a369-45d2-89ea-2656e16c158d)<br>
> (url = 'post/delete/<int:pk>/') (view = post_delete)
> 해당 url로 이동시 id(Post의 pk)에 해당하는 `Post` 객체를 삭제한다. 삭제를 완료후 Post 전체 조회 화면으로 리디렉션된다.

***
#### TestCase