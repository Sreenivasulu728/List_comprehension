def palindrome(n):
    num=n
    res=0
    while n!=0:
        rem=n%10
        n//=10
        res=res*10+rem
    if res==num:
        return True
# l=[]
# for x in range(10,101):
#     if palindrome(x):
#         l.append(x)
# print(l)
#l=[11,12,14,22,33,23,35]
print(list(filter(palindrome,[11,12,14,22,33,23,35])))
