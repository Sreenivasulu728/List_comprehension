# l=[[1,2,3],[10,20,30],[5,10,15]]
# res=set(res.append[i][j]for i in range(len(l))for j in range(len(l[i])))
# print(res)
s='THE QUICK BROWN FOX JUMPS OVER LAZY DOG'
words=s.split()
l=[[x,len(x)]for x in words]
print(l)
# l=[]
# # for x in range(len(words)):
# for x in words:
#     l.append([x,len(x)])
# print(l) 