def armstrong(n):
    p=len(str(n))
    res=0
    num=n
    while n!=0:
        rem=n%10
        res+=rem**p
        n//=10
        if res==num:
           return True
# l=[]        
# for x in range(1,1001):
#    if armstrong(x):
#       l.append(x)
# print(l)   
l=[153,123,216,371,23]
li=list(filter(armstrong,l))
print(li)

    
