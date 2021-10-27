# [원티드] 백엔드 프리온보딩 선발 과제 

- 지원자 : 김주현

- 교육 신청 사이트: https://www.wanted.co.kr/wd/81239?from=resume


## 적용 기술

- Python
- Django
- Sqlite3
- JWT
- bcrypt

## 구현 방법 및 기능

- Python언어를 기반으로 Django Framework를 활용한 게시판 CRUD API 구현하기

- 유저 생성, 인가, 인증 기능 적용
- core앱
  - 생성 및 수정 이력관리를 위한 추상화 모델 작성
- users앱
  	- 회원가입을 통해 bcrypt로 비밀번호 암호화
  	- 로그인을 통해 JWT 토큰 생성
  	- 사용자별 인가를 위해 decorators.py생성 후 login_decorator 부여

- postings앱
  - 게시물 작성 및 조회 기능 구현
  - 게시물 조회 pagination 구현
  - 게시물 상세내용 조회, 수정, 삭제 기능 구현



## API 명세

#### 1. POST 회원가입

Request

```
curl POST http://localhost:8000/users/signup
{
  "username": "jhjh2002",
  "password": "abcd!e12",
  "name": "kimjuhyun",
  "email": "jhjh2002@naver.com"
}
```

Response

```
-D {
    "username" : "jhjh2002",
    "password" : "abcd!e12",
    "name" : "kimjuhyun",
    "email" : "jhjh2002@naver.com"
}
```

회원가입 성공

```
{
  "message": "SUCCESS"
}
```

#### 2. POST 로그인

Request

```
curl POST http://localhost:8000/users/signin
{
  "email": "jhjh2002@naver.com",
  "password": "abcd!e12"
}
```

Response

```
-H 'Authorization: $2b$12$hc1LZHJLP6nnB3z4B.wfNO/xLr9x4dHHhCsVgB3RrsFzngVaglCzu' \
-D {
    "email" : "jhjh2002@naver.com",
    "password" : "abcd!e12"
}
```

#### 3. POST 게시물 등록

Request

```
curl POST http://localhost:8000/postings
{
  "title": "dddd",
  "content": "awecio"
}
```

Response

```
-H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30._0ehvwVmxk3KfX1zJyqV5nAWs-cfUA6iEN-qgpVl5g4' 
-D {
    "title" : "dddd",
    "content" : "awecio"
}
```

게시물 등록 성공

```
{
    "data": "SUCCESS"
}
```

#### 4. Get 게시물 조회

Request

```
curl GET http://localhost:8000/postings?limit5&offset=0
```

Response

```
{
    "count": 6,
    "data": [
        {
            "post_id": 3,
            "user": "kimjuhyun",
            "title": "dadd",
            "created_at": "2021-10-27T05:59:25.120",
            "updated_at": "2021-10-27T06:00:30.885"
        },
        {
            "post_id": 4,
            "user": "kimjuhyun",
            "title": "dddd",
            "created_at": "2021-10-27T06:54:27.714",
            "updated_at": "2021-10-27T06:54:27.714"
        },
        {
            "post_id": 5,
            "user": "kimjuhyun",
            "title": "웹툰",
            "created_at": "2021-10-27T06:56:29.718",
            "updated_at": "2021-10-27T06:57:32.932"
        },
        {
            "post_id": 6,
            "user": "kimjuhyun",
            "title": "웹툰",
            "created_at": "2021-10-27T06:56:54.610",
            "updated_at": "2021-10-27T06:56:54.610"
        },
        {
            "post_id": 7,
            "user": "kimjuhyun",
            "title": "던킨",
            "created_at": "2021-10-27T06:59:47.083",
            "updated_at": "2021-10-27T06:59:47.083"
        },
        {
            "post_id": 8,
            "user": "kimjuhyun",
            "title": "던킨",
            "created_at": "2021-10-27T07:00:15.594",
            "updated_at": "2021-10-27T07:00:15.594"
        }
    ]
}
```

게시물 조회 성공

```
{
  "data": "SUCCESS"
}
```

#### 4. Get 게시물 상세조회

Request

```
curl GET 'http://localhost:8000/postings/3'
```

Response

```
{
  "data": {
    "post_id": 3,
    "user": "kimjuhyun",
    "title": "dddd",
    "content": "awecio",
    "created_at": "2021-10-27T05:59:25.120",
    "updated_at": "2021-10-27T05:59:25.120"
  }
}
```

#### 5. PATCH 게시물 수정

Request

```
curl PATCH http://localhost:8000/postings/3
{
  "title": "dadd",
  "content": "aaacio"
}
```

Response

```
-H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30._0ehvwVmxk3KfX1zJyqV5nAWs-cfUA6iEN-qgpVl5g4' 
-D {
    "title" : "dddd",
    "content" : "awecio"
}
```

게시물 수정 성공

```
{
    "message": "UPDATED"
}
```



#### 6. DELETE 게시물 삭제

Request

```
curl http://localhost:8000/postings/2
```

Response

```
-H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.WKpk79OnEXW1TphFDi5oVQvFx9ODT7L5LboX_mmZ6L8'

```

게시물 삭제 성공
```
{
    "message": "DELETED"
}
```
