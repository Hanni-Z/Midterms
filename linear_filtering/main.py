import cv2
import numpy as np

def apply_linear(img):
    # Define the sharpening kernel (standard matrix for sharpening)
    kernel = np.array([[-1, -1, -1], 
                       [-1,  9, -1], 
                       [-1, -1, -1]])
    
    # Apply the filter
    # ddepth=-1 means the output image will have the same depth as the source
    dst = cv2.filter2D(img, -1, kernel)
    
    return dst