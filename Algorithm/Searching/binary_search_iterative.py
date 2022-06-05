# to perform binary search array must be sorted

def binary_search_iterative(A,key):
    l = 0                    #O(1)
    r = len(A) - 1           #O(1)
    while l<=r:              #O(n/2) = O(logn)
        m = (l + r) // 2     #O(logn)
        if A[m] == key:      #O(logn)
            return m         #O(1)
        elif key < A[m]:     #O(logn)
            r = m-1          #O(1)
        elif key > A[m]:     #O(logn)
            l = m+1          #O(1)
    return -1                #O(1)

Array = [2, 3, 4, 10, 40]
print(binary_search_iterative(Array,2))

# time complexity O(logn)
