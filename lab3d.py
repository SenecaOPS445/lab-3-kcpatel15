#!/usr/bin/env python3
# Author ID: kcpatel15

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        shell=True
    )
    output, _ = p.communicate()
    free_space_str = output.decode('utf-8').strip()
    return free_space_str

if __name__== '__main__':
    print(free_space())