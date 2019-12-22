from flask import Flask, render_template, request, Response, jsonify
from Camera import Camera
from CVProcessing import tapePos
import json
import cv2
from read_and_write import read_json, write_json, json_parse
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"


cam = Camera(0)
CVProcessor = tapePos(cam)



@app.route('/')
def cv2_pipeline():
    # default values being passed in 


    #range and base values
    dual_slider = read_json('dual_slider')

    
    # single sliders default
    slider = read_json('slider')
    
    
    # dropdown defaults WIP

    return render_template('orange-cv2.html', dual_slider = dual_slider, slider=slider)

@app.route('/ai_pipeline')
def ai_pipeline():
    return render_template('orange-ai.html')

@app.route('/settings')
def settings():
    return render_template('orange-settings.html')




    
@app.route("/slider", methods=["POST"])
def slider():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        for key in data:
            value = data[key]

            print(key, value)
            write_json('slider', key, value)
    return "nothing"

@app.route("/dual_slider", methods=["POST"])
def dual_slider():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        for key in data:
            value = data[key]
            print(key, value)
            
            if key == 'hue':
                CVProcessor.set_hue(value)
            elif key == 'saturation':
                CVProcessor.set_saturation(value)
            elif key == 'value':
                CVProcessor.set_value(value)

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
        for key in data:
            value = data[key]

            if key == 'eyedropper':
                x = value[0]
                y = value[1]
                CVProcessor.generate_eyedropper(x, y)
                
            write_json('camera', key, value)
    return jsonify({'hue' : CVProcessor.hue, 'saturation' : CVProcessor.saturation, 'value' : CVProcessor.value})



# Camera test

@app.route('/cv')
def cv():
    return render_template('cv.html')



@app.route('/video_feed')
def video_feed():
    return Response(VideoCamera(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def VideoCamera():
    for img,mask,boxes in CVProcessor.process():
        
        for box in boxes:
            cv2.drawContours(mask,[box],0,(0,127,255),2)
        
        ret, jpeg = cv2.imencode('.jpg', mask)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    


if __name__ == '__main__':
    app.run()