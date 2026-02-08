import os
import cv2 # Assuming you use OpenCV, change to PIL if needed
# Import your 5 techniques (After renaming folders to remove spaces)
# You might need to adjust these imports based on your actual file names inside the folders
from image_border import main as step1
from kaleido_effect import main as step2
from linear_filtering import main as step3
from night_vision import main as step4
from oil_painting import main as step5

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
        # ACCEPT/DENY LOGIC: Check extension
        if filename.lower().endswith(ALLOWED_EXT):
            print(f"ACCEPTED: Processing {filename}...")
            
            img_path = os.path.join(INPUT_DIR, filename)
            
            # Read the image
            img = cv2.imread(img_path)
            
            if img is None:
                print(f"ERROR: Could not read {filename}")
                continue

            # --- RUN THE 5 TECHNIQUES ---
            # We assume your scripts have a function that takes an image and returns a processed one.
            # You will need to adapt this part to match your actual function names.
            
            try:
                # Example: Chaining them together
                res1 = step1.apply_border(img)
                res2 = step2.apply_kaleido(res1)
                res3 = step3.apply_linear(res2)
                res4 = step4.apply_night_vision(res3)
                final_res = step5.apply_oil_painting(res4)

                # Save final result
                save_path = os.path.join(OUTPUT_DIR, f"processed_{filename}")
                cv2.imwrite(save_path, final_res)
                print(f"SUCCESS: Saved to {save_path}")
                
            except Exception as e:
                print(f"ERROR processing {filename}: {e}")

        else:
            print(f"DENIED: Skipping non-image file {filename}")

if __name__ == "__main__":
    process_all()