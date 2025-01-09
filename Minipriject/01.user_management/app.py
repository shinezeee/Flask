from flask import Flask ,render_template ,request,redirect,url_for

app=Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...

# 사용자 추가
@app.route('/add', methods= ["GET","POST"]) # 사용자추가패이지 get/데이터 받아 새로추가 post
def add_user() :
    if request.method == "POST" :
        username = request.form['username'] #폼에서 username, name 가져오기
        name = request.form['name']
        users.append({'username': username , 'name':name}) #users 리스트에 추가
        return redirect(url_for('index')) 
    return render_template('add_user.html')

# 사용자 정보 수정
@app.route('/edit/<username>',methods =["GET","POST"]) # 특정사용자정보 get/ 수정된사용자 정보저장 post
def edit_user(username):
    # 특정 사용자 정보 찾기
    user = next((user for user in users if user["username"] == username), None)
    #next(a,b) : 제너레이터에서 첫번째 일치항목 반환하는 함수, a가 없으면 b 반환
    
    # 사용자 없으면 목록페이지로 
    if not user : 
        return redirect(url_for('intex'))
    # 수정 데이터 제출 시
    if request.method == "POST" :
        user["name"] = request.form["name"] # 값 업뎃
        return redirect(url_for('index')) # 사용자 목록 페이지로 
    return render_template('edit_user.html', user=user) # 페이지에 사용자데이터 전달
        
    
# 사용자 삭제
@app.route('/delete/<username>')
def delete_user(username):
    global users # users 리스트 수정해야 하므로 글로벌
    users = [user for user in users if user["username"] != username]
    # ㄴ> 삭제하려고 입력한 사용자이름 제외하고 리스트에 표시
    return redirect(url_for('index'))

    

if __name__ == '__main__':
    app.run(debug=True) 
    # 디버그가 트루면 코드 변셩시 자동으로 서버 재시작
