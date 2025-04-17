# Daniel's file

import virustotal_python
import os
import requests
import hashlib

#TODO: add functionality for checkbox whether you want to upload to virustotal, if yes, need api key

def run_daniel():

    # hash = hash_file("C:\\Users\\thebe\\OneDrive\\Desktop\\test.txt")
    # print(hash)


    # rtlext = isrtlext("C:\\Users\\thebe\\OneDrive\\Desktop\\test.txt")
    # print (rtlext)

    #vt = toVirusTotal("C:\\Users\\thebe\\OneDrive\\Desktop\\test.txt")
    #print(vt)

    results = search("C:\\Users\\thebe\\OneDrive\\Desktop\\test.txt", "C:\\Users\\thebe\\OneDrive\\Desktop\\keywords.txt")
    
    print(results)


    return

def toVirusTotal(file):

    
    url = "https://www.virustotal.com/api/v3/files"
    
    # Open the file in binary mode
    with open(file, 'rb') as new_file:
        # Set the headers with your API key
        headers = {"x-apikey": api_key}
        
        # Upload the file
        response = requests.post(url, headers=headers, files={"file": file})
        
        # Check the response status
        if response.status_code == 200:
            print("File uploaded successfully!")
            return response.json()  # Return the JSON response with the scan details
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    

def hash_file(filepath):
    #Hashes a file using SHA-256 and returns the hexadecimal digest
    sha256 = hashlib.sha256()
    
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):  # Read in 4KB chunks
            sha256.update(chunk)
    
    return sha256.hexdigest()


def search(file_path, keyword_path):
    with open(keyword_path, 'r') as kf:
        keywords = [line.strip() for line in kf if line.strip()]

    # Read the main file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Search for keywords in each line
    for i, line in enumerate(lines, start=1):
        for keyword in keywords:
            if keyword in line:
                print(f'Keyword "{keyword}" found on line {i}: {line.strip()}')




