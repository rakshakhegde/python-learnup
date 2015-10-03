__author__ = 'Rakshak.R.Hegde'

print('Input a:')
a = input()
print(type(a), a)


# Typecasting
# b = int(a) + 10
# print('b:', b)


# Input list of numbers
print('\nEnter list of numbers')
a = input()
print('Raw string input:', a)
a = a.split()
print('a is split by spaces:', a)
a = map(int, a)
print('Integerised a:', a)
print('uh oh that was nasty')
a = list(a)
print('Converted to list:', a)
print('Sum of all numbers:', sum(a))


# Shorter way
print('\nEnter list of numbers:')
a = list(map(int, input().split()))  # one liner
print('Integerised a:', a)
print('Sum is:', sum(a))
