#!/usr/bin/python3

import sys
import os
import time
from time import localtime, strftime

abspath = "/home/aknapp/Documents/Betriebssysteme/FilesysMem"

def get_current_time():
    time_string = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    return time_string

def write_to_file(filename):
    f = open(abspath + filename,"w+")
    i = 0
    while (i <= 25):
        print("Write Line: " + str(i) + " - " + get_current_time() + "\n")
        f.write("Write Line: " + str(i) + get_current_time() + "\n")
        time.sleep(1)
        i+=1
    f.close()

def append_to_file(filename):
    f = open(abspath + filename, "a+")
    i = 0
    while (i <= 25):
        print("Append Line: " + str(i) + " - " + get_current_time() + "\n")
        f.write("Append Line: " + str(i) + get_current_time() + "\n")
        time.sleep(1)
        i+=1
    f.close()

def read_from_file(filename):
    f = open(abspath + filename, "r")
    i = 0
    for n in f.readlines():
        print(n)
        time.sleep(1)
    f.close()

write_to_file("/file1.txt")
append_to_file("/file2.txt")
read_from_file("/file1.txt")
read_from_file("/file2.txt")
