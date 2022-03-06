
from lib.py65emu.py65emu.cpu import CPU
from lib.py65emu.py65emu.mmu import MMU




m = MMU([
    (0x00, 0x200),
    (0x1000, 0x4000, True, f)
])