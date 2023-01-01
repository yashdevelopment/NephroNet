# AUTHOR: YASH S
# Moves all the images to one directory

import os
import shutil

# Set the base directory for the images
base_dir = 'all_wsi/'

# Iterate through each subdirectory in the base directory
for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    if os.path.isdir(subdir_path):
        # Iterate through each image file in the subdirectory
        for filename in os.listdir(subdir_path):
            # Check if the file is a PNG image
            if filename.endswith('.png'):
                filepath = os.path.join(subdir_path, filename)
                # Move the image file to the base directory
                shutil.move(filepath, base_dir)
