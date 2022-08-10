n = int(input())
s = input()
flag = 0
mas1 = [0]*n
mas2 = [0]*n
check = 0
for i in range(2*n):
    if i < n:
        mas1[i] += int(s[i])
    else:
        mas2[i-n] += int(s[i])
mas1.sort()
mas2.sort()

if mas1[0] > mas2[0]:
    flag = 1
elif mas1[0] < mas2[0]:
    flag = 0
else:
    check = 1
    
for i in range(1,n):
    if flag == 1:
        if mas1[i] <= mas2[i]:
            check = 1
            break
    if flag == 0:
        if mas1[i] >= mas2[i]:
            check = 1
            break

if check == 0:
    print('YES')
else:
    print('NO')



