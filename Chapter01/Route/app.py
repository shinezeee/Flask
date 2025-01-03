from flask import Flask, request, Response

app = Flask(__name__) ## 서버를 만들어주는 코드
#  http://127.0.0.1:5000/

@app.route('/')
def home():
    return "Hello, This is Main Page"

@app.route('/about')
def about():
    return "Hello, This is About Page"


# 동적으로 URL을 생성할 수 있음
@app.route('/user/<username>')
def user_profile(username):
    return f"UserName : {username}"

@app.route('/user/<int:number>')  #>> int로 받아서 숫자만 받을 수 있음
def user_profile(number):
    return f"UserName : {number}"

# POST 방식으로 데이터를 받아오기
# (1) POSTMAN
# (2) requests 모듈

import requests # pip install requests
@app.route('/test')
def test():
    url = "http://127.0.0.1:5000/test"
    

if __name__ == "__main__":
    app.run()
    

    
  