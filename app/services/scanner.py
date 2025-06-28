import cv2 
from pyzbar.pyzbar import decode, Decoded

class Camera:
    def __init__(self, loc:str):
        self.cam = cv2.VideoCapture(loc)

    