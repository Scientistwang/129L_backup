#!/usr/bin/python3
import os
os.system('/bin/ls /etc > etc.txt')
f = open('etc.txt','r')
print(f.read())
os.system('rm etc.txt')
