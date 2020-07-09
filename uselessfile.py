#!/usr/bin/env python
#based on https://eyehere.net/2011/python-pygame-novice-professional-2/

from sys import exit

Global_X=4
print(Global_X)
def sub_pgm ():
    print("sub starts")
    Global_X=5
    print("sub change Gloabl_x=5")
    print(Global_X)
    return

sub_pgm()
print("return to main")
print(Global_X)
input("how")
exit()
