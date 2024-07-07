from flask import Flask, request, render_template, redirect, url_for
import cv2 as cv
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        angle = process_image(file_path)
        return render_template('result.html', angle=angle)
    
    return redirect(request.url)

def process_image(file_path):
    image = cv.imread(file_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in faces:
        eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)
        index = 0
        eye_1 = [None, None, None, None]
        eye_2 = [None, None, None, None]
        
        for (ex, ey, ew, eh) in eyes:
            if index == 0:
                eye_1 = [ex, ey, ew, eh]
            elif index == 1:
                eye_2 = [ex, ey, ew, eh]
            index += 1
        
        if (eye_1[0] is not None) and (eye_2[0] is not None):
            if eye_1[0] < eye_2[0]:
                left_eye = eye_1
                right_eye = eye_2
            else:
                left_eye = eye_2
                right_eye = eye_1

            left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
            right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))

            left_eye_x = left_eye_center[0]
            left_eye_y = left_eye_center[1]
            right_eye_x = right_eye_center[0]
            right_eye_y = right_eye_center[1]

            delta_x = right_eye_x - left_eye_x
            delta_y = right_eye_y - left_eye_y

            angle = np.arctan(delta_y / delta_x) * 180 / np.pi
            return round(angle, 2)
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
