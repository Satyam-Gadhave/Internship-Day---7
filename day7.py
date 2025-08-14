import os
from PIL import Image

input = r'C:\Users\Sunny\Desktop\images'
output = "resized images"
new_size = (400,400)

os.makedirs(output, exist_ok=True)

for file_name in os.listdir(input):
    if file_name.lower().endswith(('.jpg','.jprg','.png')):
        image_path = os.path.join(input, file_name)
        output_path = os.path.join(output, file_name)

        try:
            with Image.open(image_path) as img:
             resized_img = img.resize(new_size)
             resized_img.save(output_path)
             print(f'resized: {file_name}')

        except Exception as e:
           print(f'error processing {file_name}: {e}')

print("done resizing images.")