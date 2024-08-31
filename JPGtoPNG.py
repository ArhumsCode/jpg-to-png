#Given an existing folder of .jpg images
#This program will convert the .jpg images
#into a .png and save it to a new folder name of your choice



import sys
import os
from PIL import Image

argument_one = sys.argv[1]
argument_two = sys.argv[2]


# grab the first and second argument

# check if new/ exists, if not create it
# loop through images/
def png_to_jpg(existing_folder, new_folder):
    if new_folder not in os.listdir('..'):
        os.makedirs(new_folder)
    for img in os.listdir(existing_folder):
        jpeg_image = Image.open(f'{existing_folder}/{img}')
        clean_name = os.path.splitext(img)[0]
        jpeg_image.save(f'{new_folder}/{clean_name}.png', 'png')


png_to_jpg(argument_one, argument_two)

# convert image to png.
# save to the new folder
