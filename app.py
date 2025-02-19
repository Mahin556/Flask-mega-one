from flask import Flask #class

app = Flask(__name__) #object

@app.route("/") #route - endpoint - page  #empty route
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)