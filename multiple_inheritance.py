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


class D:
    def __init__(self, msg):
        self.msg = msg
    def show_msg_D(self):
        print(f"Showing msg from class D: {self.msg}")

class E:
    def __init__(self, msg):
        self.msg = msg
    def show_msg_E(self):
        print(f"showing msg from class E: {self.msg}")

class F(D,E):
    def __init__(self, msg):
        self.msg = msg
    def show_msg_F(self):
        print(f"showing msg from class F: {self.msg}")

obj_F = F(msg="object of class F")
obj_F.show_msg_D()
obj_F.show_msg_E()
obj_F.show_msg_F()