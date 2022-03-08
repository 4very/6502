
from PIL import Image
from math import sqrt

def bmp2bin(filename):
    img = Image.open(f'./img/src/{filename}.bmp')
    print(img.size)
    val = []
    for x in range(img.width):
        for y in range(0, img.height, 8):
            word = 0
            for i in range(8):
                pix = img.getpixel((x, y + i))
                word += int(pix == 0) << i
            
            val.append(word)



    with open(f'./img/bin/{filename}.bin', 'wb') as f:
        f.write(bytearray(val))
    with open(f'./img/{filename}.txt', 'w') as f:
        for x in val:
            f.write(f'\t.byte %{x:08b}\n')



def bin2bmp(filename):
    with open(f'./img/bin/{filename}.bin', 'rb') as f:
        val = f.read()

    size = int(sqrt(len(val)*8))
    img = Image.new('1', (size, size), 'white')
    for x in range(size):
        for y in range(4):
            for i in range(8):
                # print(x, y*4+i, y+(x*4))
                img.putpixel((x, y*4+i), 0 if (val[y+(x*4)] & (1 << i)) else 255)

    img.save(f'./img/{filename}-conv.bmp') 



bmp2bin('heart32')
bin2bmp('heart32')