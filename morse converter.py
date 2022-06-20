# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:34:13 2022

@author: SergioOliveira
"""

import requests


code = input("Write the message or character:")

def convert_message(code):
        code = code.replace('A', '. _' )
        code = code.replace('a', '. _' )
        code = code.replace('B', '_ . . .' )
        code = code.replace('b', '_ . . .' )
        code = code.replace('C', '_ . _ .')
        code = code.replace('c', '_ . _ .')
        ...
        return code


if len(code) > 0:
    convert_message(code)
else:
    print('Error insert valid message')
 

       
lock_code = code
print(f"Your message was: {lock_code}")

morse = convert_message(code)
print(f'your morse code is: {morse}')

