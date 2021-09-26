# Exercises for Functions Lesson #

## Pair programming ##

Take the following nested list 

```py
>>> fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
```

and create a function that returns a _flat list_:

```py
['pepper', 'zucchini', 'onion', 'cabbage', 'lettuce', 'garlic', 'apple', 'pear', 'banana']
```

Answer:

```py
def flatten(lst):
    """
    Flatten list

    Input:
        - lst, a nested list (one level of nesting only)
    """
    flat_list = list()
    for sublst in lst:
        for item in sublst:
            flat_list.append(item)
    
    return flat_list

# OR with a list comprehension

def flatten(lst):
    return [item for sublst in lst for item in sublst]


fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]

flat_fridge = flatten(fridge)
print(flat_fridge)
```

## Check your understanding ##

---

## Practice questions ##


<br /> 

</details>

<details>
  <summary> What is `[]`?</summary>

1. An empty `list`. In Python square brackets are used to open and close a list object.

</details>


<br /> 

</details>

<details>
  <summary> 2. How would you assign the value 'hello' as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)</summary>

`spam[2] = 'hello'` 

</details>


3. For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`.

<br /> 

</details>

<details>
  <summary> 3.1. What does `spam[int(int('3' * 2)` // 11)] evaluate to?</summary>

'd'

</details>

<br /> 

</details>

<details>
  <summary> 3.2. What does spam[-1] evaluate to? </summary>

'd'

</details>

<br /> 

</details>

<details>
  <summary> 3.3.What does spam[:2] evaluate to? </summary>

['a', 'b']

</details>






---
















3. For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`.
    * What does spam[int(int('3' * 2) // 11)] evaluate to?
    * What does spam[-1] evaluate to?
    * What does spam[:2] evaluate to?
4. For the following three questions, let’s say `ham` contains the list
`[3.14, 'cat', 11, 'cat', True]`.
    * What does `bacon.index('cat')` evaluate to?
    * What does `bacon.append(99)` make the list value in bacon look like?
    * What does bacon.remove('cat') make the list value in bacon look like?
5. What are the operators for list concatenation and list replication?
6. What is the difference between the append() and insert() list methods?
7. What are two ways to remove values from a list?
8. Name a few ways that list values are similar to string values.
9. What is the difference between lists and tuples?
10. How do you type the tuple value that has just the integer value 42 in it?
11. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
12. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
13. What is the difference between copy.copy() and copy.deepcopy()?












