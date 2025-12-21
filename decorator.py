import copy

def add_logging(func):
    def wrapper(*args, **kwargs):
        print("pre-execution")
        func(*args, **kwargs)
        print("post-execution")
    return wrapper

@add_logging
def add(a,b):
    print(a+b)

#add(5,6)

@add_logging
def check_palindrome(number):
    num = copy.deepcopy(number)
    rev=0
    while num > 0:
        digit =  num % 10
        rev = rev*10 + digit
        num = num//10

    if rev == number:
        print("palindrome number")
    else:
        print("not a palindrome number")

#check_palindrome(102)

@add_logging
def fibonaci_series(number):
    lis=[0,1]
    itr=2
    while itr <= number:
        value = lis[-1]+lis[-2]
        lis.append(value)
        itr+=1
    print(lis)
    #way 2
    # for itr in range(2,number+1):
    #     if itr in [0,1]:
    #         pass
    #     else:
    #         lis.append(lis[itr-1]+lis[itr-2])
    # print(lis)

fibonaci_series(5)
#[0, 1, 1, 2, 3, 5] number=5

