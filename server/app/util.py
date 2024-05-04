import os
import numpy as np
from PIL import Image

# Define the directory to store generated images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def generate_noisy_images(num_images):
    image_paths = []
    for i in range(num_images):
        # Generate random noisy image
        img = np.random.rand(256, 256, 3) * 255  # Random pixel values
        noisy_img = Image.fromarray(img.astype('uint8')).convert('RGB')

        # Save the image
        img_filename = f'image_{i+1}.png'
        img_path = os.path.join(UPLOAD_FOLDER, img_filename)
        noisy_img.save(img_path)
        image_paths.append(img_path)

    return image_paths
