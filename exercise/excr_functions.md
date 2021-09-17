# Exercises for Functions Lesson #

## Pair programming ##

## Check your understanding ##


__Combining Strings__

'Adding' two strings produces their concatenation: `a + b` is `ab`. Write a function called `fence()` that takes two parameters called `original` and `wrapper` and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

```py
>>> print(fence('name', '*'))
```

and the output should be

```py
*name*
```

Answer:
```py
def fence(original, wrapper):
    return wrapper + original + wrapper
```

__Return versus print__

Note that `return` and `print()` are not interchangeable. `print()` is a function that prints data to the screen. It enables us, users, see the data. The `return` statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:

```py
def add(a, b):
    print(a + b)
```

What will we see if we execute the following commands?

```py
A = add(7, 3)
print(A)
```

Answer:

Python will first execute the function `add()` with `a = 7` and `b = 3`, and, therefore, print 10. However, because function `add()` does not have a line that starts with `return` (no return 'statement'), it will, by default, return nothing which is called `None`. Therefore, A will be assigned to `None` and the last line (`print(A)`) will print `None`. As a result, we will see:

```py
10
None
```

__Selecting Characters From Strings__

If the variable `s` refers to a string, then `s[0]` is the string’s first character and `s[-1]` is its last. Write a function called `outer()` that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

```py
>>> print(outer('helium'))
```

and output 

```py
hm
```

Answer:

```py
def outer(input_string):
    return input_string[0] + input_string[-1]
```



## Practice questions ##

In your answers to practice questions, try to use code to illustrate your answer.


1: Why are the advantageous of functions, and more generally, modular programming?

2: When does the code in a function execute: during function definition or function call?

3: What statement creates a function?

4: What is the difference between a function and a function call?

5: How many scopes are there in Python?

6: What happens to a variable in local scope, when the function call returns?

7: What is a return value? Can a return value be part of an expression?

8: If a function lacks a return statement, what is the return value of the function call?

9: What keyword allow you to update a global variable in a function?

10: What does `None` mean?

11: What does the `import numpy` statement do?

12: If you have a function named `randint()` and a module named `random`, how would you import and call `randint`?

13: How do you prevent a program from crashing, when it gets an error?

14: What constitutes the `try` clause? What constitutes the `except` clause?