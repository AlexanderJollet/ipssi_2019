#!/usr/bin/python3

import sys

fd = str(sys.argv[1])
fichier = open(fd)

n = 0
while fichier.readline():
    n+=1

print(n)
