import cv2
import os

class cat_detection():

    def read_face_output(self, jpg_directory):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        img = cv2.imread(f'{jpg_directory}')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
        faces = cat_cascade.detectMultiScale(gray, 1.1, 3)
        if len(faces) > 0:
            return True
        else:
            return False