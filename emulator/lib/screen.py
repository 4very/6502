import tkinter as tk
import threading

class Screen(threading.Thread):
    window = None

    def __init__(self, width, height, bg='white'):

        self.height = height
        self.width = width
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
            width=self.width, 
            height=self.height, 
            cursor='tcross')
        self.canvas.create_rectangle(
            0,
            0,
            self.width,
            self.height,
            fill=self.bg,
            outline=''
        )
        self.__draw()
        self.canvas.pack()
        self.root.mainloop()

    
    def __draw(self):
        for x, y, color in self.queue:
            self.canvas.create_rectangle(
                x, 
                y, 
                x+1, 
                y+1, 
                fill=color,
                outline=""
            )
            self.canvas.update()
            self.root.update()
        self.queue = []
        self.root.after(1, self.__draw)


    def draw(self, x, y, color):
        self.queue.append((x, y, color))
