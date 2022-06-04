# sum(n) = 1 + 2 + 3 + 4 + ... + (n-2) + (n-1) + n -> n(n+1)/2
# sum(n) = sum(n-1) + n [n>1]
#          1            [n=1]

def sum_recursive(n):
    if n == 1:
        return 1
    return sum_recursive(n-1) + n

num = int(input("number = "))
print(sum_recursive(num))

# time complexity O(n)