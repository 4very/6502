from lib.screen import Screen
from time import sleep
from random import randint

screen = Screen(200, 200)
print('threaded')
screen.draw(100, 100, 'red')


for x in range(200):
    for y in range(200):
        if x % 10 == 0 or y % 10 == 0:
            screen.draw(x, y, 'red')