def linear_sort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1,n):
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp

Array = [2,3,1,11,6,4]
linear_sort(Array)
print(Array)

# time complexity , Comparison: 1 + 2 + 3 + ... + n-1 = n(n-1)/2 = O(n^2)
#                   Swapping: 1 + 1 + 1 + + ... + 1 = n-1 = O(n)