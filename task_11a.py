n = int(input())
factorial = 1
for i in range(2,n+1):
    factorial *= i
print(factorial)


# n = int(input)
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)



# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1)*n
# print(fac(5))