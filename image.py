from PIL import Image

img = Image.open('images/astronaut.jpg')

img.thumbnail((400, 400))
img.save('thumbnail.jpg')

