N,K=list(map(int,input().split()))
lst=list(map(int,input().split()))
tmp = 0
stc = [0]*K
sum = 0
# def pls(i):
#     global lst,K
#     for x in range(K):
#         try:
#             if lst[i+x] == 2:
#                 lst[i+x] = 0
#             elif lst[i+x] == 1:
#                 lst[i+x] = 2
#             elif lst[i+x] == 0:
#                 lst[i+x] = 1
#         except:
#             pass
# for i in range(len(lst)):
#     while not lst[i] == 0:
#         pls(i)
#         tmp += 1
# print(tmp)

for i in range(len(lst)):
    z = (3-(sum+lst[i])%3)%3
    stc.append(z)
    sum+=z
    sum-=stc[-K]
    tmp+=z
print(tmp)
