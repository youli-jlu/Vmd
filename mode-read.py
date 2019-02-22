#!/usr/bin/python
import os
import shutil
import re
import sys

def main():
    nmode = open("normal-mode1.dat",mode='r')
    nmd = open("lm.nmd",mode='a')
    lines = nmode.readlines()
    nmd.write("mode 1 ")
    for line in lines[0:len(lines)]:
        word = line.split()
        nmd.write(" " + word[0])
    nmd.close()
    nmode.close()

main()
