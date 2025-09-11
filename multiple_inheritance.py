class A:
    def __init__(self, msg):
        self.msg=msg
    def show_A(self):
        print(f"showing msg from class A: {self.msg}")
    
class B(A):
    def __init__(self, msg):
        self.msg=msg
    def show_B(self):
        print(f"showing msg from class B: {self.msg}")
    
class C(B):
    def __init__(self, msg):
        self.msg=msg
    def show_C(self):
        print(f"showing msg from class C: {self.msg}")
    
obj_C= C(msg="object of class C")
obj_C.show_C()
obj_C.show_B()
obj_C.show_A()