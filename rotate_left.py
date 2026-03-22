def rotateLeft(d, arr):
    # Write your code here
    end_element = arr[:d]
    for index in range(d,len(arr)):
        arr[index-d] = arr[index]
    arr[-d:]=end_element
    return arr

print(rotateLeft(2, [1,2,3,4,5]))
