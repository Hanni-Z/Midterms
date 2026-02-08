import os
import cv2
from image_border.main import apply_border
from kaleido_effect.main import apply_kaleido
from linear_filtering.main import apply_linear
from night_vision.main import apply_night_vision
from oil_painting.main import apply_oil_painting

INPUT_DIR = 'input_images'
OUTPUT_DIR = 'output_images'
ALLOWED_EXT = ('.png', '.jpg', '.jpeg', '.webp')

def process_all():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = os.listdir(INPUT_DIR)
    
    for filename in files:
        if filename.lower().endswith(ALLOWED_EXT):
            
            check_path = os.path.join(OUTPUT_DIR, f"border_{filename}")
            if os.path.exists(check_path):
                print(f"SKIPPING: {filename} (Already processed)")
                continue

            print(f"\nACCEPTED: Processing {filename}...")
            img_path = os.path.join(INPUT_DIR, filename)
            original_img = cv2.imread(img_path)
            
            if original_img is None:
                continue

            try:
                # Apply techniques and save
                res1 = apply_border(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"border_{filename}"), res1)

                res2 = apply_kaleido(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"kaleido_{filename}"), res2)

                res3 = apply_linear(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"linear_{filename}"), res3)

                res4 = apply_night_vision(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"night_{filename}"), res4)

                res5 = apply_oil_painting(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"oil_{filename}"), res5)

                print(f"SUCCESS: Generated 5 images for {filename}")

            except Exception as e:
                print(f"ERROR processing {filename}: {e}")

if __name__ == "__main__":
    process_all()