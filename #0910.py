s = input()
open = 0
sum = 0
for i in range(len(s)-4):
    if s[i:(i+5)] == 'heavy':
        open += 1
    if s[i:(i+5)] == 'metal':
        sum += open
print(sum)
