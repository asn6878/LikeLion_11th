# LikeLion_11th

## 4 주차 과제는 django_project_1 입니다.
> 😵 Template의 CSS가 뒤죽박죽입니다. 사실 GPT를 사용해서 이것저것 넣어본것이기도 하고, 아직 CSS를 많이 다뤄보지 않아 해당 프로젝트로 연습중입니다. 시간되는대로 템플릿 언어를 사용한 파일정리 및 코드 분리를 해볼 예정입니다..!😂

이번 과제는 지난주차에 모델링한 `models.py` 을 기반으로 CRUD, Create(Post 생성), Read(Post 한개 조회), Update(Post 업데이트), Delete(Post 삭제) + List(전체조회)를 구현하고, 테스트케이스 `Test.py`를 작성하는 과제입니다.
간단한 게시글을 작성할 수 있는 게시판기능을 구현하였습니다. 

> ### ▶ POST 전체 조회 List
> 이미지
> (url = 'post/') (view = index) (template = index.html) 
> `Post` 객체내의 데이터를 모두 나타낸다. 글 제목을 클릭해 해당 글의 **detail (READ 글 조회)** 로 이동이 가능하다.

> ### ▶ POST 생성 Create
> 이미지
> (url = 'post/create/') (view = post_create) (template = create.html)
> 알맞은 값을 입력후, 글작성 버튼을 클릭시 `Post` 객체가 생성되고, Post 전체 조회 화면으로 리디렉션된다.

> ### ▶ POST 조회 Read
> 이미지
> (url = 'post/<int:pk>/') (view = post_receive) (template = detail.html)
> id(Post의 pk)에 해당하는 `Post`의 내용을 확인할 수 있는 창이다.

> ### ▶ POST 업데이트 Update
> 이미지
> (url = 'post/update/<int:pk>/') (view = post_update) (template = update.html)
> id(Post의 pk)에 해당하는 `Post`의 내용을 수정할 수 있는 창이다. 수정 버튼을 클릭시 Post 전체 조회 화면으로 리디렉션된다.

> ### ▶ POST 삭제 Delete
> 이미지
> (url = 'post/delete/<int:pk>/') (view = post_delete)
> 해당 url로 이동시 id(Post의 pk)에 해당하는 `Post` 객체를 삭제한다. 삭제를 완료후 Post 전체 조회 화면으로 리디렉션된다.

***
#### TestCase