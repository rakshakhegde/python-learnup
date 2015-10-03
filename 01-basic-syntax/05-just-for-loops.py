__author__ = 'Rakshak.R.Hegde'

print('for-1')
print(list(range(10)))
for i in range(10):  # [0-10) = [0-9]
    print(i)

print('\nfor-2')

for i in range(3, 10):  # [2-9]
    print(i)

print('\nfor-3')
for i in range(0, 10, 2):  # for(int i=0; i<10; i+=3)
    print(i)

# an addition to loops
print('\nwhile loop')
a = 0
print('a<20:', a < 20)
while a < 20:
    print(a, end=' ')
    a += 1
    if a == 15:
        break
