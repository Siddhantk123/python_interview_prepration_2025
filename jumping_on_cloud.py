"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

def jumpingOnClouds(c):
    # Write your code here
    min_steps=0
    current_index=0
    while current_index < len(c):
        if current_index+2 < len(c) and c[current_index +2] != 1:
            min_steps +=1
            current_index +=2
        elif current_index+1 < len(c) and c[current_index +1] != 1:
            min_steps +=1
            current_index +=1
        else:
            current_index +=1
    return min_steps

print(jumpingOnClouds([0,0,1,0,0,1,0]))