# Classes in Python and OOP #

# Object-oriented programming in Python

## Introduction ##

_modes of programming_
  * tactical mode: short-term problem solving
  * strategic mode: long-term product development

_object-based_ vs. _object-oriented_ code
  * pass objects around in scripts, use objects in expressions, called method &c
  * OO: objects participate in _inheritance hierarchy_

_class_
  * object template in Python that supports inheritance
  * main OOP tool in Python
  * packages of functions that process built-in object types
  * entirely optional in Python

_OOP_
  * effective programming, factor to minimize redundancy, new programs are customization of existing code

_Inheritance_
  * mechanism for code customization and reuse

### UML Diagram
* A UML diagram is a diagram based on the UML (Unified Modeling Language) with the purpose of visually representing a system along with its main actors, roles, actions, artifacts or classes, in order to better understand, alter, maintain, or document information about the system.

## Rationale behind classes ##
* whenever you have an application that can be decomposed into a set of objects
* model real-world structure and relationships more accurately
* support better programming that flat procedural programming

_Inheritance_
  * 'kinds-of' relations that allow subordinate objects to inherit properties of superordinate objects
  * specialization
_composition_
  * 'part-of' relations that reflect that any object is a collection of components (an example of composition). A component can be coded as a class that defines its behavior and relationships
  * container

### Distinctive properties ###
 * _Multiple instances_ - object templates, a call of a class creates an object (with a namespace)

 * _Customization via inheritance_ - a class can be extended by redefining attributes in a subclass --> classes can build up namespace hierarchies
    * superclass  links are made by listing classes in parentheses in class statement header
    * class - attributes are created by statements (assignments) in class statements
    * instance - attributes are generated by assignments to self attributes in methods



 * _Operater overloading_ - through protocol methods, classes can create objects that respond to operations that work on built-in types (e.g., slicing, concatenation, indexing &c)
```py
class Super(self):
  def method(self):
    print('in Super.method')

class Sub(super):
  def method(self):             # override method
    print('stating Sub.method') # add action
    Super.method(self)          # run default action
    print('ending Sub.method')
```

### Implementation of OOP ###
  * special first argument in function t0 receive the subject of the call
  * inheritance attribute search to support programming by customization

## OOP ##

Core OOP expression in Python

```py
object.attribute
```
* the expression initiates a search in objects derived from class statements. the expression searches a tree of linked objects, looking for the first appearance of `attribute`: "Find the first occurrence of `attribute` by looking in object, then in all classes above it, from bottom to top and left to right."
* i.e., attribute fetches are tree searches

_class objects_
  * attributes provide behavior (data and functions) inherited by all instances
_instance objects_
  * attributes record data that varies pr. specific object

<attribute inheritance search figure around here>


```py
class C2: ...           # make class objects
class C3: ...
class C1(C2, C3): ...   # link to superclasses (in this order), multiple inheritance/several supers

I1 = C1()               # make instances
I2 = C1()               # linked to their classes
```

* attributes are usually attached to classes by assignments made at the top level in class statement blocks, and not nested inside function `def` statements there
* attributes are usually attached to instances by assignments to the special argument passed to functions coded inside classes, called `self`

```py
class C2: ...             # make class objects
class C3: ...

class C1(C2, C3):         # link to superclasses (in this order), multiple inheritance/several supers
  def setname(self, who): # Assign name: C1.setname
    self.name = who       # Self is either I1 or I2

I1 = C1()                 # make instances
I2 = C1()                 # linked to their classes

I1.setname('kaj')         # set I1.name to 'kaj'
I2.setname('andrea')      # set I2.name to 'andrea'
print(I1.name)            # prints 'kaj'
```
* `def` inside a class is a _method_ that automatically receives the first special argument (`self`) that provides a handle bask to the instance
* any value passed to the method, will go to arguments after self (who in this case)

* `__init__` constructor, called each time an instance is generated, new instance is passed to `self` argument of `_init__`. effect is to initialize instance without requiring a method call

```py
class C2: ...               # make class objects
class C3: ...

class C1(C2, C3):           # link to superclasses (in this order), multiple inheritance/several supers
  def __init__(self, who):  # set name when constructed
    self.name = who         # Self is either I1 or I2

I1 = C1()                   # make instances
I2 = C1()                   # linked to their classes

I1.C1('kaj')                # set I1.name to 'kaj'
I2.C1('andrea')             # set I2.name to 'andrea'
print(I1.name)              # prints 'kaj'
```

# An Example: Personal Database

## Step 1: Making Instances

```py
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

```
* pass data to instance as arguments to constructor method and assign to self
* `self` is instance object and data (`name`, `job`, `pay`) are state information
* `self.job` has global scope (assigned to instance), while `job` only local to constructor function

Test class
```py
kaj = Person('Kaj N??rgaard', job='Jazz Musician')
andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)

print(kaj.name, kaj.pay)
print(andrea.name, andrea.pay)
print(f'[RESULT] {anrea.job} pays better than {kaj.job}')
```
* each record is independent information --> kaj and andrea are both _namespace objects_ (i.e., independent copy og class state information)

