class dunderMethod:
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject
    def __str__(self):
        return f"Name is:{self.name}\nSubject is: {self.subject}"
    
    def __len__(self):
        return len(self.name)
    
    def __add__(self,*args):
        return 5+5
    
    def __del__(self):
        print("called __del__() method")

obj = dunderMethod(name="Siddhant", subject="Programming")
print(obj)  #Name is:Siddhant
            #Subject is: Programming
print(len(obj)) # 8
print(obj.__dict__) #{'name': 'Siddhant', 'subject': 'Programming'}
print(obj+obj) #10