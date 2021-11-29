# Classes in Python #

First introduction to classes in Python

Learning goals:

* How to create classes and instantiate objects in Python
* How to add attributes and behaviors to Python objects
* How to organize classes into packages and modules


## Creating a class ##

Use the `class` keyword to define a class and end with `:`. Notice the naming rule, we reserve CamelCase for class defintion accoring to PEP 8.

Create `some_class.py` and define your first class without any data or behavior.

```py
class SomeClass:
    pass
```

Open the terminal and instantiate the class in interactive mode

```sh
$ python -i some_class.py
>>> o = SomeClass
>>> print(o)
<class '__main__.SomeClass'>
```

Similar to a function call, but Python 'knows' that we are calling a class, not a function.

### Adding attributes ###

With python objects, we can add attributes interactively using dot notation `<object>.<attribute> = <value>`.

```sh
>>> class Point:
...     pass
...
>>> p1 = Point()
>>> p2 = Point()
>>> p1.x = 5
>>> p1.y = 4
>>> p2.x = 3
>>> p2.y = 6
>>> print(p1.x, p1.y)
5 4
>>> print(p2.x, p2.y)
3 6
>>> dir(p1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']
```

Apart from the dunder methods `__<method>__`, we can see that our class now has a x and y attribute.

### Adding behavior to a class ###

Now it is time to start constructing a class with behavior. Create a `point.py` script.

```py
class Point():
    def reset(self):
        self.x = 0
        self.y = 0
```

And the run the script interactively

```sh
$ python -i point.py
>>> p = Point()
>>> p.reset()
>>> print(p.x, p.y)
0 0
```

A method is formatted like a function, but 'called' by using dot notation, the `self` parameter however is necessary for class methods.

### The `self` parameter ###

`self` represents a required argument for methods which reference the object of the method that can be used to access attributes and methods of the object. Without `self`, you will get a TypeError that indicates a missing argument.

### Adding more arguments ###

Extend the `Point` class in `point.py` with additional behavior.

```py
import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        dist = math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )
        return dist
```

And then run an experiment with two points

```sh
$ python -i point.py
>>> p1 = Point()
>>> p2 = Point()
>>> p1.reset()
>>> p2.move(5,0)
>>> print(p2.calculate_distance(p1))
5.0
>>> p1.move(3,4)
>>> print(p1.calculate_distance(p2))
4.47213595499958
>>> print(p1.calculate_distance(p1))
0.0
```

### Initializing an object ###

We still need to set the default attributes (data) of the class (currently we need to use the move or reset methods). In Python we use an _initializer_ to initialize an object when created. The initialization method is like any other method, except it has a special name `__init__`.

```py
class Point:
    def __init__(self, x, y):
        self.move(x, y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)
```

Now we can construct a point

```sh
$ python -i point.py
>>> p = Point(3, 5)
>>> print(p.x, p.y)
3 5
```

Now we cannot initialize a point without providing the x and y arguments (or we get at TypeError).

Using default values, as in functions, we can add

```py
class Point:
    def __init__(self, x = 0, y = 0):
        self.move(x, y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)
```

We normally put the initialization stateents in the `__init__` function

### Adding a docstring ###

As always it is important to add documentation for our code (and use self-documenting practices when naming classes).

```py
import math

class Point:
    """ Represents point in 2-d geom coordinates
    """
    def __init__(self, x = 0, y = 0):
        """ Initialize position of a point
        x, y: int, defalt 0, 0
        """
        self.move(x, y)
    
    def move(self, x, y):
        """ Move point to new location in 2d
        """
        self.x = x
        self.y = y
    
    def reset(self):
        """ Reset point to geom origin
        """
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        """ Calculate Euclidian dist between two
        points
        other_point: int, second point passed as parameter
        """
        dist = math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )
        return dist
```

And then re-run our experiment from before

```sh
$ python -i point.py
>>> p1 = Point()
>>> p2 = Point(5,0)
>>> print(p2.calculate_distance(p1))
5.0
>>> p1.move(3,4)
>>> print(p1.calculate_distance(p2))
4.47213595499958
>>> print(p1.calculate_distance(p1))
0.0
```

## Case study ##

Build simple notebook app.

_Notes_

* note is a short memo
* records day of production
* tags for easy querying
* update notes with new knowledge
* search note


```


```