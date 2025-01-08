from flask import Flask
from flask_mysqldb import MySQL

import yaml 
from flask_smorest import Api
from posts_routes import create_posts_blueprint

app = Flask(__name__)
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

mysql = MySQL(app)

api = Api(app)
#api.register_blueprint()

# 만튼 페이지 나오게 만드는 라우트
from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")


if __name__ == "__main__":
    app.run(debug=True)