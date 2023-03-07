# l=[]
# for x in range(1,11):
#     if x%2==0:
#        l.append(x) #| l+=[x]
       
# print(l)
l=dict(x for x in range(1,11)if x%2==0)
print(l)