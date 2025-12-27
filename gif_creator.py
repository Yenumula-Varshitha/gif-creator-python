from PIL import Image
import os

folder = os.getcwd()

images = sorted([img for img in os.listdir(folder) if img.endswith('.jpg')])

frames = []

WIDTH, HEIGHT = 500, 500

for image in images:
    img = Image.open(image)
    img = img.resize((WIDTH, HEIGHT))
    frames.append(img)

frames[0].save(
    "output.gif",
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=700,
    loop=0
)

print("GIF created successfully!")