```py
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

if __name__=='__main__':                        # when run for tessting only
  # self-test code
  kaj = Person('Kaj N??rgaard', job='Jazz Musician')
  andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)
  print(kaj.name, kaj.pay)
  print(andrea.name, andrea.pay)
```
* `__name__` module is designed to only run for testing, to avoid that the tests also runs when the class is imported
* run a file _directly_ (execute main) or _indirectly_ (from person import Person)
* _hard coding operations_ like surname and praise outside a class is a maintenance nightmare

## Step 2: Adding Behavior Methods

Use the instances

```py
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

if __name__=="__main__":                        # when run for tessting only
  # self-test code
  kaj = Person('Kaj N??rgaard', job='Jazz Musician')
  andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)
  print(kaj.name, kaj.pay)
  print(andrea.name, andrea.pay)
  print(kaj.name.split()[-1])
  andrea.pay *= 1.1
  print('{0:.2f}'.format(andrea.pay))
```
* _hard coding operations_ like surname and praise outside a class is a maintenance nightmare
* code/add methods for all behavior

```py
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

  def surname(self):                            # Behavior methods
    return self.name.split()[-1]              # self is implied subject

  @rangetest(percent=(0.0, 1.0))                # decorator to validate and avoid astronomic pay raise
  def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent))    # must change here only

if __name__=="__main__":                        # when run for tessting only
  # self-test code
  kaj = Person('Kaj N??rgaard', job='Jazz Musician')
  andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)
  print(kaj.name, kaj.pay)
  print(andrea.name, andrea.pay)
  print(kaj.surname(), andrea.surname())
  andrea.giveRaise(.10)
  print(andrea.pay)
```

## Step 3: Operator Overloading

Employ _operator overloading_ to provide a print display of the class instances that is more useful that the default

Default behavior
```py
>>> print(andrea)
<__main__.Person object at 0x00000000029A0668>
```
* `__repr__` and `__str__` operator overloading methods, both methods are run automatically every time an instance is converted to its print string
* `__str__` is preferred by `print()` and `str()`, and `__repr__` is the fallback for these roles

```py
# add __repr__ overloading method for printing objects
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

  def surname(self):                            # Behavior methods
    return self.name.split()[-1]              # self is implied subject

  @rangetest(percent=(0.0, 1.0))                # decorator to validate and avoid astronomic pay raise
  def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent))    # must change here only

  def __repr__(self):                           # add operator overloading method
    return f'[Person: {self.name}, {self.pay}]' # string to print

if __name__=="__main__":                        # when run for tessting only
  # self-test code
  kaj = Person('Kaj N??rgaard', job='Jazz Musician')
  andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)
  print(kaj)
  print(andrea)
  print(kaj.surname(), andrea.surname())
  andrea.giveRaise(.10)
  print(andrea)
```

* Result
  * the class packages data and logic into single, self-contained software-component
  * the software component is easy to locate and change in the future
  * allows us to encapsulate behavior in order to avoid redundancy (and associated cost from maintenance)

## Step 4: Customizing Behavior by Subclassing

* customize class by expanding software hierarchy
* create subclass that inherits methods

* Task, all managers get an additional bonus of 10% when they get a raise
Bad approach: copy-paste
```py
class Manager(Person):
  def giveRaise(self, percent, bonus=.10):
    self.pay = int(self.pay * (1 + percent + bonus))
```
* works, BUT copy-paste increase maintenance cost, e.g., if we change the Person procedure for giving a raise, we also have to change the procedure for Manager

Good approach: augmentation of original `giveRaise()`
```py
class Manager(Person):
  def giveRaise(self, percent, bonus=.10):
    Person.giveRaise(self, percent + bonus)
```
* uses that class methods are called through _instance_ OR _class_, that is, `instance.method(args...)` is equivalent to `class.method(instance, args)`

```py
# add customization of one behavior in a subclass
class Person:
  def __init__(self, name, job=None, pay=0):    # constructor method with three arguments (normal function args)
    self.name = name                            # fill out fields when created
    self.job = job                              # self is the new instance object
    self.pay = pay

  def surname(self):                            # Behavior methods
    return self.name.split()[-1]                # self is implied subject

  @rangetest(percent=(0.0, 1.0))                # decorator to validate and avoid astronomic pay raise
  def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent))    # must change here only

  def __repr__(self):                           # add operator overloading method
    return f'[Person: {self.name}, {self.pay}]' # string to print

class Manager(Person):
  def giveRaise(self, percent, bonus=.10):      # Redefine at this level
    Person.giveRaise(self, percent + bonus)     # Call Person's version

if __name__=="__main__":                        # when run for tessting only
  # self-test code
  kaj = Person('Kaj N??rgaard', job='Jazz Musician')
  andrea = Person('Andrea Willumsen', job='Entertainer', pay=1000000)
  print(kaj)
  print(andrea)
  print(kaj.surname(), andrea.surname())
  andrea.giveRaise(.10)
  print(andrea)

  povl = Manager('Povl Kj??ller', 'Narrator', pay=1000000)
  povl.giveRaise(.10)
  print(povl.surname()
  print(povl)
```
