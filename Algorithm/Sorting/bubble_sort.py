def bubble_sort(A):
    n = len(A)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

A = [3,5,8,9,6,2]
bubble_sort(A)
print(A)

# time complexity , Comparison: 1 + 2 + 3 + ... + n-1 = n(n-1)/2 = O(n^2)
#                   Swapping: 1 + 2 + 3 + ... + n-1 = n(n-1)/2 = O(n^2)