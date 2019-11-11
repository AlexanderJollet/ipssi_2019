#!/usr/bin/python3

from hashlib import md5
import sys

def compare_pass(mdp, encoding='utf-8'):
    mdp = str(sys.argv[1])
    ipssi = 'ipssi'
    newmdp = md5(mdp.encode(encoding)).hexdigest()
    testmdp = md5(ipssi.encode(encoding)).hexdigest()

    if (newmdp == testmdp):
        print ('md5 "ipssi": ' + newmdp)
        print ('md5   pass : ' + testmdp)
        return True
    else:
        print ('md5 "ipssi": ' + newmdp)
        print ('md5   pass : ' + testmdp)
        return False
