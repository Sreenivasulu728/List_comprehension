def prime(n):
    if n>1:
        for x in range(2,n//2+1):
            if n%x==0:
                return False
        return True
l=[2,3,4,5,6,7,8,11]
li=list(filter(prime,l))
print(li)