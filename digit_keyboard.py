#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:23:12 2018

@author: moritzgruber

Python interface for arduino-based 5-digit keyboard. 

requires pySerial

''' TBD: 
1. make table into dict for speed
2. tidy up code
3. think about smart way to assign characters to binary numbers
4. think about ways to use this
''' 
"""

import serial
import numpy as np
import string

def read_arduino(table):
    ''' Creates a serial object to read from arduino, reads the values and 
    converts them to a character according to the lookup table created in
    create_table'''   
    #ard = serial.Serial('/dev/tty.usbmodem1411', 9600)
    ard = serial.Serial('/dev/tty.usbmodem14121',9600) 
    out = []
    while True:
        x = ard.readline()
        x = x.decode('utf-8')
        x = x[:-2]
        print('---')
        print(x)
        out.append(x)
        print(translate(out,table))
        if len(out)>20:
            break
    return out

def create_table():
    '''Create lookup table that converts 5-bit strings to letters'''   
    index = np.arange(0,26,1)
    binary = []
    chars = []
    for i in range(26): # suboptimal
        current = bin(int(index[i]))
        binary.append(format(current[2:].zfill(5)))
        chars.append(string.ascii_lowercase[i])
    table = np.column_stack([binary,chars]) 
    return table



def translate(binary_list,table):
    ''' Implements lookup table created using create_table'''
    translation = []
    for i in range(len(binary_list)):
        idx = np.where(table[:,0]==binary_list[i])
        try: 
            idx = np.asscalar(idx[0])
            translation.append(table[idx,1])
        except ValueError: # invalid combination
            translation.append('%')
    return "".join(translation)

def main():
    '''Main method. Reads 5 numbers from arduino, outputs them as letters
    on-line and then outputs the resulting string.'''
    table = create_table()
    out = read_arduino(table)
    translate(out,table)
    
if __name__=='__main__':
    main()
    


    
