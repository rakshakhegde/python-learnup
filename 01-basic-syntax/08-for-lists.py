__author__ = 'Rakshak.R.Hegde'

a = ['atria', 'vtu', 'belgaum', 'karnataka']
for i in a:
    print(i)

# Strings Mangling
print('\n\nStrings of max length = 5')
for i in a:
    if len(i) > 5:
        print(i[:5])
    else:
        print(i)
