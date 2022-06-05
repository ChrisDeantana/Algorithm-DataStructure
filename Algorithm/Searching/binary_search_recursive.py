# to perform binary search array must be sorted

def binary_search_recursive(A,key,l,r):
    if l > r:                                               #O(1)
        return -1                                           #O(1)
    else:                                                   #O(1)
        m = (l+r) // 2                                      #O(1)
        if A[m] == key:                                     #O(logn)
            return m                                        #O(1)
        elif key < A[m]:                                    #O(logn)
            return binary_search_recursive(A,key,l,m-1)     #O(logn)
        elif key > A[m]:                                    #O(logn)
            return binary_search_recursive(A,key,m+1,r)     #O(logn)

Array = [2, 3, 4, 10, 40]
print(binary_search_recursive(Array, 3, 0, 4))

# time complexity O(logn)