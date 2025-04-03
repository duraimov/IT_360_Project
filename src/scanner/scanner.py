#!/usr/bin/env python3
# Ty Qualters & Daniel Uraimov

import os

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askdirectory(title="Select a Folder")
    if file_path:
        return file_path
    return None

def scanner():

    if os.name != 'nt':
        print('This program does not support your operating system')
        exit(1)

    from .pyads import ADS # https://github.com/RobinDavid/pyADS (License: MIT)


    print('IT 360 Folder Scanner\n')

    root = Tk()
    root.title("IT 360 Folder Scanner by Daniel Uraimov and Ty Qualters")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    filename = tk.StringVar(value="No folder selected")

    def pick_file():
        dir = open_file()
        if dir:
            filename.set(dir)

    ttk.Button(frm, text="Open Folder", command=pick_file).grid(column=0, row=0)
    label = ttk.Label(frm, textvariable=filename).grid(column=2, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

    # print('Type \'help\' for a list of commands.')

    # while True:
    #     userInput = input('> ')
    #     print()
    #     match userInput:
    #         case 'help':
    #             print('Commands:')
    #             print('  - help [No Arguments]')
    #             print('  Displays a list of commands')
    #             print()
    #             print('  - summary [Directory] [(Optional) Output File]')
    #             print('  Performs a general analysis on a folder/directory')
    #             print()
    #             print('  - listads [File/Directory]')
    #             print('  Lists the Alternate Data Streams (ADS) of a file or directory')
    #             print()
    #             print('  - readads [File/Directory] [ADS] [(Optional) Output File]')
    #             print('  Reads the contents of an ADS')
    #             print()
    #             print('  - isrtlext [File]')
    #             print('  Checks if a file\'s extension is in RTL')
    #             print()
    #             print('  - issteg [File]')
    #             print('  Checks if a file has hidden contents')
    #             print()
    #             print('  - getperms [File/Directory]')
    #             print('  Recursively check permissions of a file or directory')
    #             print()
    #             print('  - getmeta [File]')
    #             print('  Get the metadata of a file')
    #             print()
    #             print('  - exit')
    #             print('  Close the program')
    #             print()
    #         case 'exit' | 'quit':
    #             print('Goodbye!')
    #             exit(0)
