list1=[1,1,2,3,5,1,0,3,10,"ab"]
output=[1,3] #are the repeated charecter

li=[]
repeted=[]
for val in list1:
    if val not in li:
        li.append(val)
    elif val not in repeted:
        repeted.append(val)
# print(list(set(repeted)))
print(repeted)

# import json
# val_freq={}
# for val in list1:
#     if val not in val_freq:
#         val_freq[val]=1
#     else:
#         val_freq[val] +=1
# print(json.dumps(val_freq, indent=2))

# import re
# str1="mishra.siddhant003@gmail.com"

# search = re.search(r"(\d+)", string=str1).group(1)
# if search:
#     print(search)

str1 = "abCDABCDeuhriUEYREyrabcdeyr"
#freq of below from above string
# abcd
# eyr
def find_freq_of_substring(string:str, substring:list):
    final_dic={}
    string_lower = str1.lower()
    for sub_string in substring:
        final_dic[sub_string]=0

    for index in range(0,len(string_lower)):
        for sub_string in final_dic:
            if string_lower[index:index+len(sub_string)] == sub_string.lower():
                final_dic[sub_string] +=1
    print(final_dic)

string = "abCDABCDeuhriUEYREyrabcdeyr"
substring=["abcd","eyr","yra","De"," "]
# find_freq_of_substring(string,substring)

#linux command
# ls, pwd, cd <path>, /root, cd /home cd -, mkdir siddhant, touch file1, 
# find / -iname ".log"
# grep -inr

# ip1=10.116.66.101
# location: /home/siddhant/flashing_data

# ip2=10.116.43.101
# location= /home/siddhant

# ssh 10.116.66.101

# scp -r /home/siddhant/flashing_data root@10.116.43.101:/home/siddhant
# how to setup root user in linux?
# Ans:
# Create a new user
# cmd: sudo adduser username
# This will:
# Create home directory /home/username
# Ask for password
# Set basic details

# to switch between user:
# su username

# Delete a user
# sudo deluser username

# how to access any ip:
#Ans: usinf ssh command, eg: ssh <ip_address>






