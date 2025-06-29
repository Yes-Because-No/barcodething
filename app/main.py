from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.services.scanner import Camera, CameraCallbacks
import cv2
import asyncio
import numpy as np

cam = Camera(0)

app = FastAPI()
        

@app.get("/")
def main():
    def combo(frame):
        ret, decoded, img = CameraCallbacks.scan_for_barcode(frame)
        if ret:
            print(decoded.data.decode("utf-8"))
            img = np.full((480,640, 3), (0,255,0))
        return CameraCallbacks.to_web_streamable(img)
        
    return StreamingResponse(cam.gen_frames(combo), media_type="multipart/x-mixed-replace; boundary=frame")


