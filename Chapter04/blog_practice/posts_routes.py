from flask import request, jsonify
from flask_smorest import Blueprint

def create_posts_blueprint(mysql) :                             # 블루프린트 설명
    posts_blp = Blueprint ('posts',__name__,url_prefix='/posts',description="posts api")  


    @posts_blp.route('/', methods={'GET',"POST"})
    def posts() :
        cursor = mysql.connection.cursor()
        
        # 게시글 조회하기
        if request.method == "GET" :
            sql = "selete * from posts"
            cursor.execute(sql)
            posts = cursor.fetchall() # 모든 목록 가져오기
            cursor.close()
            post_list = []
            
            for post in posts :
                post_list.append (
                    {
                        "id" : post[0],
                        "title" : post[1],
                        "content" : post[2],
                    }
                )
            return jsonify(post_list)
        # 특정 게시글 조회하기 
        
        # 게시글 생성하기
        
        # 게시글 수정하기
        
        # 게시글 삭제하기