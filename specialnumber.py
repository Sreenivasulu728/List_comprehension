def factorial(n):
    fact=1
    for x in range(1,n+1):
        fact*=x
    return fact
def special(n):
    num=n
    res=0
    while n!=0:
        rem=n%10
        n//=10
        res+=factorial(rem)
    # return res
    if num==res:
        return True
# n=143
# if n==special(n):
#     print('special number')
# else:
#     print('not')
    
# l=[]
# for x in range(100,301):
#     if special(x):
#         l.append(x)
# print(l)
for x in range(100,301):
    if special(x):
        print(x)
