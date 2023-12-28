# @#&%0
from PIL import Image
import os

image = input("enter file directory of image: ")

im = Image.open(image)
im1 = im.convert("L")
img_size = (im1.size)
width = img_size[0]
height = img_size[1]
im1 = im1.resize((width*3, height*2))
if img_size[0] > 600 or img_size[1] > 1000:
    width = img_size[0]/2
    height = img_size[1]/2
    if width%2 != 0:
        width += 0.5
    if width%2 != 0:
        height += 0.5
    im1 = im1.resize((int(width), int(height)))

ac = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
im2list = list(im1.getdata())

with open(f"doodled_{os.path.basename(image)}.txt", "w") as file:
    file.write("")

with open(f"doodled_{os.path.basename(image)}.txt", "a") as file:
    for index, val in enumerate(im2list):
        if index%(width) == 0:
            file.write("\n")
        if val <= 23:
            file.write(ac[-1])
        elif val <= 46:
            file.write(ac[-2])
        elif val <= 69:
            file.write(ac[-3])
        elif val <= 92:
            file.write(ac[-4])
        elif val <= 115:
            file.write(ac[-5])
        elif val <= 138:
            file.write(ac[-6])
        elif val <= 161:
            file.write(ac[-7])
        elif val <= 184:
            file.write(ac[-8])
        elif val <= 207:
            file.write(ac[-9])
        elif val <= 230:
            file.write(ac[-10])
        else:
            file.write(ac[-11])