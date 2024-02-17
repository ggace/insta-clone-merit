
from flask import Flask, request   # flask 클래스를 가져온다.
import json

from controller import FeedController

app = Flask(__name__)     # 플라스크 객체를 생성한다. __name__은 현재 실행 중인 모듈 이름을 전달하는 것이다.

@app.route('/main')           # 기본서버 127.0.0.1:5000 뒤에 붙는 주소를 적어준다.
def index():              # 위의 주소를 호출 시 보여 줄 것을 함수로 작성해 준다. 중복되지 않도록만 적어주면된다.
    return "this is main page"

@app.route("/feeds/<action>", methods=["GET", "POST", "PUT", "DELETE"])
def feeds(action):
    if not ("options" in request.args):
        return "Fail: parameter whose name is 'options' is not existed."
    
    options = json.loads(request.args.get("options"))
    if(request.method == "GET"):
        return FeedController.feeds(action, options)
    else:
        return "hello"

if __name__ == '__main__':# 다른데서 부르면 실행하지 마라는 뜻이다.
    app.run(debug=True)