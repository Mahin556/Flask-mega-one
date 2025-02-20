from flask import Flask #class
from flask import render_template

app = Flask(__name__) #object

@app.route("/") #route - endpoint - page  #empty route
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)