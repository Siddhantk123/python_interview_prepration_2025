import threading

def sum(a,b,**kwargs):
    n=0
    while n<100:
        print (f"sum:{a+b}")
        n+=1

def mul(a,b):
    n=0
    while n<100:
        print(f"mul: {a*b}")
        n+=1

thread_obj_1 = threading.Thread(target=sum, args=(1,2), kwargs={"c":3, "d":4})
thread_obj_2 = threading.Thread(target=mul, args=(1,2))

thread_obj_1.start()
thread_obj_2.start()

thread_obj_1.join()
thread_obj_2.join()
