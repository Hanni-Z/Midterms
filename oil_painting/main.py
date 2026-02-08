import cv2

def apply_oil_painting(img):
    # Standard parameters: 7, 1
    # 7 is the size of the pixel neighborhood
    # 1 is the dynamic ratio
    try:
        dst = cv2.xphoto.oilPainting(img, 7, 1)
    except AttributeError:
        # Fallback if xphoto is not installed on the server
        dst = cv2.bilateralFilter(img, 9, 75, 75)
        
    return dst