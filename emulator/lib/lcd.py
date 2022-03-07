from cmath import log10
from time import sleep
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
    

s = Screen(64, 128, 'white', 10)
s.draw(0, 0, 'red')
s.draw(1, 0, 'green')
s.draw(2, 0, 'blue')
s.draw(3, 0, 'yellow')
s.draw(4, 0, 'black')
s.draw(5, 0, 'white')
s.draw(6, 0, 'red')
s.draw(7, 0, 'green')
s.draw(8, 0, 'blue')
s.draw(9, 0, 'yellow')
s.draw(10, 0, 'black')
s.draw(11, 11, 'red')
s.draw(12, 11, 'green')
s.draw(13, 11, 'blue')
s.draw(14, 11, 'yellow')

class LCD:


    def __init__(self):
        self.screen = Screen(128,64, scale=2)
        self.col = 0x00000000
        self.row = 0x0000
        self.data = [[0 for _ in range(128)] for _ in range(64)]

        addrs = {
            '0101010111x': self.DON,
            '0101011xxxx': self.PAGEADDR,
            '0100001xxxx': self.UCOLADD,
            '0100000xxxx': self.LCOLADD,
            '01011100011': self.NOP,
            '101xxxxxxxx': self.READ,
            '110xxxxxxxx': self.WRITE,
            '01011100010': self.RESET
        }

        self.instr = {}

        for key,val in addrs.items():
            if key.find('x') != -1:
                xs = key.count('x')
                for i in range(2**xs):
                    nkey = key.replace('x'*xs,bin(i)[2:].zfill(xs))
                    self.instr[nkey] = val
            else:
                self.instr[key] = val





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
                addr = f'{addr%16:03b}{val:08b}'
                self.instr[addr](addr)

                

    
    # 0101010111x - display on/off
    def DON(self, addr):
        pass
    
    # 0101011xxxx - page address
    def PAGEADDR(self, addr):
        pass

    # 0100001xxxx - upper column address
    def UCOLADD(self, addr):
        pass

    # 0100000xxxx - lower column address
    def LCOLADD(self, addr):
        pass

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



    # LCD().process({
    #     'start': 0x6000,
    #     'length': 0x000F,
    #     'readonly': False,
    #     'memory': [
    #         0x00, # 0000
    #         0x00, # 0001
    #         0b11100011, # 0010
    #         0x00, # 0011
    #         0x00, # 0100
    #         0x00, # 0101
    #         0x00, # 0110
    #         0x00, # 0111
    #         0x00, # 1000
    #         0x00, # 1001
    #         0x00, # 1010
    #         0x00, # 1011
    #         0x00, # 1100
    #         0x00, # 1101
    #         0x00  # 1110
    #     ]
    # })





