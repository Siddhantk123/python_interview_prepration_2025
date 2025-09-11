def func(*args,**kwargs):
    print(f"*args: {args}")
    print(f"**kwargs: {kwargs}")

func(5,6) 
#*args: (5, 6) <-Tupple
# **kwargs: {} <- dictonary

# func(a=10, b=20)
#**kwargs: {'a': 10, 'b': 20}
