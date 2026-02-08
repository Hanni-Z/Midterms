import cv2
import numpy as np

def apply_night_vision(img):
    # 1. Split into Blue, Green, Red channels
    b, g, r = cv2.split(img)
    
    # 2. Night vision is monochromatic Green.
    # We create an empty black channel for Blue and Red.
    zeros = np.zeros(img.shape[:2], dtype="uint8")
    
    # 3. Merge them back: (Blue=0, Green=Original Green, Red=0)
    # We also multiply 'g' by 1.5 to simulate the "brightening" of night goggles
    enhanced_g = cv2.convertScaleAbs(g, alpha=1.5, beta=0)
    
    dst = cv2.merge([zeros, enhanced_g, zeros])
    
    return dst