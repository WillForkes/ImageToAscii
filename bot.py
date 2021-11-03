import os
from PIL import Image
import math

def point_value(x):
    return int(x / 50)

def char_value(n):
    arr = ["..", "--", "::", "!!", "11", "##"]
    return arr[n]

image_file = input("Image file [>>] ").replace("\"", "")

image = Image.open(image_file)
multiplier = int((image.size[1] / 100) * 1.7) # fits image into screen size

image = image.resize((int(image.size[0] / multiplier), int(image.size[1] / multiplier))) # resize image to fit screen
image = image.convert('L').point(point_value, mode="1") # convert each point to number returned by point_value func

length = image.size[0]
height = image.size[1]
toprint = ""

os.system(f"mode con: cols={length * 2} lines={height}") # resize window to fit image
for y in range(height):
    for x in range(length):
        toprint += char_value(image.getpixel((x, y))) # image.getpixel return value between 0-5

    print(toprint) 
    toprint="" # reset row for next line

input() # pause