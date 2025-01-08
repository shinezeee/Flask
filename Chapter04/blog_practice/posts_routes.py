from flask import request, jsonify
from flask_smorest import Blueprint ,abort

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

        # 게시글 생성하기
        if request.method == "POST":
            title = request.json.get ("title")
            content = request.json.get("content")
            
            if not title or not content :
                abort(400, message= "Title or content is missing.")
            
            sql = "INSERT INTO posts(title,content) VALUES(%s,%s)"
            cursor.execute(sql,(title,content))
            mysql.connection.commit()
            
            return jsonify({"message" : "Success"}),201
        
        
    @posts_blp.route('/<int:id>', methords = ["GET","PUT","DELETE"])
    def post(id) :
        cursor = mysql.connection.cursor()
        # 특정 게시글 조회하기 
        if request.method == "GET":
            sql = f"SELECT * FROM posts WHERE id={id}" 
            cursor.execute(sql)
            post = cursor.fetchone() # 결과중 첫번째행
            
            if not post : # 없으면 404 에러코드
                abort (404, message = "Post not found.")
                
            return {
                "id" : post[0],
                "title" : post[1],
                "content" : post[2],
                 }
        # 게시글 수정
        if request.method == "PUT":
            title = request.json.get("title")
            content = request.json.get("content")
            
            if not title or not content : # 없으면 에러코드
                abort (404, message = "Tilte or Content not found.")
            
            # 게시물 불러오기    
            sql = "SELETE * FROM posts WHERE id =%s"
            cursor.execute(sql,(id))
            post = cursor.fetchone()
            
            if not post : # 없으면 404 에러코드
                abort (404, message = "Post not found.")
            
            # 게시물 수정하기
            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql,(title,content,id))
            mysql.connetion.commit()
            
            return jsonify({"message":"Sussessfully Updated Title & Content."})
        
        # 게시물 삭제
        if request.method == "DELETE" :
            # 게시물 불러오기    
            sql = "SELETE * FROM posts WHERE id =%s"
            cursor.execute(sql,(id))
            post = cursor.fetchone()
            
            if not post : # 없으면 404 에러코드
                abort (404, message = "Post not found.")
                
        sql = "DELETE FROM posts WHERE id =%s"
        cursor.execute(sql,(id))
        mysql.connetion.commit()
        
        return jsonify({"message":"Sussessfully Deleted Post."})

    return posts_blp