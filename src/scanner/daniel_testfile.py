# Daniel's file

import virustotal_python
import os


def run_daniel():

    print('Daniel this is your main function. Whatever you want to do, just put it here.')


    return

def isrtlext(file):
    rtl_override_present = False
    for char in file:
        if ord(char) == 0x202E:
            rtl_override_present = True
            break
    return rtl_override_present

def toVirusTotal(file):
    return    




