
from flask import Flask, request   # flask 클래스를 가져온다.
import json

from controller import FeedController, UserController

app = Flask(__name__)     # 플라스크 객체를 생성한다. __name__은 현재 실행 중인 모듈 이름을 전달하는 것이다.

@app.route('/main')           # 기본서버 127.0.0.1:5000 뒤에 붙는 주소를 적어준다.
def index():              # 위의 주소를 호출 시 보여 줄 것을 함수로 작성해 준다. 중복되지 않도록만 적어주면된다.
    return "this is main page"

@app.route("/feeds/<action>", methods=["GET", "POST", "PUT", "DELETE"])
def feeds(action):
    if not ("options" in request.args):
        return "Fail: parameter whose name is 'options' is not existed."
    
    options = json.loads(request.args.get("options"))
    if(request.method == "GET"): #조회
        return FeedController.get_feeds(action, options)
    elif(request.method == "POST"): #추가
        return FeedController.post_feeds(action, options)
    elif(request.method == "PUT"): #수정
        return FeedController.put_feeds(action, options)
    elif(request.method == "DELETE"): #삭제
        return FeedController.delete_feeds(action, options)
    else:
        return "Fail: this method is not available to access"

@app.route("/users/<action>", methods=["GET", 'POST', 'PUT','DELETE'])
def users(action):
    if not ("options" in request.args):
        return "Fail: parameter whose name is 'options' is not existed."
    
    options = json.loads(request.args.get("options"))
    if(request.method == "GET"): #로그인
        return UserController.get_users(action, options)
    elif(request.method == "POST"): #회원가입
        return UserController.post_users(action, options)
    elif(request.method == "PUT"): #회원정보 수정
        return UserController.put_users(action, options)
    elif(request.method == "DELETE"): #회원 삭제
        return UserController.delete_users(action, options)
    else:
        return "Fail: this method is not available to access"

if __name__ == '__main__':# 다른데서 부르면 실행하지 마라는 뜻이다.
    app.run(host="0.0.0.0", port=5000, debug=True)