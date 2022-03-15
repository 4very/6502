

from lib.p6502 import p6502
from time import sleep

p = p6502('graphics_test')

while p.mmu.read(0) != 0xFF:
    p.step()
    sleep(0.001)
    # print(f'{p.mmu.read(0x0004):08b}')

print('done!')