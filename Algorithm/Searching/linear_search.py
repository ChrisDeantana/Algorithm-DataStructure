def linear_search(A, key):
    n = len(A)              #O(1)
    index = 0               #O(1)
    while(index<n):         #O(n+1)
        if(A[index]==key):  #O(n)
            return index    #O(1)
        index = index + 1   #O(n)
    return -1               #O(1)

Array = [12, 4, 3, 51, 99]
print(linear_search(Array, 3))

# time complexity O(n)