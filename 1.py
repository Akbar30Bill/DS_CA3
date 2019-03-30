a = int(input())
lst = list(map(int,input().split()))
lst.insert(0,10**10)
lst.append(10**10)
# print(lst)
sizer,sizel,rt,lt = [],[],[],[]
for i in range(1,a+1):
    while True:
        if len(rt) == 0:
            rt.append(i)
            sizer.append(i - 1)
            break
        else:
            if lst[i] < lst[rt[-1]]:
                rt.append(i)
                try:sizer.append(rt[-1]-rt[-2])
                except:sizer.append(0)
                break
            else:
                rt.pop()
    # print(rt)
for i in range(a,0,-1):
    while True:
        if len(lt) == 0:
            lt.append(i)
            sizel.append(a - i)
            break
        else:
            if lst[i] < lst[lt[-1]]:
                lt.append(i)
                try:sizel.append(lt[-2]-lt[-1])
                except:sizel.append(0)
                break
            else:
                lt.pop()
    # print(lt)
# print(sizel)
# print(sizer)
sizel.reverse()
for i in range(0 , a):
    print(max([sizel[i],sizer[i]]),end=" ")
print()
