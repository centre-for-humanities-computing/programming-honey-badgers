# Flow of Control with Python #

---
**Control flow**

The order in which the individual python statements, expressions and function call are evaluated. Explicit control flow is a feature of imperative progamming languages, like Python, in contrast to declarative programming languages (e.g., SQL). A control statement in Python enable the program to _make a decision_ and follow one execution path instead of another. Control flow ensures that your Python program can follow multiple paths (bifurcate, repeat, bypass), instead of just a linear execution.
---

## Branching with Boolean Values ##

* Boolean errors

```py
>>> spock = True
>>> spock
True
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>>
>>> True = 2+2
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
```

| Operator | Meaning |
| - | - |
| `==` | equal to|
| `!=` | not equal to|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

* Boolean integer tests

```py
>>> 23 == 23
True
>>> 23 == 5
False
>>> 2 != 3
True
>>> 5 != 5
False
```

* String and float tests

```py
>>> 'spock' == 'spock'
True
>>> 'spock' == 'Spock'
False
>>> 'spock' != 'kirk'
True
>>> False == False
True
>>> 23.0 == 23
True
>>> 23 == '23'
```

* leg/geq

```py
>>> 5 < 23
True
>>> 5 > 23
False
>>> 23 < 23
False
>>> spock = 25
>>> spock <= 25
True
>>> kirk = 24
>>> kirk >= 10
True
```

variable assignment vs. equality test
    - `==` operator compares two values
    - `=` operator assigns a value to a variable

### Boolean operators ###

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


