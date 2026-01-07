import copy

def two_sum_prob(nums, target):
    """
    return indices of two number whose addition is equal to target
    n1+n2=target
    """
    target_val = []
    for index,value in enumerate(nums):
        if target-value in nums:
            if target-value == value:
                continue
            if value not in target_val:
                print([index, nums.index(target-value)])
                target_val.append(target-value)

# two_sum_prob([1,2,4,6,2,7,8,3,9,5], 6)

"""
global and nonlocal keyword example
"""
# Nonlocal: useful only in case of nested function for globalising the variable
# Scope of modification is inside nested function/method
x=5
def outer_func():
    x= 10
    def inner_function():
        nonlocal x
        x+=10
        print(f"inside the inner_function: {x}") #inside the inner_function: 20
    inner_function()
    print(f"Outside inner function in outer function: {x}") #Outside inner function in outer function: 20

#outer_func()
#print(f'outside the outer function":{x}') #outside the outer function":5

#Global variable: scope of modification is universal
x=5
def outer_func_1():
    x= 10 #local variable
    def inner_function_1():
        global x
        x+=10
        print(f"inside the inner_function: {x}") #inside the inner_function: 15
    inner_function_1()
    print(f"Outside inner function in outer function: {x}") #Outside inner function in outer function: 10

# outer_func_1()
# print(f'outside the outer function":{x}') #outside the outer function":15

# diff b/t is and ==: 'is' is for address comparision(refrence), "==" for value comparision
# a=5
# b=5
# print(id(a))   # 140727522718760
# print(id(b))   # 140727522718760

# print(a is b) # True
# print(a == b) # True


# a=(1,2,3)
# b=(1,2,3)
# print(a == b)   # True  (values are equal)
# print(a is b)   # True (same object in memory)

# a = [1,2]
# b = [1,2]
# print(a == b)   # True  (values are equal)
# print(a is b)   # False (different objects in memory, *list*)
#dic1={"a":1, "b":1}
#dic2={"a":1, "b":1}
#
#print(dic1 == dic2) # True
#print(dic1 is dic2) # False
"""
Find Longest Substring Without Repeating Characters
Example inputs/outputs:
Input: "abcabcbb" → Output: 3 (substring "abc")
Input: "bbbbb" → Output: 1 (substring "b")
Input: "pwwkew" → Output: 3 (substring "wke")
"""

def find_longest_nonrepeating_substring(string):
    i,j=0,1
    word_len_dic={}
    word=string[i]
    while j <= len(string)-1:
        if string[j] not in word:
            word +=string[j]
            j+=1
        else:
            word_len_dic[word]= len(word)
            i=j
            j=j+1
            word=string[i]
    # print(word_len_dic)

    longest_len=0
    for word, length in word_len_dic.items():
        if length >= longest_len:
            longest_len= length
            longest_word = word
    return (longest_word, longest_len)


# print(find_longest_nonrepeating_substring("abcabcbb"))
# print(find_longest_nonrepeating_substring("bbbbb"))
# print(find_longest_nonrepeating_substring("pwwkew"))

def longest_common_prefix(word_list):
    if word_list[0]:
        first_word =  word_list[0]
    else:
        return f"List is empty"
    flag=False
    common_prefix=""
    for index, char in enumerate(first_word):
        for word in word_list[1:]:
            if char == word[index]:
                flag = True
            else:
                flag=False
        if flag == True:
            common_prefix += char
        else:
            return common_prefix


#print(longest_common_prefix(["flower","flow","flight"]))
# print(sorted(["flower","flow","flight"]))  #["flower","flow","flight"]

