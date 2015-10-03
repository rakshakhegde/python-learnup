__author__ = 'Rakshak.R.Hegde'

n, l = map(int, input().split())
p = sorted(map(int, input().split()))
mL = 0
for i in range(len(p) - 1):
    mL = max(mL, (p[i + 1] - p[i]) / 2)
mL = max(mL, p[0], l - p[-1])
print(mL)
