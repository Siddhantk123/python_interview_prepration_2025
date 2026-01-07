# def two_sum_prob(nums, target):
#     """
#     return indices of two number whose addition is equal to target
#     n1+n2=target
#     """
#     target_val = []
#     for index,value in enumerate(nums):
#         if target-value in nums:
#             if target-value == value:
#                 continue
#             if value not in target_val:
#                 print([index, nums.index(target-value)])
#                 target_val.append(target-value)

# two_sum_prob([1,2,4,6,2,7,8,3,9,5], 6)

# nonlocal variable

# x= 5
# def outer_function():
#     x=10
#     def inner_function():
#         nonlocal x
#         x +=10
#         print(f"printing value of x from inner function: {x}") #20
#     inner_function()
#     print(f"printing value of x outside inner but inside outer: {x}") #20

# outer_function()
# print(f"printing value of x from outside the outer function: {x}") #5


#global function
# x= 5
# def outer_function():
#     x=10
#     def inner_function():
#         global x
#         x +=10
#         print(f"printing value of x from inner function: {x}") #15
#     inner_function()
#     print(f"printing value of x outside inner but inside outer: {x}") #10

# outer_function()
# print(f"printing value of x from outside the outer function: {x}") #15

a= 5
b=5
# print(a is b)
# print(a == b)
# print(id(a)) #140709437220088
# print(id(b)) #140709437220088

list_1 = [1,2,3]
list_2= [1,2,3]
# print(id(list_1))
# print(id(list_2))
# print(list_1 is list_2)
# a= 5
# b=5
# print(a is b)
# print(a == b)
# print(id(a))
# print(id(b))

# list_1 = [1,2,3]
# list_2= [1,2,3]
# print(id(list_1))
# print(id(list_2))
# print(list is list_2)
# print(list_1 == list_2)

# dict_1={"a":1,
#         "b":2
#         }

# dict_2={"a":1,
#         "b":2
#         }
# print(id(dict_1))
# print(id(dict_2))
# print(dict_1 is dict_2)
# print(dict_1 == dict_2)

# def longest_common_prefix(word_list):
#     common_prefix=""
#     if word_list == []:
#         print("No element present in word_list")
#         return
#     first_word = word_list[0]
#     flag = False
#     for index,value in enumerate(first_word):
#         for word in word_list[1:]:
#             if index > len(word)-1:
#                 flag=False
#             if value == word[index]:
#                 flag = True
#             else:
#                 flag = False
#         if flag == True:
#             common_prefix += value
#         if flag == False:
#             return common_prefix

# common_prefix = longest_common_prefix(["flower","flow","flght"])
# common_prefix = longest_common_prefix(["flower","flow","flows"])
# print(common_prefix)

"""
Find longest possible palindrome substring
Input: "babad"
Output: "bab"  # or "aba"
"""

def longest_possible_palidrome_substring(string):
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
# def longest_possible_palidrome_substring(string):
#     substring_len={}
#     for i in range(len(string)):
#         for j in range (len(string)):
#             if string[i:j+1] == string[i:j+1][::-1]:
#                 substring_len[string[i:j+1]] = len(string[i:j+1])
    
#     longest_len=0
#     for length in substring_len.values():
#         if length > longest_len:
#             longest_len = length
#     for substring, length in substring_len.items():
#         if length == longest_len:
#             print(f"{substring},{longest_len}")

# longest_possible_palidrome_substring("babad")

"""
Third largest element in an array of distinct elements
Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: 14
Explanation: Largest element is 20, second largest element is 16 and third largest element is 14
"""
# method1
def m1_3rd_largest(array):
    return sorted(array)[-3]

# third_largest = m1_3rd_largest([1, 14, 2, 16, 10, 20])
# print(third_largest)

#method 2
# def m2_3rd_largest(array):
#     #sorting
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if array[j] < array[i]:
#                 array[i],array[j]=array[j],array[i]
#     print(array[-3])

# third_largest = m1_3rd_largest([1, 14, 2, 16, 10, 20])
# print(third_largest)

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
def longest_increasing_secquence(array):
    all_inc_seq=[]
    for i in range(len(array)):
        inc_seq=[array[i]]
        cap_i = i
        for j in range(i+1, len(array)):
            if array[j]>array[cap_i]:
                inc_seq.append(array[j])
                cap_i=j
        all_inc_seq.append(inc_seq)

    longest_len=0
    for seq in all_inc_seq:
        if len(seq)>longest_len:
            longest_len=len(seq)

    for seq in all_inc_seq:
        if len(seq) == longest_len:
            print(seq)

# longest_increasing_secquence([3, 10, 2, 1, 20])
# longest_increasing_secquence([2,2,2])
# longest_increasing_secquence([10, 20, 35, 80])

input= "apple,grape.pineaple/orange\\dragon:"
# output = ["apple","grape","pineapple","orange","dragon"]
# import re
# list_fruits = re.findall(pattern=r"\w+", string=input)
# print(list_fruits)

class Alpha:
    def abc_alpha(self):
        print("Alpha")
class Beta:
    def abc_beta(self):
        print("Beta")                 
class Gama(Beta, Alpha):
    def abc_gamma(self):  
        print("Gamma")
        
# obj_gama = Gama()
# obj_gama.abc_alpha()
# obj_gama.abc_beta()
# obj_gama.abc_gamma()

in_lis =[1,2,3,4,1,2,3,4]
op_convert = [1,1,2,2,3,3,4,4]
op_convert=[1,2,3,4]

# print(sorted(in_lis))
# print(list(set(in_lis)))

# dic1={"c":3}
# dic2={"a":1,
#       "b":2,
#       **dic1}
# print(dic2) #{'a': 1, 'b': 2, 'c': 3}

# to run cmd on cli
# example of python is platfor dependent
import os
# os.system(command="ls")
# os.system(command="dir")

dir = os.listdir()
for file in dir:
    if file.endswith(".py"):  #string.endswith() works
        print(file, end=",")

# os.system(command="dir")

# def even(num):
#     if num % 2 == 0:
#         return num
    
# even = list(map(even,range(1,101)))
# print(even)

# add = lambda x,y: x+y
# print(add(2,3))

list_1 = [1,2,3,4]
list_2 = [1,2,3,4]

# print(id(list_1)) #2906727133184
# print(id(list_2)) #2906731723840

tuple_1=(1,2,3,4)
tuple_2=(1,2,3,4)

# print(id(tuple_1)) #1810295269360
# print(id(tuple_2)) #1810295269360
# a=3
# b=3
# print(id(a)) #140709001405624
# print(id(b)) #140709001405624
