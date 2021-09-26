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

`'d'`

</details>


<br /> 

</details>

<details>
  <summary> 3.2. What does spam[-1] evaluate to? </summary>

`'d'`

</details>


<br /> 

</details>

<details>
  <summary> 3.3.What does spam[:2] evaluate to? </summary>

`['a', 'b']`

</details>


4. For the following three questions, let’s say `ham` contains the list
`[3.14, 'cat', 11, 'cat', True]`.

</details>


<br /> 

</details>

<details>
  <summary> 4.1 What does `ham.index('cat')` evaluate to? </summary>

`1`, The `index()` method returns the first index of the specified element in the list. Use optional `start` and `end` parameters in `list.index(element, start, end)` to search from and up to specific index.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 4.2. What does `ham.append(99)` make the list value in `ham` look like? </summary>

`[3.14, 'cat', 11, 'cat', True, 99]`, the `.append()` method adds a single item to the existing list. It doesn't return a new list of items but will modify the original list by adding the item to the end of the list.

</details>

</details>

<br /> 

</details>

<details>
  <summary> 4.3. What does `ham.remove('cat')` make the list value in `ham` look like? </summary>

`[3.14, 11, 'cat', True]`, the `remove()` method takes a single element as an argument and removes it from the list. If the element doesn't exist, it throws `ValueError`.

</details>


---













5. What are the operators for list concatenation and list replication?
6. What is the difference between the append() and insert() list methods?
7. What are two ways to remove values from a list?
8. Name a few ways that list values are similar to string values.
9. What is the difference between lists and tuples?
10. How do you type the tuple value that has just the integer value 42 in it?
11. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
12. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
13. What is the difference between copy.copy() and copy.deepcopy()?












