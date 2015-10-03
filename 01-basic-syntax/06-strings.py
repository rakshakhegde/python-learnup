__author__ = 'Rakshak.R.Hegde'

a = 'futurelane'
print(a)
print('Length:', len(a))
print('Get character:', a[0], a[2], a[6], a[9])  # try beyond range (>=10)

#Slicing
print('\nSlicing:', a[:7], a[7:], a[2:7], a[2:7:2])

print('Handy methods')
print('\nIndex of rel:', a.index('rel'))
print('Count "e":', a.count('e'))
print(a.startswith('future'))
print(a.endswith('bane'))
print(a.upper(), a.upper().lower())


# Miscellaneous
print('\nString Formatting:')
# a = '{} was eating {} apples'
a = '{name} was eating {count} apples and {count} oranges'
print('Template:', a)
# a = a.format('John', 'three')
a = a.format(count='6', name='John') # order changed
print('Tada:', a)
