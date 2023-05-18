from flask import Flask
from flask import render_template
from flask import request


# __name__ : 모듈 명(->test)
app = Flask(__name__)

name = "Collin Powell"
id = 20180233
dept = "정보통신공학"
grade = 4
age = 26
hp = "010-1234-5678"
face_img = "../static/face_images/Colin Powell.jpg"


@app.route('/')
def index():
    return render_template("index.html", var1=name, var2=id, var3=dept, var4=grade, var5=age, var6=hp, var7=face_img)

# @app.route('/data', method=['POST'])
# def dataGet():
#     data = request.json
#     return render_template("index.html", var1=data['key'], var2=id, var3=dept, var4=grade, var5=age, var6=hp, var7=face_img)

if __name__ == '__main__':
    app.debug = True
    app.run()