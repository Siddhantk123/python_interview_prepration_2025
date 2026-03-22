def count_up_to(n):
    count = 1
    while count <= n:
        yield count   # returns value but keeps function state, its like a factory which give product on demand not all at once
        count += 1
gen = count_up_to(5)

print(gen) # <generator object count_up_to at 0x0000028A39EE9490>
print(next(gen)) #1
print(next(gen)) #2

print("remaining")
for num in gen:
    print(num) #3, 4, 5

# print(next(gen)) #error: StopIteration

def count_up_infinite():
    count=1
    while True:
        yield count
        count+=1
gen = count_up_infinite()
print("count infinite series")
print(next(gen))
print(next(gen))
print(next(gen))

itr = 1
for count in gen:
    print(count)
    if itr == 10:
        break
    itr+= 1


