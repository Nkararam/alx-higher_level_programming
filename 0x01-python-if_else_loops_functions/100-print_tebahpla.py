#!/usr/bin/python3
for b in range(ord('z'), ord('a') - 1, -1):
    if b % 2 == 0:
        i = 0
    else:
        i = 32
    print('{}'.format(chr(b - i)), end='')
