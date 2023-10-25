#!/usr/bin/env python3

"""
XShell 
~~~~~~~~

Linux SHell and Control Manager

Version: `0.0.3`
"""

import os
import platform

osx = platform.system()

os.system('')

def windowsShell():
    while 1:
        try:
            path = os.getcwd()
            user = str(input(f'\033[95m<\033[96mXSHell\033[95m> \033[93m{path}\033[97m> '))
            if user.startswith('cd'):
                newPath = user.replace('cd ', '')
                os.chdir(newPath)
            
            elif user == "exit":
                exit()
                
                
            else:
                os.system(user)
                
        except KeyboardInterrupt:
            exit()
            
        
def linuxShell():
    while 1:
        try:
            path = os.getcwd()
            user = str(input(f'\033[92m<\033[93mXSHell\033[92m> \033[95m{path}\033[97m> '))
            if user.startswith('cd'):
                newPath = user.replace('cd ', '')
                os.chdir(newPath)
            
            elif user == "exit":
                exit()
                
                
            else:
                os.system(user)
                
        except KeyboardInterrupt:
            exit()

        
if __name__ == "__main__":
    if osx == "Windows":
        windowsShell()
        
    elif osx == "Linux":
        linuxShell()
