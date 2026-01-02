"""

"""
# class A:
#     def __init__(self, msg):
#         self.msg=msg
#     def show_msg(self):
#         print (self.msg)

# class B(A):
#     def __init__(self,msg):
#         super().__init__(msg)
    
# obj_classB = B(msg="obj of class B")
# obj_classB.show_msg(

"""
lis =[1,2,3,4,1,2,3,4]
convert = [1,1,2,2,3,3,4,4]
convert=[1,2,3,4]
"""
def convert(lis):
    dic={}
    final_list_2=[]
    final_list_1=[]
    for element in lis:
        if element not in dic:
            dic[element]=1
        else:
            dic[element]+=1
    # print(dic)
    
    for element,value in dic.items():
        final_list_2.append(element)
        final_list_1.extend([element]*value)
    print(final_list_2)
    print(final_list_1)

convert([1,2,3,4,1,2,3,4])

        