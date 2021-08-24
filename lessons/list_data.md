# The `list` data type in Python #

Getting multiple input strings from user

```py
usr_strings = list()

while True:
    print(f'Enter the name of philosopher {len(usr_strings)} (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    usr_strings = usr_strings + [name]

print('The names are:')
for name in usr_strings:
    print(' ' + name)
```

Multiple assignment from lists
```py
book = ['Neuromancer', 'Gibson, William', 'Science Fiction']
title, author, genre = book[0], book[1], book[2] 
```

### Passing references
Functions pass value references to parameter variables, for mutable objects this means a copy of the reference is used for the parameter (e.g., it will modify the list):

```py
def add_feature(a_book, a_paramter):
    a_book.append(a_parameter)

book = ['Neuromancer', 'Gibson, William', 'Science Fiction']
subgenre(book, 'Cyberpunk')
print(book)
['Neuromancer', 'Gibson, William', 'Science Fiction', 'Cyberpunk']
```
