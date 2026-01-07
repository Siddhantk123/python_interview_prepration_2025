# lis=[itr for itr in range(1,11) if itr%2==0]
# print(lis)

# dic={index:value for index, value in enumerate([1,2,3,4,5,6,7,8,9,10]) if value%2==0}
# print(dic)
# dict1={"a":1,
#      "b":2}

# dict2={"c":1,
#       "d":2}

# dict_final=dict1
# dict_final.update(dict2)
# print(dict_final)
string="abcabcbb"
final_substring={}

# def find_longest_substring_not_duplicate(string):
#     i,j=0,1
#     substring=string[i]
#     while j<len(string)-1:
#         if string[j] not in substring:
#             substring =substring + string[j]
#             j=j+1
#         else:
#             final_substring[substring]=len(substring)
#             i=j
#             j=j+1
#             substring=string[i]
#     print(final_substring)

# find_longest_substring_not_duplicate(string)

list_A=[1,2,3,4,5,8,9]
list_B=[4,5,6,7,8]
# intersection=[4,5,8]

def find_intersection(listA,listB):
    intersection=[]
    if len(list_A) != len(list_B):
        longest_list = listA if len(list_A) > len(list_B) else list_B
        smallest_list = listA if len(list_A) < len(list_B) else list_B
    else:
        longest_list=list_A
        smallest_list=list_B

    for value in longest_list:
        if value in smallest_list:
            intersection.append(value)
    print(intersection)

# find_intersection(list_A, list_B)

def logging(func):
    def wrapper(*args, **kwargs):
        print("pre_execution")
        func(*args, **kwargs)
        print("post_execution")
    return wrapper

@logging
def add(a,b):
    print(a+b)
# add(1,2)


