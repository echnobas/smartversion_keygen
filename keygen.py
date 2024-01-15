username = input()

import random
username = username.upper()
x = 0x47694c
y = len(username)
for i in range(len(username)):
    if not (i % 14): # i is a multiple of 14
        y = 39
    x += y * ord(username[i])
    if (i + 3) % 14: # i + 3 is not a multiple of 14
        y *= 3
    else:
        y *= 7
raw = random.choice(
  [
    0x12091999,
    0x31121999,
    0x2062000,
    0x13062004,
    0x21032004,
    0x28032004,
    0x5052005,
    0x29052005,
    0x1122004
  ]) + x
print(hex(raw)[2:].upper().replace("8", "\0").replace("B", "8").replace("\0", "B"))