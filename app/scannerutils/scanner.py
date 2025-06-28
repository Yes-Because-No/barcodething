import cv2 
from pyzbar.pyzbar import decode, Decoded
from typing import Callable

def findCodeStill(availableIds: list[str], img: cv2.typing.MatLike) -> Decoded:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decoded_objs: list[Decoded] = decode(img)
    for decoded in decoded_objs:
        if decoded.data.decode("utf-8") in availableIds:
            return decoded 
    raise TypeError("No barcode found, so no value can be returned")

def findFirstCode(availableIds: list[str], read: Callable[[], tuple[bool, cv2.typing.MatLike]]) -> Decoded:
    while 1:
        ret, img = read()
        if ret:
            try: 
                decoded: Decoded = findCodeStill(availableIds, img)
                return decoded
            except Exception as e:
                pass
            cv2.waitKey(10)
    raise TypeError("No barcode can be found in the video stream after breaking loop, so no value returned")

if __name__=="__main__":
    cam = cv2.VideoCapture(0)
    print(findFirstCode(["600101605"], cam.read).data.decode("utf-8"))

    while 1:
        ret, img = cam.read()

        if ret:
            dec = decode(img)
            for i in dec:
                x,y,w,h = i.rect
                cv2.rectangle(img, (x-10,y-10), (x+w+10, y+h+10), (255,255,120), 3)
                cv2.putText(img, i.type, (x,y+50+h), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
        cv2.imshow("img", img)
        cv2.waitKey(3)
