def count_up_to(n):
    count = 1
    while count <= n:
        yield count   # returns value but keeps function state, its like a factory which give product on demand not all at once
        count += 1
gen = count_up_to(5)

print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3

for num in gen:
    print(num)
