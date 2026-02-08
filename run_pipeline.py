import os
import cv2

# FIXED IMPORTS: Adjusted to match your folder structure (midterms/...)
from image_border.main import apply_border
from kaleido_effect.main import apply_kaleido
from linear_filtering.main import apply_linear
from night_vision.main import apply_night_vision
from oil_painting.main import apply_oil_painting

INPUT_DIR = 'input_images'
OUTPUT_DIR = 'output_images'
ALLOWED_EXT = ('.png', '.jpg', '.jpeg', '.webp')

def process_all():
    # 1. Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 2. Look for files in input folder
    files = os.listdir(INPUT_DIR)
    
    for filename in files:
        if filename.lower().endswith(ALLOWED_EXT):
            print(f"\nACCEPTED: Processing {filename}...")
            
            img_path = os.path.join(INPUT_DIR, filename)
            original_img = cv2.imread(img_path) # Load original once
            
            if original_img is None:
                print(f"ERROR: Could not read {filename}")
                continue

            try:
                # --- TECHNIQUE 1: Border ---
                res1 = apply_border(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"border_{filename}"), res1)

                # --- TECHNIQUE 2: Kaleido ---
                res2 = apply_kaleido(original_img) # Use original_img, not res1
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"kaleido_{filename}"), res2)

                # --- TECHNIQUE 3: Linear Filter ---
                res3 = apply_linear(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"linear_{filename}"), res3)

                # --- TECHNIQUE 4: Night Vision ---
                res4 = apply_night_vision(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"night_{filename}"), res4)

                # --- TECHNIQUE 5: Oil Painting ---
                res5 = apply_oil_painting(original_img)
                cv2.imwrite(os.path.join(OUTPUT_DIR, f"oil_{filename}"), res5)

            except Exception as e:
                print(f"ERROR processing {filename}: {e}")

        else:
            print(f"DENIED: Skipping non-image file {filename}")

if __name__ == "__main__":
    process_all()