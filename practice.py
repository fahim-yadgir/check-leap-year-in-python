# num = 123456

# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num//10

# print(rev)


# num = '123456789'

# print(num[::-1])

# string = 'fahim'

# rev = ''

# for i in string:
#     rev = i + rev

# print(rev)

n = 123456

rev = 0

for i in range(len(str(n))):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)