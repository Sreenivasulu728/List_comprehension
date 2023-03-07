def niven(n):
    num=n
    res=0
    while n!=0:
        rem=n%10
        n//=10
        res+=rem
    if num%res==0:
        return True
l=[12,11,14,20,21,23]
# for x in range(10,51):
#     if niven(x):
#         l.append(x)
# print(l)
li=list(filter(niven,l))
print(li)