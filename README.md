# Midterm Image Processing Project

## Project Overview

This project implements various image processing effects on input images, including:

- Image Border
- Kaleidoscope/Kaleido Effect
- Linear Filtering
- Night Vision
- Oil Painting

The project is designed to run all effects automatically in a full pipeline on any new image.

## Tools and Technologies

- Programming Language: Python 3.14
- Libraries: OpenCV
- IDE: VSCode
- Version Control: GitHub

## System Features

- Full pipeline processes all images in the input_images/ folder
- Automatically skips already processed images
- Outputs saved in output_images/
- Any new image placed in input_images/ will be automatically processed by the full pipeline and saved in output_images/

## Project Structure

C:.
│ README.md
│ run_pipeline.py
│ tests/
│ output_images/
│ image_border/
│ kaleido_effect/
│ linear_filtering/
│ night_vision/
│ oil_painting/

## Running Tests

To run the full pipeline and all modules:

python tests/test_pipeline.py

- Full pipeline processes all input images and skips already processed ones
- Output images saved in output_images/
- Trying other type of image file

## Continuous Integration

- GitHub Actions can be configured to run automated tests on each push
- Ensures that the pipeline works correctly after updates

## DevOps Workflow

- Development of image processing effects in Python
- Version control using GitHub
- Testing done locally by the tester
- Full pipeline automation handled via run_pipeline.py
- CI/CD can be integrated for future automation

## Output

- All processed images are saved in the output_images/ folder
- Example output images:
  - Image Border Effect
  - Kaleidoscope Effect

(Replace example images with actual output images for your presentation)
