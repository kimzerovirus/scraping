# 파이썬 크롤러 만들기

## 파이썬 가상 환경 사용해 보기

### 가상 환경 만들기

```bash
mkdir venvs
cd venvs
python3 -m venv myproject
```

> 맥(Mac) 사용자는 python대신 python3 명령을 사용해야됨.

### 가상 환경 진입하기

```bash
# venv/myproject/bin 위치의 activate 실행
source activate
```

> 가상환경에서 벗어나려면 deactivate 해주면 됨.

**어떤 파이썬 환경이 실행되는지 확인하기**

```bash
(venv-project) $ which python
```

이제 마음껏 가상환경에 파이썬 패키지를 설치하면 된다

### PyCharm에 가상환경 세팅하기

![pycharm](/Users/zerovirus/Desktop/Code/scarping/pycharm.png)

### 파이썬 패키지 requirements 만드는 법

```bash
# pip freeze 이용하기
$ pip freeze > requirements.txt

# -r 옵션 이용하기
$ pip install -r requirements.txt
```

### 가상환경 위치에서 flask 실행하기

> 가상환경 진입후 -> flask app 실행 파일 위치에서 `flask run` 커맨드

기본적으로 flask 는 `app.py` 를 찾아서 실행하므로 커스텀하고 싶다면 `set FLASK_APP=` 명령어를 사용하여 파일명을 바꿀 수 있음 

개발모드 세팅 `set FLASK_DEBUG=true`