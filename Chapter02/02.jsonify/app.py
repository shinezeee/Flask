from flask import Flask, jsonify

app = Flask(__name__)
#--- GET ---
# 1. 전체 게시글 불러오기
@app.route('/api/v1/feeds', methods = ['GET'])
def show_all_feeds():
    data = {
        'result' :'success','data':{"feed1":"data1","feed2":"data2"} 
        }
    return data

# 2. 특정 게시글 불러오기
@app.route('/api/v1/feeds/<int:feed_id>', methods =['GET'])
def show_one_feed(feed_id):
    print (feed_id)
    data = {'result' :'success','data':{"feed1":"data1"}}
    return data

#--- POST ---
# 1. 게시글 작성
@app.route('/api/v1/feeds',methods =["POST"])
def create():
    return