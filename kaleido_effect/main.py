import cv2
import numpy as np

def apply_kaleido(img):
    rows, cols = img.shape[:2]
    
    # Logic: Rotate the image 45 degrees relative to the center
    # This creates the "Kaleido" shifting effect
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    
    return dst