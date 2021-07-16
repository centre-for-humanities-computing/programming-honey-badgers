

# Boolean operators




## Truth tables for Boolean operators

Boolean operators (NOT/AND/OR) compare Boolean values/expressions (True/False).

Negation, NOT/$\lnot$

| Expression | $\lnot$`True` | $\lnot$`False` |
| - | :-: | :-: |
| Evaluates to...  | __F__ | __T__ |

```py
>>> A = True
>>> not A
False
>>> B = False
>>> not B
True
>>> not not B
False
```

Conjunction, AND/$\land$

| Expression | `True` $\land$ `True` | `True` $\land$ `False` | `False` $\land$ `True` | `False` $\land$ `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __F__ | __F__ | __F__ |

```py
>>> A = True
>>> A and A
True
>>> B = False
>>> A and B
False
>>> B and A
False
>>> B and B
False
```

Disjunction, OR/$\lor$

| Expression | `True` $\lor$ `True` | `True` $\lor$ `False` | `False` $\lor$ `True` | `False` $\lor$ `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __T__ | __T__ | __F__ |

```py
>>> A = True
>>> A or A
True
>>> B = False
>>> A or B
True
>>> B or A
True
>>> B or B
False
```

### Examples

What is the largest number

```py
x = 1
y = 3
z = 2
if (x > y) and (x > z):
    print("x is larger than y and z")
elif (y > x) and (y > z):
    print("y is larger than x and z")
else:
    print("z is larger than x and y")
```

Neural representations of Boolean operators