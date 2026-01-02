"""
class and object
"""
import requests

class TestRail:
    def __init__(self, base_url, usr_name, password):
        self.usr_name= usr_name
        self.password= password
        self.url= base_url

    def get_run_data(self):
        response = requests.get(url=f"{self.url}/api/1").json()
        print("Please find resonse data")
        return response

##instance of a class(i.e onbject)
# test_rail=TestRail(base_url="https://testrail.com", usr_name="msiddhant23", password="@123Erp")
# test_rail.get_run_data()

"""
inheritance: child class inherit the properties of a parent class
"""

class Toyota:
    def __init__(self, brand_name):
        self.brand_name=brand_name

    def post_brand_name(self):
        print(f"Brand Name: {self.brand_name}")

class Innova(Toyota):
    def feature(self):
        super().post_brand_name()
        print("Less expensive than Fortuner in India\n"
              "Comfortable car")

class Fortuner(Toyota):
    def feature(self):
        print("More expensive than Innova in India\n"
              "Comfortable car")
        
# # obj creation: will create child class object
# print("Data of Innova")
innova_obj=Innova(brand_name="Toyota")
# innova_obj.post_brand_name()
innova_obj.feature()

# print("\nData of Fortuner")
# fortuner_obj=Innova(brand_name="Toyota")
# fortuner_obj.post_brand_name()
# fortuner_obj.feature()

# class, object,inheritance and polymorphism
class Father:
    def show_father_name(self):
        print("Father's name is: Mr B.N Mishra")

class Mother:
    def show_mother_name(self):
        print("Mother's name is: Mrs Indu Mishra")
class child1(Father,Mother):
    def __init__(self, name):
        self.name = name
    def child1_name(self):
        print(f"child1 name: {self.name}")
    
class child2(Father,Mother):
    def __init__(self, name):
        self.name = name
    def child2_name(self):
        print(f"child1 name: {self.name}")

# obj_child1 = child1(name="Siddhant")
# obj_child1.child1_name()
# obj_child1.show_father_name()
# obj_child1.show_mother_name()

# obj_child2 = child2(name="Adarsh")
# obj_child2.child2_name()
# obj_child2.show_father_name()
# obj_child2.show_mother_name()
"""
Polymorphism: available in many form: same function in 2 class has different meaning
"""
class Innova:
    def features(self):
        print("1. Less expensive than Fortuner in India\n"
              "2. Comfortable car\n")

class Fortuner:
    def features(self):
        print("1. More expensive than Innova in India\n"
              "2. Comfortable car")

# Innova().features()
# Fortuner().features()

"""
encapsulation: wrapping of data and asociated features in single unit
"""
class bankAccount:
    def __init__(self):
        self.balance=0
    def deposit_amount(self, amount):
        print("DEPOSITE AMOUNT")
        self.balance +=amount
    def withdraw_amount(self, amount):
        print("WITHDRAW AMOUNT")
        if amount > self.balance:
            print("Please enter valid amount\n"
                 f"Available balance is: {self.balance}")
        else:
            self.balance -=amount
            print(f"Pleae collect amount: {amount}\n")
    def check_balance(self):
        print(f"Available balance is: {self.balance}")

# bank=bankAccount()
# bank.deposit_amount(amount=500000)
# bank.check_balance()
# bank.withdraw_amount(amount=200000)
# bank.check_balance()
# bank.deposit_amount(amount=200000)
# bank.check_balance()
