# Daniel's file

import virustotal_python
import os
import requests

api_key = "6acabfc35b112fd6c58b626055a8fe288e0f5571f03b099d44ffe3380b21a72b"

def run_daniel():

    print('Daniel this is your main function. Whatever you want to do, just put it here.')


    return

   #checks for file extensions written right to left 
def isrtlext(file):
    rtl_override_present = False
    for char in file:
        if ord(char) == 0x202E: #if file name contains right to left unicode
            rtl_override_present = True
            break
    return rtl_override_present

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
    




