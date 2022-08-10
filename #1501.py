n = int(input())
m = list(map(int, input().split()))
maxi = m[0]
flag = True
for i in range(len(m)):
    maxi = max(m[i], maxi)
    if m[i] < maxi:
        print(-1)
        flag = False
        break
if flag:
    print(max(m) - min(m))
