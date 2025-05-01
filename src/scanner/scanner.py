#!/usr/bin/env python3
# Ty Qualters & Daniel Uraimov
import hashlib
import os

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import io
from .files import FileOpener, DirectoryHandler
from .utils import *
from .keywords import KeywordChecker

def hash_file(filepath):
    # Hashes a file using SHA-256 and returns the hexadecimal digest
    sha256 = hashlib.sha256()

    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):  # Read in 4KB chunks
            sha256.update(chunk)

    return sha256.hexdigest()

def open_file():
    file_path = filedialog.askdirectory(title="Select a Folder")
    if file_path:
        return file_path
    return None

def do_scan(dirpath):
    # Everything we want to scan for should go in here!!
    results_file = open('results.txt', 'w')
    results_file.write('Scan results:\n')

    working_dir = DirectoryHandler(dirpath)
    for filename in working_dir.list_files():
        if not filename:
            continue

        print(filename)
        file = working_dir.get_file(filename)
        if not file or file.exists() is False:
            continue

        file.open_file()
        contents = file.read()
        results_file.write(f'File: {filename}\n')
        results_file.write(f'\tContains RTL character? {"Yes" if isrtlext(filename) else "No"}\n')
        results_file.write(f'\tMetadata: {str(get_metadata(working_dir.get_file_path(filename)))}\n')
        results_file.write(f'\tSHA-256 digest: {hash_file(working_dir.get_file_path(filename))}\n')

        if KeywordChecker.check_file(filename) == []:

            results_file.write(f'\tContains no suspicious keywords\n')
        else:
            results_file.write(f'The keywords found were: {KeywordChecker.check_file}')    
            
        file.close_file()

    results_file.close()

    messagebox.showinfo("Scan completed", "Results are saved to results.txt")

def scanner():

    if os.name == 'nt':
        from .pyads import ADS # https://github.com/RobinDavid/pyADS (License: MIT)


    print('IT 360 Folder Scanner\n')

    root = tk.Tk()
    root.title("IT 360 Folder Scanner by Daniel Uraimov and Ty Qualters")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    filename = tk.StringVar(value="No folder selected")

    # Function to handle folder selection
    def pick_file():
        dir = open_file()
        if dir:
            filename.set(dir)
            # Enable the Scan button when a folder is selected
            scan_button.config(state="normal")

    # Function to handle scanner
    def on_scan_button_click():
        fname = filename.get()
        do_scan(fname)
        scan_button.config(state="disabled")

    # Create buttons and labels
    ttk.Button(frm, text="Open Folder", command=pick_file).grid(column=0, row=0)
    ttk.Label(frm, textvariable=filename).grid(column=1, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)

    # Initially disabled Scan button
    scan_button = ttk.Button(frm, text="Scan", command=on_scan_button_click, state="disabled")
    scan_button.grid(column=1, row=1)

    root.mainloop()