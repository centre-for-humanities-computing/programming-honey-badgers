# Lists and Dictionaries #

Both lists and dictionaries are used to store collections of data

## Lists ##

To write proper programs, we need data types that can contain multiple values and therefore handle large complex data. The `list` data types can store multiple items in a single vairable and is used to store collections of data.

### List data type ###

* a `list` is a value (a list value) that contains multiple values in an _ordered sequence_

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> date_of_birth = [2233, 2305, 2336]
>>> what_a_mess = ['Q', 11235, False, 3.14]
>>> what_a_mess
['Q', 11235, False, 3.14]
```

#### Indexing lists ####

The list data type is a sequence that allow you to index the individual elements (starting from `0`).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[0]
'Kirk'
>>> captains[1]
'Picard'
>>> captains[2]
'Janeway'
>>> print(f'{captains[2]} is my favorite captain')
'Janeway is my favorite captain'
>>> print(f'{captains[0]} is older than {captains[1]} and captains[2]')
```

An index should not exceed the number of values in yhe list (as list index `len(listname) - 1`) and it can _only_ be an integer (type `int`).

```py
>>> captains[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> captains[2.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float

>>> captains['2']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
```

#### Nested lists ####

Lists can contain nested (other) list values (i.e., a list of lists), which is a convenient data type for managing hierarchical data.

```py
>>> fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
>>> print(fridge[0])
['pepper', 'zucchini', 'onion']
>>> print(fridge[0][0])
'pepper'
```

#### Negative indices ####

Lists allow you to index from the end (instead of the beginning).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[-1]
'Janeway'
```

Negative indexing is actually a shorthand for 

```py
>>> captains[len(captains)-1]
'Janeway'
>>> captains[len(captains)-2]
'Picard'
```

#### Slicing lists ####

Indices can be used to index individual elements (values) and slices (sequences of elements).

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[0:4]
['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[1:3]
['Picard', 'Sisko']
>>> xy_only = captains[0:-1]
>>> xy_only
['Kirk', 'Picard', 'Sisko']
>>> captains[:-1]
['Kirk', 'Picard', 'Sisko']
```

#### Chaging values in a list ####

You can assign a value of a list location with an index

``` py
>>> captains = ['Kirk', 'Picard', 'Sisko']
>>> captains[2] = 'Janeway'
>>> captains
['Kirk', 'Picard', 'Janeway']
```

#### List concatenation and replication ####

Like strings (`str`) that is also sequence data, you can use `+` to concatenate lists and `*` for replicate lists.

```py
>>> ['Kirk', 'Picard', 'Janeway'] + [2233, 2305, 2336]
['Kirk', 'Picard', 'Janeway', 2233, 2305, 2336]
>>> [2233, 2305, 2336] * 2
[2233, 2305, 2336, 2233, 2305, 2336]
```

If you are left wondering 'how then do i do element-wise multiplication?' after the last example of replication, then look up `numpy` or use a list comprehension

```py
>>> [item * 2 for item in [2233, 2305, 2336]]
[4466, 4610, 4672]
```

#### Removing elements from a list ####

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> del captains[2]
>>> captains
['Kirk', 'Picard', 'Janeway']
```

### Working with lists ###

List allow you to `append()` new elements (just as concatenating from the end)

```py
users = list()
while True:
    print(f'Please enter the name of user {len(users) + 1} or enter nothing to end.')
    name = input()
    if name == '':
        break
    users.append(name)
print('The users are:')
for name in users:
    print(f'   {name}')
```

#### Iterate over lists ####

Because lists are sequence data, you can iterate through evey element in the list with a `for` or `while` statement.

```py
captains = ['Kirk', 'Picard', 'Janeway']
for captain in captains:
    print(captain)
```

```py
i = 0
while i < len(captains):
    print(captains[i])
    i = i + 1
```