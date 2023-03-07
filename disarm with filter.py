def disarm(n):
    temp=n
    summ=0
    p=len(str(n))
    while n>0:
        rem=n%10
        summ=summ+rem**p
        n=n//10
        p-=1
    if summ==temp:
        return True
            
l=[135, 175, 518, 598,231,222]
li=list(filter(disarm,l))
print(li)

# for x in range(1,1001):
#     if disarm(x):
#         l.append(x)
# print(l)