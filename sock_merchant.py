'''
https://www.hackerrank.com/challenges/sock-merchant/problem
'''

def sockMerchant(n, ar):
    # Write your code here
    colour_freq={}
    for colour in ar:
        if colour not in colour_freq:
            colour_freq[colour]=1
        else:
            colour_freq[colour]+=1
    
    total_pair=0
    for colour, freq in colour_freq.items():
        total_pair += freq//2
    return  total_pair

print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))