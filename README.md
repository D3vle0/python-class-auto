
# <img src="./img/python.svg" height="20px"> python-class-auto

여러분의 자료구조B 시간을 행복하게 해줄 프로그램!  
작성한 코드를 dimigo.biz 에 자동으로 올려줍니다.  

## :satellite: 설치
```sh
git clone https://github.com/D3vle0/python-class-auto.git
cd python-class-auto
```
```py
pip install selenium
```
## :wrench: credentials.json
```json
{
"email":"",
"pw":"",
"std":"",
"proj_folder":"",
"chromedriver_path":""
}
```
`email` : dimigo.biz 로그인에 사용되는 이메일  
`pw`: 비밀번호  
`std`: 학번 이름  
`proj_folder`: 업로드할 파이썬 파일 폴더의 경로  
`chromedriver_path`: 크롬드라이버 파일 경로  
  
example  
```json
{
"email":"",
"pw":"",
"std":"1423 배상혁",
"proj_folder":"/home/devleo/OneDrive/프로젝트/programmingB/",
"chromedriver_path":"./chromedriver"
}
```

## :rocket: 실행
```sh
python3 app.py
```

## :exclamation: 주의사항
수업시간에 작성한 파이썬 파일명은 반드시 오늘 날짜 (mmdd) 형태로 저장합니다.  
ex: `1013.py`
