from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def cv2_pipeline():
    return render_template('orange-cv2.html')

@app.route('/ai_pipeline')
def ai_pipeline():
    return render_template('orange-ai.html')

@app.route('/settings')
def settings():
    return render_template('orange-settings.html')



def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)
    
@app.route("/slider", methods=["POST"])
def slider():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        print(data)
    return "nothing"

@app.route("/dual_slider", methods=["POST"])
def dual_slider():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        print(data)
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


if __name__ == '__main__':
    app.run()