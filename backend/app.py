from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)
    
@app.route("/test", methods=["POST"])
def test():
    clicked=None
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        print(data['data'])
    return "nothing"

@app.route("/dropdown", methods=["POST"])
def dropdown():
    clicked=None
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        print(data['dropdown'])
    return "nothing"

@app.route('/button')
def button():
    print('button pressed')
    return "Nothing"


    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()