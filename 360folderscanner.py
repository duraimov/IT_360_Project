#!/usr/bin/python3
# Ty Qualters & Daniel Uraimov

import os

if os.name != 'nt':
    print('This program does not support your operating system')
    exit(1)

import pyads # https://github.com/RobinDavid/pyADS (License: MIT)


print('IT 360 Folder Scanner\n')
print('Type \'help\' for a list of commands.')

while True:
    userInput = input('> ')
    print()
    match userInput:
        case 'help':
            print('Commands:')
            print('  - help [No Arguments]')
            print('  Displays a list of commands')
            print()
            print('  - summary [Directory] [(Optional) Output File]')
            print('  Performs a general analysis on a folder/directory')
            print()
            print('  - listads [File/Directory]')
            print('  Lists the Alternate Data Streams (ADS) of a file or directory')
            print()
            print('  - readads [File/Directory] [ADS] [(Optional) Output File]')
            print('  Reads the contents of an ADS')
            print()
            print('  - isrtlext [File]')
            print('  Checks if a file\'s extension is in RTL')
            print()
            print('  - issteg [File]')
            print('  Checks if a file has hidden contents')
            print()
            print('  - getperms [File/Directory]')
            print('  Recursively check permissions of a file or directory')
            print()
            print('  - getmeta [File]')
            print('  Get the metadata of a file')
            print()
            print('  - exit')
            print('  Close the program')
            print()
        case 'exit':
            print('Goodbye!')
            exit(0)
