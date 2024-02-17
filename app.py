
from flask import Flask   # flask 클래스를 가져온다.

from MasterController import MainAPI

app = Flask(__name__)     # 플라스크 객체를 생성한다. __name__은 현재 실행 중인 모듈 이름을 전달하는 것이다.

apis = {
    "main": MainAPI
}

@app.route('/<api>')           # 기본서버 127.0.0.1:5000 뒤에 붙는 주소를 적어준다.
def index(api):              # 위의 주소를 호출 시 보여 줄 것을 함수로 작성해 준다. 중복되지 않도록만 적어주면된다.
    if(api in apis):
        return apis[api].execute()
    else:
        return "this page is not existed    "
    
if __name__ == '__main__':# 다른데서 부르면 실행하지 마라는 뜻이다.
    app.run(debug=True)