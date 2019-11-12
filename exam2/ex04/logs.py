#!/usr/bin/python3

from datetime import datetime

def logthis(a):
    date = datetime.now()
    datedate = date.strftime("%Y-%m-%d %H:%M:%S ")
    fichier = open("python.log", "a")
    fichier.write(datedate)
    fichier.write(a + "\n")
    fichier.close()
