import subprocess

# response = subprocess.run('ls', shell=True) #this will give error coz it is not recognized at windows
# response = subprocess.run('dir', shell=True)
# print(response)

host = "google.com"
ping = subprocess.Popen(["ping", "-n", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = ping.communicate()
print(out.decode('utf-8') if out else error.decode('utf-8'))

#different important packages are
"""
import pandas
import numpy
import requests     <- api
import beautifulsoup <- api for webscrapping
import subprocess
import re
import os
import serial
import time
import threading
import pdb
import json
"""