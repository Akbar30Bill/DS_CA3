lll=int(input())
mdn=list(map(int,input().split()))
lst=[]
for i in range(lll):
    lst.append(mdn.count(mdn[i]))
stk=[]
sstk=[]
for i in range(lll-1 , -1 , -1):
    while True:
        if len(stk) == 0:
            stk.append(i)
            sstk.append(-1)
            break
        else:
            if lst[i] < lst[stk[-1]]:
                stk.append(i)
                sstk.append(mdn[stk[-2]])
                break
            else:
                stk.pop()
sstk.reverse()
print(*sstk)
