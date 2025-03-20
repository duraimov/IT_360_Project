#!/usr/bin/env python3

from .files import FileOpener, DirectoryHandler

def testing():

    from .daniel_testfile import run_daniel
    run_daniel()

    # --------------
    # print('Test 1: Open file')
    # file = FileOpener('testfile.txt')
    # file.open_file()
    # file.print()
    # file.close_file()

    # --------------
    # print('Test 2: Open directory')
    # dir = DirectoryHandler('.')
    # print(f'Dirname: {dir.dirname}')

    # ---------------

    # print('Test 3: Whatever this is')
    # keywords = ["repeat"]
    # results = {}
    # filepath = "testfile.txt"

    # with open(filepath, 'r', encoding='utf-8') as file:
    #     for line_num, line in enumerate(file, 1):
    #         matches = []
    #         for keyword in keywords:
    #             if keyword.lower() in line.lower():
    #                 matches.append(keyword)
            
    #         if matches:
    #             results[line_num] = matches

    # print(results)