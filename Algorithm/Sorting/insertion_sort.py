def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue

Array = [2,3,1,11,6,4]
insertion_sort(Array)
print(Array)

# time complexity , Comparison: 1 + 2 + 3 + ... + n-1 = n(n-1)/2 = O(n^2)
#                   Swapping: 1 + 2 + 3 + ... + n-1 = n(n-1)/2 = O(n^2)
