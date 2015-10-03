__author__ = 'Rakshak.R.Hegde'

a = 10
if a == 7:
    print('7 is prime')
elif a < 0:
    print('Negative number')
elif a > 0:
    print('Positive number')
else:  # always comes last
    print('Has to be zero :P')

print('\nOne line if')
a, b = 100, 20
c = a if a < b else b # c=a<b ? a :b
print(c)
