# fact(n) = n! = 1 x 2 x 3 x 4 x ... x (n-2) x (n-1) x n
# fact(n) = fact(n-1) x n [n>0]
#           1             [n=0]

def func(n):
    if n == 0:
        return 1
    return func(n-1) * n

num = int(input("number = "))
print(func(num))

# time complexity O(n)