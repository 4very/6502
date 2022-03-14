
# 6502
This project is inspired by [Ben Eater's series](https://www.youtube.com/playlist?list=PLowKtXNTBypFbtuVMUVXNR0z1mu7dp7eH) about building a computer around a W65C02 microprocessor. My application for emulating the project was to create a [Tamagotchi](https://tamagotchi.fandom.com/wiki/Tamagotchi_(1996_Pet))-esque digital pet on a dot matrix lcd screen. The end goal of this project is to learn and design my own pcd to mount all of the hardware inside of a frame to hang on the wall.

---
## Emulator

It's easier debugging a emulator than hardware with an arduino... right? Yes™

### Checklist
- [x] LCD Emulator
- [x] Write test program to write to emulator

### Dependencies
- [py65emu](https://github.com/docmarionum1/py65emu/blob/master/README.rst) a 6502 emulator
- tkinter to emulate a dot matrix screen

if using screen.py under wsl than you need to install https://medium.com/javarevisited/using-wsl-2-with-x-server-linux-on-windows-a372263533c3

