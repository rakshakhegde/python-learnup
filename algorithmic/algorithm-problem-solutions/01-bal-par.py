__author__ = 'Rakshak.R.Hegde'

s = input()  # (()()())
# find if balanced
sum = 0
for ch in s:
    if ch == '(':
        sum += 1
    else:
        sum -= 1
    if sum < 0:
        break
# print('Balanced' if sum == 0 else 'Not')
# find immediate pairs
cntr = 0
for i in range(len(s) - 1):
    if s[i] == '(' and s[i+1] == ')':
        cntr += 1
print(cntr if sum == 0 else -1)
