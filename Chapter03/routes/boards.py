from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# 게시판 
@board_blp.route('/')
class BoardList(MethodView):
    # 게시판 목록 가져오기
    def get(self):
        boards = Board.query.all()
        return jsonify([{"user_id": board.user_id, 
                         "id": board.id,
                         "title": board.title, "content": board.content, "author": board.author.name} for board in boards])

    # 게시글 생성
    def post(self):
        data = request.json
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_board)
        db.session.commit()
        return jsonify({"message": "Board created"}), 201

# 특정 게시글 
@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    # 특정 게시글 상세정보 조회
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})

    # 특정 게시글 수정
    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})

    # 특정 게시글 삭제
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})