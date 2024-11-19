import os
from PIL import Image
import algorithm
import main

img = Image.open('movie2.png')
imgGray = img.convert('L')
imgGray.save('bw.png')


# with open("bw.png", "rb") as image:
#   f = image.read()
#   b = bytearray(f)
#   for i in b:
#       print(i)

def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())


bytes = readimage('bw.png')
e_bytes = []
for i in bytes:
    add = algorithm.driver(int(i))
    print(int(add))
    e_bytes.append(str(add))


def swap_pixels(input_image, region_lists):
    pixels = list(input_image.getdata())
    # print(region_lists)
    for region in region_lists:
        for i in range(0, len(region) - 1, 2):
            pixels[int(region[i]) % 100], pixels[int(region[i + 1]) % 100] = (pixels[int(region[i + 1]) % 100],
                                                                              pixels[int(region[i]) % 100])
    scrambled_image = Image.new(input_image.mode, input_image.size)
    scrambled_image.putdata(pixels)
    return scrambled_image

input_image = Image.open('bw.png')
output = swap_pixels(input_image,e_bytes)
main.scramble(output)

# image = Image.open(io.BytesIO(bytes))
# image.save('new.png')
