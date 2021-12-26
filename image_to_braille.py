"""
for i in range(0xa0, 0xa3 + 1):
    for j in range(0x80, 0xff):
        try:
            char = (b'\xe2' + bytes([i]) + bytes([j])).decode("utf-8")
            print(f"{bin(i)} {bin(j)} {char}")
        except:
            pass
"""
'''
while True:
    bin = input()
    i = int(bin[0:8], 2)
    j = int(bin[8:16], 2)
    try:
        char = (b'\xe2' + bytes([i]) + bytes([j])).decode("utf-8")
        print(char)
    except:
        print("-")


'''
"""
def print_braille(array):
    for i in range(0, len(out1), 2):
        for j in range(0, len(out1[0]), 5):
            char = 

test=[
    [True, True],
    [True, False],
    [True, True],
    [True, True],
]

print(print_braille(test))
"""

#111000101010000010000000
#111000101010001110111111
#               100000000
char = 0b111000101010000010000000
char = (char & ~0b1) | 0b1 if True else char
char = (char & ~0b1000) | 0b1000 if True else char
char = (char & ~0b10) | 0b10 if True else char
char = (char & ~0b10000) | 0b10000 if True else char
char = (char & ~0b100) | 0b100 if True else char
char = (char & ~0b100000) | 0b100000 if True else char
char = (char & ~0b100000000) | 0b100000000 if True else char
char = (char & ~0b1000000000) | 0b1000000000 if True else char
print(char.to_bytes(24, "big").decode('utf-8'))