import cv2
import numpy as np

def apply_kaleido(img):
    # 1. Get the size of the image
    h, w = img.shape[:2]
    
    # 2. Calculate the center points
    cx, cy = w // 2, h // 2
    
    # 3. Crop the Top-Left corner (This will be our "seed" image)
    # We ignore the rest of the image to create perfect symmetry
    top_left = img[0:cy, 0:cx]
    
    # 4. Create the Top-Right by mirroring Top-Left horizontally
    top_right = cv2.flip(top_left, 1) # 1 = Horizontal Flip
    
    # 5. Combine them to create the full Top Half
    top_half = np.hstack((top_left, top_right))
    
    # 6. Create the Bottom Half by mirroring the Top Half vertically
    bottom_half = cv2.flip(top_half, 0) # 0 = Vertical Flip
    
    # 7. Combine Top and Bottom to make the full Kaleidoscope
    final_img = np.vstack((top_half, bottom_half))
    
    return final_img