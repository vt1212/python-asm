#print('Please Enter the String:')
#x=input()
#y='***',x
#print('Capitalised at the First:',y.title())
#print('Capitalise all the WORD',y.upper())
# is a tuple, not a string (A tuple is an ordered, immutable collection of items)
# so y.title() and y.upper() will fail
#corret version
print('Please Enter the String:')
x = input()
y = '***' + x
print('Capitalised at the First:', y.title())
print('Capitalise all the WORD:', y.upper())
#A string is a sequence of characters enclosed in single ('), double ("), or triple quotes (''' """)
#A tuple is an ordered, immutable collection of items. It is similar to a list, but cannot be changed (immutable) after creation.
# use tuple when you need fixed data that won’t change