lll=int(input())
mdn=list(map(int,input().split()))
lst=[0]*lll
def fbz(index):
    global mdn,lst
    for i in range(index,lll):
        if lst[index] < lst[i]:
            return mdn[i]
    return -1
for i in range(lll):
    lst[i] = mdn.count(mdn[i])
for i in range(lll):
    print(fbz(i),end=" ")
print()
