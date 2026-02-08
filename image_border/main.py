import cv2

def apply_border(img):
    # Logic extracted from your 'image_frame.ipynb'
    
    # 1. Inner Border (Gold/Yellow)
    inner_thickness = 5
    inner_color = [0, 215, 255] # BGR Color from your code
    
    step_1_img = cv2.copyMakeBorder(
        img,
        inner_thickness, inner_thickness, inner_thickness, inner_thickness,
        cv2.BORDER_CONSTANT,
        value=inner_color
    )

    # 2. Outer Border (Blue-Grey)
    outer_thickness = 40
    outer_color = [92, 133, 165] # BGR Color from your code

    fancy_frame = cv2.copyMakeBorder(
        step_1_img, 
        outer_thickness, outer_thickness, outer_thickness, outer_thickness,
        cv2.BORDER_CONSTANT,
        value=outer_color
    )
    
    # 3. Return the result (Do NOT save or show it here)
    return fancy_frame