import subprocess

response = subprocess.run('ls', shell=True) #this will give error coz it is not recognized at windows
response = subprocess.run('dir', shell=True)
# print(response)

# for windows
host = "google.com"
process = subprocess.Popen(["cmd", f"ping {host}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = process.communicate()
print(out.decode('utf-8') if out else error.decode('utf-8'))

#for windows
# process = subprocess.Popen(
#     ["cmd", "/c", "dir"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# output, _ = process.communicate()
# print(output)

#different important packages are
"""
import pandas
import numpy
import requests     <- api
import beautifulsoup <- api for webscrapping
import subprocess
import serial
import re
import os
import time
import threading
import pdb
import json
"""