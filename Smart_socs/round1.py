
def logging(func):
    def wrapper(*args, **kwargs):
        print("pre condition")
        func(*args, **kwargs)
        print("post execution")
    return wrapper

@logging
def sum_of_num(x,y):
    print(x+y)

# sum_of_num(1,2)
import re
#need to reverse the string keeping the position of special chareter fix
original_str="sidd@ha#nt"
out="tnah@dd#is"

def rev_string_pos_sp_const(string):
    # converting each char of string into list
    lis_str = list(string) #['s', 'i', 'd', 'd', '@', 'h', 'a', '#', 'n', 't']
    #capture special char index and val in dictonary
    idx_spc={}
    for index,char in enumerate(lis_str):
        if re.search(pattern="\W", string=char): #check for special char
            idx_spc[index] = char

    #remove special char from list
    for value in idx_spc.values():
        lis_str.remove(value)

    #reverse lis_str
    lis_str=lis_str[::-1]

    # insert special charecter at there original position
    for index, value in idx_spc.items():
        lis_str.insert(index, value)
    
    #convert list to string
    final_string = "".join(lis_str)
    print(final_string)

rev_string_pos_sp_const("sidd@ha#nt")
rev_string_pos_sp_const("sidd@$ha#n&t")

import copy
list_1=["a",["b","c"]]
shallow_copy = copy.copy(list_1)
deep_copy = copy.deepcopy(list_1)

#modifying original list_1
list_1[1][0]="d"
# print(list_1)       #['a', ['d', 'c']] got modified
# print(shallow_copy) #['a', ['d', 'c']] got modified
# print(deep_copy)    #['a', ['b', 'c']] same as original

list_2=["a",["b","c"]]
shallow_copy=copy.copy(list_2)
deep_copy=copy.deepcopy(list_2)

#modify original list 2
list_2[0]="d"
# print(list_2)      #['d', ['b', 'c']] got modified
# print(shallow_copy)#['a', ['b', 'c']] same as original
# print(deep_copy)   #['d', ['b', 'c']] same as original

#Generator
def count_up_to(n):
    count=0
    while count < n+1:
        yield count
        count +=1

# gen = count_up_to(5)

# print(next(gen))
# print(next(gen))
# for val in gen:
#     print(val)

# import re
# str= (test_get_log)_t(1234)
# c=re.search(str, pattern="(\w)+_t(\d+)")
# text=c.group(1)
# number=c.group(2)

# difference between re.search() and re.match() in regex
'''
re.match: try to match the pattern only at the begining of the string.
re.search: try to serach and  match in full string 
'''
str_1 = "hello world"
match_1 = re.match(r"(hello)", str_1)
# print(match_1.group(0)) #hello
match_2 = re.match(r"(world)", str_1)
# print(match_2)          # None

#re.search--> is recommended to use
match_3 = re.search(r"hello", str_1)
# print(match_3.group(0)) #hello
match_4 = re.search(r"world", str_1)
# print(match_4.group(0)) #world

class abc:
    c=4
    @classmethod
    def class_method(cls):
        print(cls.c)

    @staticmethod
    def static_method(a,b):
        print(a*b)

# obj_abc=abc()
# obj_abc.class_method()
# obj_abc.static_method(1,2)

# class Father:
#     def father_name(self):
#         print("father name is x")

# class child(Father):
#     def __init__(self):
#         super().father_name()

# obj_child= child()

#method overloading
'''
on the basis of different number of parameter passed to a method from the same class,
it behaves differentially
python does not support this traditional approach instead it consider the last
method defined with the same name inside the class.
'''

class Area:
    def method_area(self, s):
        return s*s
    def method_area(self, l,b,h):
        return l*b*h

obj_area = Area()
# area=obj_area.method_area(2) #TypeError: Area.method_area() missing 2 required positional arguments: 'b' and 'h'
# print(area)
   

#meathod overriding
"""
child class override the implementation of method present in both parent &child class
"""
class Father:
    def show_name(self):
        print("father name is x")
    def show_feature_father(self):
        print("I am a father of y")

class Child(Father):
    def show_name(self):
        print("child name is y")

obj_child = Child()
# obj_child.show_name() #child name is y, -----> method override happen
# obj_child.show_feature_father() #I am a father of y