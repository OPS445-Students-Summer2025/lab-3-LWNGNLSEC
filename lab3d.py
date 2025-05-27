#!/usr/bin/env python3

#This script will return the free disk space on a Linux system's root directory
# Author ID: clee259

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"],
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE)
    output = p.communicate()
    return(output[0].decode('utf-8').strip())

if __name__ == '__main__':
    print(free_space())