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
                print(decoded.data)
                return decoded
            except Exception as e:
                pass
            cv2.waitKey(10)
    raise TypeError("No barcode can be found in the video stream after breaking loop, so no value returned")

