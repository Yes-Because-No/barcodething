import cv2 
from pyzbar.pyzbar import decode, Decoded
import asyncio 
import threading
from typing import AsyncGenerator, TypeVar, Callable

T = TypeVar("T")

#Camera class based on https://github.com/god233012yamil/Building-a-FastAPI-Web-Server-to-Stream-Video-from-Camera/

class Camera:
    def __init__(self, loc:int|str):
        self.cam = cv2.VideoCapture(loc)
        self.lock = threading.Lock()

    def release(self):
        with self.lock:
            if self.cam.isOpened():
                self.cam.release()
    
    def get_frame(self, callback: Callable[[cv2.typing.MatLike], T]) -> T:
        with self.lock:
            ret, img = self.cam.read()

            return callback(img)
        
    async def gen_frames(self, callback: Callable[[cv2.typing.MatLike], T])-> AsyncGenerator[T, None]:
        try:
            while True:
                frame = self.get_frame(callback)
                yield frame
                cv2.waitKey(0)
                await asyncio.sleep(0)
        except (asyncio.CancelledError, GeneratorExit):
            print("Stopped generating frames")
        finally:
            print("Frame generator exited")
                

class CameraCallbacks:
    @staticmethod 
    def frame_as_cv2_matlike(frame:cv2.typing.MatLike)-> cv2.typing.MatLike:
        return frame

    @staticmethod 
    def scan_for_barcode(frame: cv2.typing.MatLike)-> tuple[bool, Decoded, cv2.typing.MatLike]:
        nframe = frame
        nframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objs = decode(nframe)
        
        return (True, decoded_objs[0], frame) if decoded_objs else (False, Decoded(
            data=None,
            type=None,
            rect=None,
            polygon=None,
            quality=None,
            orientation=None
        ), frame)


