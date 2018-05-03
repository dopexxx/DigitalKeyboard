import serial, string, os, sys
import numpy as np


class typing(object):
    
    """
    Untested draft for a class
    
    """
    
    
    def __init__(self,dev='Mo',pipe='Mo'): 
        """
        Parameters:
        -----------
        DEV      {str} specifiying the serial port (depending on used device)
        PIPE     {str} specifiying the pipeline to use (Mo's per default)
        
        """
        
        if dev == 'Mo':
            self.ard = serial.Serial('/dev/tty.usbmodem1411', 9600)
        elif dev == 'J':
            self.ard = serial.Serial('/dev/tty.usbmodem14421',9600) 
        else:
            raise ValueError("Unspecified serial port")
            
        if pipe == 'Mo':
            # Original pipeline
            self.create_table()        
            self.out = self.read_arduino()
            self.translate()
        elif pipe == 'J'
            # Alternative pipeline
            self.predictions = str()
            self.create_dict()
            self.read_arduino() # Change 1 line in that method
            self.translate_dict()
        else:
            raise ValueError("Unspecified pipeline")
        
        
        
    def read_arduino(self,):
    ''' 
    Creates a serial object to read from arduino, reads the values and 
    converts them to a character according to the lookup table created in
    create_table
    '''   
    self.out = []
    while True:
        x = self.ard.readline()
        x = x.decode('utf-8')
        x = x[:-2]
        print('---')
        print(x)
        self.out.append(x)
        self.translate()
        # Alternative
        # self.translate_dict()
        if len(out)>20:
            break
    return out


    def create_table(self):
        '''Create lookup table that converts 5-bit strings to letters'''   
        index = np.arange(0,26,1)
        binary = []
        chars = []
        for i in range(26): # suboptimal
            current = bin(int(index[i]))
            binary.append(format(current[2:].zfill(5)))
            chars.append(string.ascii_lowercase[i])
        self.table = np.column_stack([binary,chars]) 
    
    
    def translate(self):
        ''' 
        Implements lookup table created using create_table
        '''
        translation = []
        for i in range(len(self.out)):
            idx = np.where(self.table[:,0]==self.out[i])
            try: 
                idx = np.asscalar(idx[0])
                translation.append(self.table[idx,1])
            except ValueError: # invalid combination
                translation.append('%')
        print("".join(translation))



    def create_dict(self):
        self.chars = dict()
        self.chars['10000'] = 'a'
        self.chars['01000'] = 'e'
        self.chars['00100'] = 'i'
        self.chars['00010'] = 'o'
        self.chars['00001'] = 'u'
        self.chars['11000'] = 't'
        self.chars['10100'] = 'n'
        self.chars['10010'] = 's'
        self.chars['10001'] = 'h'
        self.chars['11100'] = 'r'
        self.chars['01100'] = 'd'
        self.chars['01110'] = 'l'
        self.chars['00111'] = 'c'
        self.chars['11110'] = 'm'
        self.chars['01111'] = 'w'
        self.chars['00110'] = 'f'
        self.chars['10011'] = 'g'
        self.chars['10111'] = 'y'
        self.chars['01010'] = 'p'
        self.chars['11011'] = 'b'
        self.chars['00011'] = 'v'
        self.chars['11001'] = 'k'
        self.chars['00101'] = 'j'
        self.chars['01101'] = 'x'
        self.chars['10101'] = 'z' 
        self.chars['11101'] = 'q'
        self.chars['11111'] = ' '
        self.chars['10110'] = '.'
        self.chars['01001'] = ','
        self.chars['01011'] = '!'
        # chars['11010'] = CAPS LOCK

        self.upper = dict()
        self.upper['10110'] = ':'
        self.upper['01001'] = ';'
        self.upper['01011'] = '?'
        
        self.capslock = False # Default is lowercase writing




    def translate_dict(self):
        """
        Retrieves character from a dictionary by using 5-digit binary string as key.
        """


        if self.out[-1] == '11010': # CAPS LOCK PRESSED?

            self.capslock = not self.capslock 
            print("Capslock activated." if self.capslock else "Capslock deactivated.")

        else:

            char = self.chars[self.out[-1]].upper() if self.capslock else self.chars[self.out[-1]]
            self.predictions += self.upper[self.out[-1]] if self.out[-1] in self.upper and self.capslock else char
            print(self.predictions)



typer = typing()
    
