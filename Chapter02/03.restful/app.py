from flask import Flask , request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

items = [] # 리스트 저장

class Item (Resource):
    # 특정 아이템 조회
    def get(self,name):
        for item in items :
            if item['name'] == name :
                return item
            return {"message": "Item not found"}, 404 
   
    # 새 아이템 추가
    def post(self,name):
        for item in items :
            # 이미 있다면 
            if item ['name'] == name :
                return {'message':f"An item with name '{name}' already exist."},400
            
        data = request.get_json()
            
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        
        return new_item, 201
    
    # 아이템 업데이트
    def put(self,name):
        data = request.get_json()
        
        for item in items :
            if item ['name'] == name :
                item['price'] == data['price']
                return item

        # 업데이트 하고자 하는 아이템 데이터가 없다면 추가한다
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        return new_item
    
    # 아이템 삭제
    def deletd(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        
        
api.add_resource(Item,'/item/<string:name>') #  경로추가

if __name__ == '__main__':
    app.run(debug=True)