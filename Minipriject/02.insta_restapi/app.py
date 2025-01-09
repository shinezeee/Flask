from flask import Flask, request, render_template ,jsonify

app = Flask (__name__)

users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

## 사용자 조회
# --/users 경로에 GET 요청을 보내면, 모든 사용자의 목록을 JSON 형태로 반환
@app.get('/users')
def view_users():
    return {"users": users}

## 사용자 생성
# --/users 경로에 POST 요청을 보내면, 새로운 사용자를 생성하고, 생성된 사용자 정보를 JSON 형태로 반환
# (각 사용자는 고유한 username과 초기 게시물 목록을 가져야 합니다.)
@app.post("/users")
def create_user():
    request_data = request.get_json() # 클라이언트가 보낸 json 데이터
    #새 유저 생성
    new_user = {"username":request_data["username"], "posts" : [{"title":"New Post","likes" :0}]}
    users.append(new_user) # 사용자리스트에 추가
    return new_user, 201

## 게시물 추가
# --/users/post/<username> 경로에 POST 요청을 보내면, 
# 지정된 사용자의 게시물 목록에 새 게시물을 추가하고, 추가된 게시물 정보를 JSON 형태로 반환
@app.post('/users/post/<username>')
def add_post(username):
    request_data = request.get_json()
    for user in users : # 사용자 찾기
        if user["username"] == username :
            new_post = {'title': request_data['title'], 'likes':request_data['likes']}
            user["post"].append(new_post) # 사용자 게시물 리스트에 추가
            return new_post
    # 사용자 없으면 오류 반환
    return {"message": "User not found"}, 404

## 사용자별 게시물 조회
# --/users/post/<username> 경로에 GET 요청을 보내면, 지정된 사용자의 모든 게시물을 JSON 형태로 반환
@app.get('/users/post/<username>')
def view_user_posts(username):
    # 사용자 찾기 
    for user in users :
        if user ["username"] == username:
            return {"post":user["posts"]} # 사용자 있으면 게시물 반환
    # 사용자 없으면 오류 반환
    return {"message": "User not found"}, 404
    
## 특정 게시물 좋아요 수 증가
# --/users/post/like/<username>/<title> 경로에 PUT 요청을 보내면, 지정된 사용자의 특정 게시물의 좋아요 수를 1 증가시키고, 
# 업데이트된 게시물 정보를 JSON 형태로 반환해야 합니다.
@app.put('/users/post/like/<username>/<title>')
def post_like (username,title) :
    # 사용자 찾기 
    for user in users :
        if user ["username"] == username: # 있으면
            # 게시물 찾기
            for post in user["posts"] : 
                if post ["title"] == title : #게시물 있으면
                    post ["likes"] += 1 # 좋아요수 증가
                    return{
                        "title": post["title"],
                        "likes": post["likes"]
                    }# 값 반영 
            #게시물 없으면 오류 반환
            return {"message": "Post not found"}, 404            
    # 사용자 없으면 오류 반환
    return {"message": "User not found"}, 404
    
## 사용자 삭제
# --/users/<username> 경로에 DELETE 요청을 보내면, 해당 사용자를 삭제하고, 
# 삭제되었다는 메시지를 JSON 형태로 반환
@app.delete('/users/<username>')
def delete_user (username):
    global users
    users = [user for user in users if user["username"] !=username]
    return {"message": "User deleted"}, 200 # 성공시완료 메세지 코드 반환

if __name__ == '__main__':
    app.run(debug=True)