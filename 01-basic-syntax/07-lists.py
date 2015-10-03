__author__ = 'Rakshak.R.Hegde'

a = [2, 5, 6, 9]
print(a)

print('Accessing particular elements:')
print(a[0], a[2])

print('Length:', len(a))

a.append(10)
print('append', a)

a.remove(5)
print('remove', a)

a.pop()
print('pop', a)

a.pop(0)
print('pop at 0', a)
a.pop(0)
print('pop at 0', a)

# brand new way to initialize lists
a = list(range(10))
print('\nRange List:\n', a)
# yet another way
a = [x * 2 for x in range(10)]
print('Multiplied by 2:\n', a)
