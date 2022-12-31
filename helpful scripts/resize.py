# AUTHOR: YASH S
# This script resizes all the dataset images to 512x512 resolutions. Originally used Pillow but rewrote to opencv-python for efficiency

import os
import cv2

# Set the base directory for the images
base_dir = 'all_wsi/'

# Set the target image size
target_size = (512, 512)

# Iterate through each subdirectory in the base directory
for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    if os.path.isdir(subdir_path):
        # Iterate through each image file in the subdirectory
        for filename in os.listdir(subdir_path):
            # Check if the file is a PNG image
            if filename.endswith('.png'):
                filepath = os.path.join(subdir_path, filename)
                # Read the image using opencv
                img = cv2.imread(filepath)
                # Resize the image using opencv
                img = cv2.resize(img, target_size)
                # Write the resized image to original file
                cv2.imwrite(filepath, img)
                # Confirm resize with print statement
                print(f'Resized image: {filepath}')
