#!/usr/bin/env python3
#   decode.py
#   Note this will not run in the code editor and must be downloaded
#   If using a macOS device, change im to open "macOutput.gif"
from PIL import Image 

im = Image.open("encrypted.gif")
rgb_im = im.convert('RGB')

MAX_CHARACTERS = 20
BITS_IN_A_BYTE = 8
MAX_BITS = MAX_CHARACTERS * BITS_IN_A_BYTE

my_array = []
for letters in range(0,MAX_BITS):
    my_array.append(0)

UPPER_PIXEL_ROW = int(.24 * rgb_im.size[0] - 27)
LEFT_PIXEL_COL = int(.785 * rgb_im.size[1] - 361)
DISTANCE_BETWEEN_BLOCKS = 27
LOW_PIXEL_ROW = UPPER_PIXEL_ROW + (MAX_CHARACTERS * DISTANCE_BETWEEN_BLOCKS)
RIGHT_PIXEL_COL = LEFT_PIXEL_COL + (BITS_IN_A_BYTE * DISTANCE_BETWEEN_BLOCKS)

pos = 0
for i in range(UPPER_PIXEL_ROW, LOW_PIXEL_ROW, DISTANCE_BETWEEN_BLOCKS):
    for j in range(LEFT_PIXEL_COL, RIGHT_PIXEL_COL, DISTANCE_BETWEEN_BLOCKS):
        r,g,b = rgb_im.getpixel((j,i))
        if g < 254: #the white pixels have green values of 254, blue have less
            my_array[pos] = 1
        pos = pos + 1
print(my_array)

message_as_bits = ''
for bit in my_array:
  message_as_bits = message_as_bits + str(bit)
print(message_as_bits)

letter = 0
decoded = ''
for n in range(0,MAX_BITS):
  if n % 8 == 0:
    if letter != 0:
      decoded = decoded + chr(letter)
      letter = 0
    letter = int(message_as_bits[n]) * 128 + letter
  elif n % 8 == 1:
    letter = int(message_as_bits[n]) * 64 + letter
  elif n % 8 == 2:
    letter = int(message_as_bits[n]) * 32 + letter
  elif n % 8 == 3:
    letter = int(message_as_bits[n]) * 16 + letter
  elif n % 8 == 4:
    letter = int(message_as_bits[n]) * 8 + letter
  elif n % 8 == 5:
    letter = int(message_as_bits[n]) * 4 + letter
  elif n % 8 == 6:
    letter = int(message_as_bits[n]) * 2 + letter
  elif n % 8 == 7:
    letter = int(message_as_bits[n]) * 1 + letter
print(decoded)