from flask import Flask
from flask_mysqldb import MySQL

import yaml 
from flask_smorest import Api
from posts_routes import create_posts_blueprint

app = Flask(__name__)
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
# 보안이슈로 db = yaml.safe_load(open('db.yaml')) 쓰느게 좋음

app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

# flask-smorest api 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

mysql = MySQL(app)

api = Api(app)
api.register_blueprint(create_posts_blueprint(mysql))

# 블로그관리 페이지
from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")


if __name__ == "__main__":
    app.run(debug=True)