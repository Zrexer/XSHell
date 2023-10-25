#!/usr/bin/env python3

"""
XShell 
~~~~~~~~

Linux SHell and Control Manager

Version: `0.0.1`
"""

import os

os.system('')

while 1:
    try:
        path = os.getcwd()
        user = str(input(f'\033[95mPS \033[96m{path}\033[93m>\033[97m '))
        if user.startswith('cd'):
            newPath = user.replace('cd ', '')
            os.chdir(newPath)
        
        elif user == "exit":
            exit()
            
        else:
            os.system(user)
            
    except:
        continue
