from flask import Flask, render_template, request, Response
from camera import VideoCamera
import json

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def cv2_pipeline():
    # default values being passed in 


    #range and base values
    dual_slider = {'hue': [[0, 255], [30, 200]],  
                    'saturation': [[0, 255], [30, 200]], 
                    'value': [[0, 255], [30, 200]], 
                    'target': [[0, 255], [30, 200]], 
                    'fullness': [[0, 255], [30, 200]], 
                    'aspect': [[0, 255], [30, 200]]}


    # single sliders default
    slider = {'exposure': 211,  
                    'white_balance': 213, 
                    'erosion_steps': 214, 
                    'dilation_steps': 215, }
    
    
    # dropdown defaults WIP
    dropdown = {
        'orientation' : 'normal'

    }


    return render_template('orange-cv2.html', dual_slider = dual_slider, slider=slider)

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
        print(data)
    return "nothing"

@app.route('/button')
def button():
    print('button pressed')
    return "Nothing"





@app.route("/camera", methods=["POST"])
def camera():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        print(data)
    return "nothing"



# Camera test

@app.route('/cv')
def cv():
    return render_template('cv.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run()