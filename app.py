from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("top.html") 

@app.route("/list/")
def list():
    return render_template("list.html")  

@app.route("/list/<name>")
def list_name(name):
    return f'List, {name}'

@app.route("/detail")
def detail():
    return render_template("detail.html") 

if __name__ == '__main__':
       app.run(debug=True)
