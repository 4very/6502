from lib.py65emu.py65emu.cpu import CPU
from lib.py65emu.py65emu.mmu import MMU
from lib.lcd import LCD


class p6502:
    def __init__(self, filename):
        f = open(r'./programs/bin/' + filename + '.bin', 'rb')
        
        self.mmu = MMU([
            # 0000 - 0011
            (0x0000, 0x3000), # 0x0000 - 0x3000: RAM

            # 0110 - 0111
            (0x6000, 0x000F), # 0x6000 - 0x600F: LCD

            # 1000 - 1111
            (0x8000, 0x8000, True, f) # 0x8000 - 0xFFFF: ROM
        ])

        # read start vector at 0xFFFC and 0xFFFD
        self.cpu = CPU(self.mmu, self.read16Hex(0xfffc))

        self.lcd = LCD()
        


    # read 16-bit hex value from memory in little-endian format
    def read16Hex(self, addr):
        return self.mmu.read(addr+1) << 8 | self.mmu.read(addr)

    # step the 6502 emulator
    def step(self):
        self.cpu.step()
        block = self.mmu.getBlock(0x6000)
        self.lcd.process(block)
        self._blank(block)
    
    def _blank(self, block):
        for i in range(block['length']):
            self.mmu.write(i+block['start'], 0)
        
            