"""
Find longest possible palindrome substring
Input: "babad"
Output: "bab"  # or "aba"
"""
def longest_palidrome_substring(string):
    substring_len={}
    for i in range(len(string)):
        for j in range (len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                substring_len[string[i:j+1]] = len(string[i:j+1])
    
    longest_len=0
    for length in substring_len.values():
        if length > longest_len:
            longest_len = length
    for substring, length in substring_len.items():
        if length == longest_len:
            print(f"{substring},{longest_len}")
        
# longest_palidrome_substring("abhhbkl")
# longest_palidrome_substring("babad")
# longest_palidrome_substring("cbbbca")
# longest_palidrome_substring("accababccb")
# longest_palidrome_substring("ac")

"""
remove key: value pair from dictonary with retunn and without return value
"""
dic ={"a":1, "b":2, "c":3, "d":4, "e":5}
value = dic.pop("e")
# print(dic)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(value)  # 5

# del dic["d"]   # no return
# print(dic)     # {'a': 1, 'b': 2, 'c': 3}

"""
Move all zero to the end
input: arr[] = [1, 2, 0, 0, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
"""

def move_all_zero_end(arr):
    count_zero=0
    for value in arr:
        if value == 0:
            arr.remove(value)
            count_zero+=1
    print(arr+[0]*count_zero)

# move_all_zero_end([1, 2, 0, 4, 3, 0, 5, 0])

"""
Third largest element in an array of distinct elements
Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: 14
Explanation: Largest element is 20, second largest element is 16 and third largest element is 14
"""
def third_largest_using_inbuild_func(arr):
    arr = sorted(arr)
    print(arr[-3])
# third_largest_using_inbuild_func([1, 14, 2, 16, 10, 20])

def third_largest_without_using_inbuild_func(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] >= arr[j]:
                #swap
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
    print(arr[-3])
# third_largest_without_using_inbuild_func([1, 14, 2, 16, 10, 20])

"""
Maximum consecutive one’s (or zeros) in a binary array
Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
"""
def max_consicutive_0_or_1(arr):
    def max_consicutive_occurance(num, arr):
        counter=0
        counter_list=[]
        flag= False
        for value in arr:
            if value ==  num:
                flag=True
                counter +=1

            elif flag == True:
                counter_list.append(counter)
                flag=False
                counter=0

        counter_list.append(counter)
        # print(counter_list)
        return max(counter_list)

    count_1_max = max_consicutive_occurance(1, arr)
    count_0_max = max_consicutive_occurance(0, arr)
    print(max(count_1_max, count_0_max))

# max_consicutive_0_or_1([0, 1, 0, 1,0,0,0,0,0,1,1,1,0,0,0,0,1])

"""
Longest Increasing Subsequence (LIS)
Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = [30, 20, 10]
Output:1
Explanation: The longest increasing subsequences are [30], [20] and [10]

Input: arr[] = [2, 2, 2]
Output: 1
Explanation:  We consider only strictly increasing.

Input: arr[] = [10, 20, 35, 80]
Output: 4
Explanation: The whole array is sorted
"""
def longest_increasing_secquence(arr):
    inc_seq=[]
    all_inc_seq=[]
    for i in range(len(arr)):
        inc_seq.append(arr[i])
        copy_i = copy.copy(i)
        for j in range(i,len(arr)):
            if arr[j]>arr[copy_i]:
                inc_seq.append(arr[j])
                copy_i=j
        all_inc_seq.append(inc_seq)
        inc_seq=[]
    print(all_inc_seq) #[[3, 10, 20], [10, 20], [2, 20], [1, 20], [20]]
    longest_list = all_inc_seq[0]
    for index, value in enumerate(all_inc_seq):
        if len(longest_list) <= len(value):
            longest_list = value
    print(longest_list)
    print(len(longest_list))

#longest_increasing_secquence([30, 20, 22, 25]) 
# longest_increasing_secquence([3, 20, 9, 22, 25]) 
# longest_increasing_secquence([20,5,10,9,16,25,12,106,15,940]) 

"""
Finding sum of digits of a number until sum becomes single digit
Input: n = 1234 
Output: 1 
"""
def sum_of_digit_until_single(num):
    def sum_of_digit(num):
        sum=0
        while num >0:
            digit=num%10
            sum=sum+digit
            num=num//10
        return sum

    while len(str(num)) != 1:
        num = sum_of_digit(num)
    print(num)

# sum_of_digit_until_single(1234)
# sum_of_digit_until_single(5674)

'''
find first occuring unique charecter in the given string. 
'''
def find_first_occ_unique_char(string):
    string=string.lower()
    char_frq={}
    for char in string:
        if char not in char_frq:
            char_frq[char]=1
        else:
            char_frq[char] +=1
    for char in string:
        if char_frq[char] == 1:
            return char
    return -1

# print(find_first_occ_unique_char("Abcadbakl"))

"""
find nth occuring unique charecter in a string
i/p=Abcadbakl, occ_counter=2
o/p=d
"""
def find_first_occ_unique_char(string, occ_counter):
    string=string.lower()
    char_frq={}
    for char in string:
        if char not in char_frq:
            char_frq[char]=1
        else:
            char_frq[char] +=1
    counter=1
    for char in string:
        if char_frq[char] == 1:
            if counter == occ_counter:
                return char
            counter +=1
    return -1

# print(find_first_occ_unique_char(string="Abcadbakl", occ_counter=2))

#method2 slicing
def find_nth_occ_unique_char(string, occ_counter):
    counter=0
    for index,charecter in enumerate(string.lower()):
        current_char = charecter
        remaining_string = string[:index]+string[index+1:]
        if current_char not in remaining_string:
            counter +=1
            if counter == occ_counter:
                return current_char
    return -1

# print(find_nth_occ_unique_char(string="Abcadbakl", occ_counter=2))

print(find_first_occ_unique_char(string="Abcadbakl", occ_counter=2))
