from cmath import log10
import tkinter as tk
from math import floor, log10
import threading

class Screen(threading.Thread):
    window = None

    def __init__(self, width, height, bg='white', scale=1):

        self.height = height
        self.width = width
        self.scale = scale
        
        self.sheight = width*scale + (scale - 1)
        self.swidth = height*scale + (scale - 1)

        self.bg = bg
        self.queue = []
        threading.Thread.__init__(self)
        self.start()


    def callback(self):
        print('window closed!')
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.canvas = tk.Canvas(self.root, 
            width=self.swidth,
            height=self.sheight, 
            cursor='tcross')
        self.canvas.create_rectangle(
            0,
            0,
            self.swidth,
            self.sheight,
            fill=self.bg,
            outline=''
        )

        self.postext = tk.Text(self.root, 
            height=1, 
            width=floor(log10(self.width))+floor(log10(self.height))+10,
            relief=tk.FLAT,
            background=self.bg,
            bg=self.bg,

            font=('Courier', 10))
        
        
        self.__process()  
        self.canvas.pack()
        self.postext.pack()

        self.root.mainloop()

    

    def __process(self):
        for func, args in self.queue: func(*args)
        self.queue = []
        self.__pos()
        self.root.after(1, self.__process)

    def __pos(self):
        self.postext.delete(1.0, tk.END)
        x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

        if x < 0 or y < 0 or x > self.swidth or y > self.sheight: 
            xscale = '---'
            yscale = '---'
        else:
            xscale = str(floor(x/self.scale))
            yscale = str(floor(y/self.scale))

        self.postext.insert(tk.END, 'x: ' + str(xscale) + ' y: ' + str(yscale))
        self.postext.update()
        self.root.update()

    def __draw(self, x, y, color):
        self.canvas.create_rectangle(
            x*self.scale + 1, 
            y*self.scale + 1, 
            x*self.scale + self.scale + 1,
            y*self.scale + self.scale + 1, 
            fill=color,
            outline=""
        )
        self.canvas.update()
        self.root.update()

    def __fill(self, color):
        self.canvas.create_rectangle(
            0,
            0,
            self.swidth,
            self.sheight,
            fill=color,
            outline=''
        )
        self.canvas.update()
        self.root.update()



    def draw(self, x, y, color):
        self.queue.append((self.__draw, (x, y, color)))
    
    def fill(self, color):
        self.queue.append((self.__fill, (color,)))
    

class LCD:


    def __init__(self):
        self.screen = Screen(64, 128, 'white', 10)
        self.col = 0x00000000
        self.page = 0x0000
        self.data = [[0 for _ in range(128)] for _ in range(64)]

        self.instr = {
            (0b01010101110, 0b01010101111):  self.DON,
            (0b01010110000, 0b01010111111):  self.PAGEADDR,
            (0b01000010000, 0b01000011111): self.UCOLADD,
            (0b01000000000, 0b01000001111): self.LCOLADD,
            (0b01011100011, 0b01011100011): self.NOP,
            (0b10100000000, 0b10111111111):  self.READ,
            (0b11000000000, 0b11011111111):  self.WRITE,
            (0b01011100010, 0b01011100010): self.RESET
        }



    def __read(self, addr):
        for key, item in self.instr.items():
            if addr >= key[0] and addr <= key[1]:
                return item
        pass

    # memory:
    #   start: start address
    #   length: length of block
    #   readonly: True if block is ROM
    #   memory: memory array
    def process(self, block):
        for i in range(block['length']):
            addr = block['start'] + i
            if block['memory'][i] != 0:
                val = block['memory'][i]
                addr = addr%8 << 8 & 0b0111 | val
                self.__read(addr)(addr)

                

    
    # 0101010111x - display on/off
    def DON(self, addr):
        pass
    
    # 0101011xxxx - page address
    def PAGEADDR(self, addr):
        arg = addr & 0b1111
        print(f'PAGEADDR {arg:04b}')
        self.page = addr%16

    # 0100001xxxx - upper column address
    def UCOLADD(self, addr):
        arg = addr & 0b1111
        pcol = self.col

        self.col = self.col & 0b00001111 | arg << 4
        print(f'LCOLADD {arg:04b} {pcol:08b} {self.col:08b}')

    # 0100000xxxx - lower column address
    def LCOLADD(self, addr):
        arg = addr & 0b1111
        pcol = self.col

        self.col = self.col & 0b11110000 | arg
        print(f'LCOLADD {arg:04b} {pcol:08b} {self.col:08b}')

    # 01011100011 - NOP
    def NOP(self, addr):
        print('NOP')
        pass
    
    # 101xxxxxxxx - data read
    def READ(self, addr):
        pass

    # 110xxxxxxxx - data write
    def WRITE(self, addr):
        
        pass
    
    # 01011100010 - reset
    def RESET(self, addr):
        pass




LCD().process({
    'start': 0x6000,
    'length': 0x000F,
    'readonly': False,
    'memory': [
        0x00, # 0000
        0x00, # 0001
        0b01000011111, # 0010
        0x00, # 0011
        0x00, # 0100
        0x00, # 0101
        0x00, # 0110
        0x00, # 0111
        0x00, # 1000
        0x00, # 1001
        0b01000000101, # 1010
        0x00, # 1011
        0x00, # 1100
        0x00, # 1101
        0x00  # 1110
    ]
})





