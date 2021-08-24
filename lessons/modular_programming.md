# Modular programming in python, introduction to

`def` statement

```py
def hello():
    print('Hello my name is Donald Knuth')
    print('I am 83 years old')

hello()
```

`def` statments with parameters

```py
def hello(name, age=False):
    print(f'Hello my name is {name}')
    if age:
        print(f'I am {age} years old')

hello('Donald')
hello('Donald Knuth')
hello('Donald Ervin Knuth', age=83)
```

`return` statements`

```py
def age_getter(name, birthyear):
    now = datetime.datetime.now()
    age = now.year - birthyear
    return (age, name)

(age, name) = age_getter('Donald Ervin Knuth', 1938)
print(f'Hi {name}, you are {age} years old')
```

Call stack, functions are not executed linearly in Python' call stack

```py
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
```
