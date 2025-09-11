def count_up_to(n):
    count = 1
    while count <= n:
        yield count   # returns value but keeps function state
        count += 1
gen = count_up_to(5)

for num in gen:
    print(num)
