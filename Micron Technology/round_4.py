# """
# input: 1234
# output:4321
# """

# def reverse_num(num):
#     rev=0
#     while num > 0:
#         digit = num%10
#         rev = rev*10+digit 
#         num=num//10
#     print(rev)

# reverse_num(1234)

# """
# input: "apple,grape.pineaple/orange\dragon:"
# output:[apple,grapes,pineapple,dragon,orange]
# """
# import re

# input= "apple,grape.pineaple/orange\dragon:"
# try:
#     word = re.findall(pattern=r"\w+", string=input)
# except Exception as e:
#     pass

# print(word)


<<<<<<< HEAD
class Alpha:
    def __init__(self):
        self.msg="Alpha"
    def abc(self):
        print(self.msg)
class Beta:
    def __init__(self):
        self.msg="Beta"
    def abc(self):
        print(self.msg)
class Gama(Beta, Alpha):
    def __init__(self):
        Beta.__init__(self) #initialize
        Beta.abc(self)
obj_gama = Gama()

