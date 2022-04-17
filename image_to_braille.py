from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs=1, type=str)
parser.add_argument("-H", "--h-gap", default=0, type=int)
parser.add_argument("-V", "--v-gap", default=0, type=int)
args = parser.parse_args()

image = Image.open(args.filename[0])
image = image.convert("1")
pixelmap = image.load()

for j in range(0, image.height, 4+args.v_gap):
    for i in range(0, image.width, 2+args.h_gap):
        try: 
            char = bytearray([0b11100010, 0b10100000, 0b10000000])
            char[2] = (char[2] & ~0b1     ) | 0b1      if pixelmap[i+0,j+0] else char[2]
            char[2] = (char[2] & ~0b1000  ) | 0b1000   if pixelmap[i+1,j+0] else char[2]
            char[2] = (char[2] & ~0b10    ) | 0b10     if pixelmap[i+0,j+1] else char[2]
            char[2] = (char[2] & ~0b10000 ) | 0b10000  if pixelmap[i+1,j+1] else char[2]
            char[2] = (char[2] & ~0b100   ) | 0b100    if pixelmap[i+0,j+2] else char[2]
            char[2] = (char[2] & ~0b100000) | 0b100000 if pixelmap[i+1,j+2] else char[2]
            char[1] = (char[1] & ~0b1     ) | 0b1      if pixelmap[i+0,j+3] else char[1]
            char[1] = (char[1] & ~0b10    ) | 0b10     if pixelmap[i+1,j+3] else char[1]
        except IndexError:
            pass
        else:
            print(char.decode("utf-8"), end="")
    print()
