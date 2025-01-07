from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User
from marshmallow import Schema, fields

# UserSchema 정의
class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # 읽기 전용 필드
    name = fields.Str(required=True)  # 필수 입력 필드
    email = fields.Str(required=True)  # 필수 입력 필드


user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/users')


# GET: /users - 사용자 목록 조회
@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        user_schema = UserSchema(many=True)  # 다수의 사용자 데이터를 직렬화
        return user_schema.dump(users)  # 직렬화된 데이터 반환

    def post(self):
        print("요청은 오는가?")
        user_data = request.json
        user_schema = UserSchema()  # 클라이언트 데이터 역직렬화
        user = user_schema.load(user_data)  # 역직렬화 후 User 객체 생성
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201

# GET, PUT, DELETE: /users/<int:user_id> - 개별 사용자 조회, 수정, 삭제
@user_blp.route('/<int:user_id>')
class Users(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        user_schema = UserSchema()  # 단일 사용자 데이터 직렬화
        return user_schema.dump(user)  # 직렬화된 사용자 데이터 반환

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json
        user_schema = UserSchema()  # 클라이언트 데이터 역직렬화
        updated_user = user_schema.load(user_data, instance=user, partial=True)  # 역직렬화 후 수정
        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
    
    
    
    
'''
왜 이렇게 해야 하는가?
	1.	요청/응답 데이터 관리: UserSchema는 클라이언트와 서버 간에 주고받는 데이터 형식을 관리하는 역할을 합니다. 이로 인해 데이터가 정확하게 포맷팅되고 유효성 검사도 자동으로 이루어집니다.
	2.	데이터 변환 일관성 유지: UserSchema를 사용하면, 직렬화 및 역직렬화가 일관되게 이루어져 코드의 중복을 줄이고, 추후에 데이터 포맷을 바꾸더라도 수정이 쉬워집니다.
	3.	에러 처리: UserSchema에서 필수 필드를 정의하고 검증을 설정할 수 있기 때문에, 클라이언트가 잘못된 데이터를 보낼 경우 에러를 쉽게 처리할 수 있습니다.

결론:

UserSchema를 추가하면 데이터 처리가 더 일관성 있고, 유지보수가 쉬워집니다. 클라이언트와 서버 간의 데이터 전송 과정에서 오류를 줄이고, 각 요청에 대한 처리도 명확해집니다.
'''