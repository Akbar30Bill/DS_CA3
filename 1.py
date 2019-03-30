a = int(input())
lst = list(map(int,input().split()))
lst.insert(0,10**10)
lst.append(10**10)
print(lst)
kkd = [0]*a
sizer,sizel,rt,lt = [0],[0],[],[]
for i in range(1,a+1):
    while True:
        if len(rt) == 0:
            sizer.append(i)
            break
        else:
            if lst[i] < lst[rt[-1]]:
                rt.append(i)
                try:sizer.append(rt[-1]-rt[-2])
                except:sizer.append(0)
                break
            else:
                rt.pop()
    print(rt)
for i in range(a,1,-1):
    while True:
        if len(lt) == 0:
            sizel.append(i)
            break
        else:
            if lst[i] < lst[lt[-1]]:
                lt.append(i)
                try:sizel.append(lt[-1]-lt[-2])
                except:sizel.append(0)
                break
            else:
                lt.pop()
    print(lt)
for i in range(a):
    print(max([sizel[i],sizer[i]]))
