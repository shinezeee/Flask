# model -> table 생성
# 게시글 - board
# 사용자 - user

from db import db

class User(db.Model) :
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')
    # ㄴ> 양방향 관계
    address = db.Column(db.String(120), unique=True, nullable=False)

class Board(db.Model) :
    __tablename__ = "boards"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    author = db.relationship('User', back_populates='boards')
    
    
    
## user 모델의 boards : 사용자가 작성한 모든게시물(board)들의 목록을 나타냄.
## board 모델의 author : 특정 게시물을 작성한 사용자 (user)를 나타냄