# Author: Jordan Brisley
# Date: 09/19/2023
# CS325-02 Project 1

import sys
import requests

URL = sys.argv[1]       #Saving the URL argument giving by user 

page = requests.get(URL)                    #grabbing the source code from URL provivded by user

output = open("output.txt", "w")            #writing the HTML given from the URL provided to output.txt
output.write(page.text)
output.close()                              #closing output.txt
