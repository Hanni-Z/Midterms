# tests/test_pipeline.py
import subprocess
import os

def test_modules():
    modules = [
        "image_border",
        "kaleido_effect",
        "linear_filtering",
        "night_vision",
        "oil_painting"
    ]

    print("=== Testing individual modules ===\n")

    for module in modules:
        print(f"Testing {module}...")
        main_path = os.path.join(module, "main.py")
        
        if os.path.exists(main_path):
            result = subprocess.run(["python", main_path], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
        else:
            print(f"{main_path} not found!")
        print("-" * 30)

def test_full_pipeline():
    print("\n=== Testing full pipeline ===\n")
    pipeline_path = "run_pipeline.py"

    if os.path.exists(pipeline_path):
        result = subprocess.run(["python", pipeline_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
    else:
        print(f"{pipeline_path} not found!")

if __name__ == "__main__":
    test_modules()
    test_full_pipeline()
