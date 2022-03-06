from lib.py65emu.py65emu.cpu import CPU
from lib.py65emu.py65emu.mmu import MMU
from lib.screen import Screen


class p6502:
    def __init__(self, filename):
        f = open(r'./programs/bin/' + filename + '.bin', 'rb')
        self.mmu = MMU([
            (0x0000, 0x3000), # 0x0000 - 0x3000: RAM
            (0x6000, 0x1000), # 0x6000 - 0x7000: 6522
            (0x8000, 0x8000, True, f) # 0x8000 - 0xFFFF: ROM
        ])

        # read start vector at 0xFFFC and 0xFFFD
        self.cpu = CPU(self.mmu, self.read16Hex(0xfffc))

        self.screen = Screen(200,200)
        
    

    # read 16-bit hex value from memory in little-endian format
    def read16Hex(self, addr):
        return hex(self.mmu.read(addr+1) << 8 | self.mmu.read(addr))

    # step the 6502 emulator
    def step(self):
        self.cpu.step()
    
    def r(self):
        # return a register value
        def a(self):
            return self.cpu.a
        
        # return x register value
        def x(self):
            return self.cpu.x
        
        # return y register value
        def y(self):
            return self.cpu.y
        
        # return stack pointer value
        def s(self):
            return self.cpu.s
        
        # return program counter value
        def pc(self):
            return self.cpu.pc
        
        # return flag from flag register
        # N - Negative
        # V - Overflow
        # B - Break Command
        # D - Decimal Mode
        # I - Interrupt Disable
        # Z - Zero
        # C - Carry
        def getFlag(self, flag):
            return self.cpu.getFlag(flag)
        