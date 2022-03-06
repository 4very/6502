#!/bin/sh

./compilier/bin/vasm/v1.9/vasm6502_oldstyle -dotdir -Fbin ./programs/src/$1.s -o ./programs/bin/$1.bin
