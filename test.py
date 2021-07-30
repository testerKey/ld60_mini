#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/5/29 15:00
# @author    : zhuziqing
# @File      : test.py
import os
from time import sleep
import sys



output=sys.stdout
outputfile=open("2.doc","a")
print("[35m[Appium][39m Welcome to Appium v1.20.2",file=outputfile)
sys.stdout=outputfile