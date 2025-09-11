#instancemethod, classmethod, staticmethod
class Area:
    def __init__(self,side):   #instance method, self points to instance of the class
        self.side=side
    
    @classmethod
    def square(cls, s):        # class point to class
        # print(cls.side)
        print(f"Area of square: {s*s}")
    
    @staticmethod
    def rectangle(len, width):   # works as a normal function without self or cls
        print(f"Area of rectangle: {len*width}")

obj = Area(5)

obj.square(10)                    #Area of square: 100
Area(5).square(s=10)              #Area of square: 100

obj.rectangle(len=2, width=3)     #Area of rectangle: 6
Area(5).rectangle(len=2, width=3) #Area of rectangle: 6