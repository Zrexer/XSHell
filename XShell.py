#!/usr/bin/env python3

"""
XShell 
~~~~~~~~

Linux SHell and Control Manager

Version: `1.0.0`
"""

# For Better Availabality
vr = "1.0.0"

import os
import platform
import random
import hashlib
import requests

osx = platform.system()

os.system('')


# This Class Pasted from BrupRocket => https://github.com/Zrexer/BrupRocket

hashlist = ['sha1', 'sha256', 'sha224', 'sha512', 'sha384', 'sha3_256', 'sha3_224', 'sha3_512', 'sha3_384']

def createHasher(text : str, type_of_encrypt : str):
        """
        Hash Creator
        ~~~~~~~~~~~~~
        Available Type of hash: 
        
        `md5`
        `sha1`
        `sha256`
        `sha224`
        `sha512`
        `sha384`
        `sha3_256`
        
        or you can select a random type , just use "random" on parameter.
        
        """
        
        t = type_of_encrypt
        
        if t == "md5":
            md5 = hashlib.md5()
            md5.update(text.encode())
            return md5.hexdigest()
        
        elif (
            t == "sha1"
            ):
            sha1 = hashlib.sha1()
            sha1.update(
                text.encode()
                )
            return (
                sha1.hexdigest()
                )
        
        elif (
            t == "sha256"
            ):
            sha256 = hashlib.sha256()
            sha256.update(
                text.encode()
                )
            return (
                sha256.hexdigest()
                )
        
        elif (
            t == "sha224"
            ):
            sha224 = hashlib.sha224()
            sha224.update(
                text.encode()
                )
            return (
                sha224.hexdigest()
                )
        
        elif (
            t == "sha512"
            ):
            sha512 = hashlib.sha512()
            sha512.update(
                text.encode()
                )
            return (
                sha512.hexdigest()
                )
        
        elif (
            t == "sha384"
            ):
            sha384 = hashlib.sha384()
            sha384.update(
                text.encode()
                )
            return (
                sha384.hexdigest()
                )
        
        elif (
            t == "sha3_256"
            ):
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(
                text.encode()
                )
            return (
                sha3_256.hexdigest()
                )
        
        elif (
            t == "sha3_224"
            ):
            sha3_224 = hashlib.sha3_224()
            sha3_224.update(
                text.encode()
                )
            return (
                sha3_224.hexdigest()
                )
        
        elif (
            t == "sha3_512"
            ):
            sha3_512 = hashlib.sha3_512()
            sha3_512.update(
                text.encode()
            )
            return (
                sha3_512.hexdigest()
            )
            
        elif (
            t == "sha3_384"
        ):
            sha3_384 = hashlib.sha3_384()
            sha3_384.update(
                text.encode()
            )
            return (
                sha3_384.hexdigest()
            )
            
        elif (
            t == "random"
        ):
            result = (
                random.choice(hashlist)
            )
            
            return createHasher(text=text, type_of_encrypt=result)
        
# Version of tool
def version():
    return vr

# Base of Scripts
def scriptIt(scr):
    if scr == "timer":
        return """
import time 
import requests

link = "https://github.com/Zrexer"

start = time.time()
req = requests.get(link).status_code
end = time.time()

time_of_mission = f"{end-start:.2f}"
print(f'status: {req} time: {time_of_mission}')


note: if you want to change float just edit 2f , for example i want to show under 3 float, so i edit it to end-start:.3f
"""

    elif scr == "domain-ip":
        return """
import socket 

domain = "google.com"

ip = socket.gethostbyname(domain)

print(f"[+] ip: {ip}")
"""

    elif scr == "local-ip":
        return """
import socket 

host = socket.gethostname()
ip = socket.gethostbyname(host)

print(f"[+] ip: {ip}")
"""

    elif scr == "public-ip":
        return """
import requests 

ip = requests.get('https://api.ipify.org').text

print(f"[+] ip: {ip}")
"""

    elif scr == "help":
        return """
Scripts Call: 

timer
domain-ip
local-ip
public-ip
"""

def windowsShell():
    while 1:
        try:
            path = os.getcwd()
            user = str(input(f'\033[95m<\033[96mXSHell\033[95m> \033[93m{path}\033[97m> '))
            if user.startswith('cd'):
                newPath = user.replace('cd ', '')
                os.chdir(newPath)
                
            elif "--hash" in user.split():
                if "--type" in user.split():
                    type_ = user.split()[user.split().index("--type")+1]
                    text_ = user.split()[user.split().index('--hash')+1]
                    print("[+] "+createHasher(text=text_, type_of_encrypt=type_))
                    
                else:
                    text = user.split()[user.split().index('--hash')+1]
                    print("[+] "+createHasher(text=text, type_of_encrypt='random'))
                    
                    
            elif "--connect-get" in user.split():
                link_ = user.split()[user.split().index("--connect-get")+1]
                if user.split[-1] == "--status":
                    try:
                        dataS = requests.get(link_).status_code
                        print(f"[+] {dataS}")
                    except Exception as EDS:
                        print(f"[-] Error: {EDS}")
                        pass
                
                elif user.split()[-1] == "--json":
                    try:
                        dataJ = requests.get(link_).json()
                        print(f"[+] {dataJ}")
                    except Exception as EDJ:
                        print(f"[-] Error: {EDJ}")
                        pass
                
                elif user.split()[-1] == "--body":
                    try:
                        dataB = requests.get(link_).text
                        print(f"[+] {dataB}")
                    except Exception as EDB:
                        print(f"[-] Error: {EDB}")
                        pass
                        
                else:
                    try:
                        dataB___ = requests.get(link_).text
                        print(f"[+] {dataB___}")
                    except Exception as EDB:
                        print(f"[-] Error: {EDB}")
                        pass
                    
            elif "--connect-post" in user.split():
                link_ = user.split()[user.split().index("--connect-post")+1]
                if user.split[-1] == "--status":
                    try:
                        dataS_ = requests.post(link_).status_code
                        print(f"[+] {dataS_}")
                    except Exception as EDS_:
                        print(f"[-] Error: {EDS_}")
                        pass
                
                elif user.split()[-1] == "--json":
                    try:
                        dataJ_ = requests.post(link_).json()
                        print(f"[+] {dataJ_}")
                    except Exception as EDJ_:
                        print(f"[-] Error: {EDJ_}")
                        pass
                
                elif user.split()[-1] == "--body":
                    try:
                        dataB_ = requests.post(link_).text
                        print(f"[+] {dataB_}")
                    except Exception as EDB:
                        print(f"[-] Error: {EDB}")
                        pass
                        
                else:
                    try:
                        dataB__ = requests.post(link_).text
                        print(f"[+] {dataB__}")
                    except Exception as EDB_:
                        print(f"[-] Error: {EDB_}")
                        pass
                    
            elif "--script" in user.split():
                script = user.split()[user.split().index("--script")+1]
                
                print(scriptIt(script))
                    
            elif "--version" in user.split():
                print(version())
                
            elif "-v" in user.split():
                print(version())
            
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
        
        
"""            elif "" user.split():
                text_ = user.split()[-3]
                if user.split()[-2] == "--type":
                    type_ = user.split()[-1]
                    print(createHasher(text_, type_))
                    
                else:
                    print('[-] Faild to use: Switch --type')"""