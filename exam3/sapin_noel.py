#!/usr/bin/python3

import sys
from math import floor
from random import randrange

def show_tree(size) :
    sapin =""
    size_tronc = floor(size/5) + 1
    if (size % 2 == 0):
        size = size +1
    if (size <=3):
        tronc = 1
    else :
        tronc = 3
    for s in range (1, size+1, 2):
        sapin = sapin + (s * "x").center(size)
        sapin = sapin + "\n"

    boules = list(sapin)

    for b in range(len(boules)):
        if (boules[b] == 'x'):
            if (randrange(size) < floor(size / 10)):
                boules[b] = 'O'
    sapin= "".join(boules)


    for t in range(size_tronc):
        if (tronc == 1):
            sapin = sapin + ("x".center(size))
        else :
            sapin = sapin + (tronc * "x").center(size)
            sapin = sapin + "\n"
    return sapin

if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))