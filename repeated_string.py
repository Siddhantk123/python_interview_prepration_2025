'''
https://www.hackerrank.com/challenges/repeated-string/problem
'''

def repeatedString(s, n):
    # Write your code here
    count_a_substring = s.count("a")
    sectors = n//len(s)
    remaining_char_count = n%len(s)
    total_a = sectors*count_a_substring
    
    for index in range(remaining_char_count):
        if s[index] == "a":
            total_a +=1
    return total_a

print(repeatedString("a", 1000000000000))
print(repeatedString("aba", 10))

