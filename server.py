from flask import Flask, url_for, request, send_file
from werkzeug import secure_filename
import skimage.io
import io
import numpy as np
import cv2
import os
from flask import jsonify
from matplotlib.image import imread
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Uploads'
@app.route('/upload',methods =['POST'])
def upload():
    print("request recieved ")
    file = request.files['image']
    filename = secure_filename(file.filename)
    #Save image on the server
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #Read image for detection
    image = skimage.io.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(type(image))

    #Detect and save detected image on the server 
    print(filename)
    from runner import run
    result = run(image,filename)


   
    # img = imread(filename)
   
    # response= pd.Series(img).to_json(orient='values')
    # return send_file(filename)
    return send_file("Detected/"+filename)

    
if __name__ == '__main__':
    app.run()

