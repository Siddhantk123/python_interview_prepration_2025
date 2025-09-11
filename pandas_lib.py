import pandas as pd

'''
it will return data frame when you read an excel
'''
data_frame = pd.read_excel("output.xlsx").to_json()

#create data fram to post in excel
request_data_frame={
    "Name":["siddhant", "Adarsh", "Arun"],
    "Age":[27,28,32]
}

df=pd.DataFrame(request_data_frame) #step 1
df.to_excel("dummy.xlsx")           #step 2
"""
Name       Age
Siddhant   27
Adarsh     28
Arun       32
"""