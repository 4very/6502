
# from https://github.com/docmarionum1/py65emu/blob/master/README.rst

from os.path import join, dirname, basename, splitext
from os import getcwd

import sys
sys.path.insert(0, join(getcwd(), 'emulator'))

from lib.py65emu.py65emu.cpu import CPU
from lib.py65emu.py65emu.mmu import MMU

from os.path import basename
from os import getcwd


folder = basename(dirname(__file__))
filename = splitext(basename(__file__))[0]

f = open(f'./programs/{folder}/{filename}.bin', 'rb')

mmu = MMU([
    (0x00, 0x200),
    (0x1000, 0x4000, True, f)
])

c = CPU(mmu, 0x1000)

c.step()
c.step()


print(c.r.a)    # A register
print(c.r.x)    # X register
print(c.r.y)    # Y register
print(c.r.s)    # Stack Pointer
print(c.r.pc)   # Program Counter

print(c.cc)

print(c.r.getFlag('C'))
print(mmu.read(0x00))