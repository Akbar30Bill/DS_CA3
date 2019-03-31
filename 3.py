lll=int(input())
mdn=list(map(int,input().split()))
lst=[]
def fbz(index):
    global mdn,lst
    for i in range(index,lll):
        if lst[index] < lst[i]:
            return mdn[i]
    return -1
for i in range(lll):
    lst.append(mdn.count(mdn[i]))
print(mdn)
print(lst)
dorost = []
for i in range(lll):
    dorost.append(fbz(i))
stk=[]
sstk=[]
for i in range(lll-1 , 0 , -1):
    while True:
        print(stk)
        if len(stk) == 0:
            stk.append(i)
            sstk.append(-1)
            break
        else:
            if lst[i] > lst[stk[-1]]:
                stk.append(i)
                sstk.append(stk[-2]-stk[-1])
                break
            else:
                stk.pop()
print(dorost)
print(sstk)
