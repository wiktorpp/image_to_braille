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