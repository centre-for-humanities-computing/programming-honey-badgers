import datetime
import random
import traceback

def age_getter(name, birthyear):
    """ Return name and age (in years)

    Positional arguments:
    name -- str, name of subject
    birthyear -- int, year of birth
    """
    now = datetime.datetime.now()
    age = now.year - birthyear
    return (age, name)

def fortune_getter(answernumber):
    """Return your magic eight-ball answer, adapted from (Sweigart 2019)

    Positional arguments:
    answernumber -- int, in range 1 to 9
    """
    if answernumber == 1:
        return 'it is certain'
    elif answernumber == 2:
        return 'it is decidedly so'
    elif answernumber == 3:
        return 'yes'
    elif answernumber == 4:
        return 'reply hazy try again'
    elif answernumber == 5:
        return 'ask again later'
    elif answernumber == 6:
        return 'concentrate and ask again'
    elif answernumber == 7:
        return 'my reply is no'
    elif answernumber == 8:
        return 'outlook not so good'
    elif answernumber == 9:
        return 'very doubtful'

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

def f():
    print('f() starts')
    g()
    print('f() returns')

def g():
    """ Display call stack from frame object
    """
    for line in traceback.format_stack():
        print(line.strip())


def main():
    # get your age
    #(age, name) = age_getter('Donald Ervin Knuth', 1938)
    #print(f'Hi {name}, you are {age} years old')
    # get your random fortune
    #r = random.randint(1, 9)
    #fortune = fortune_getter(r)
    #print(f'and your fortune is {fortune}')

    # call stack
    #a()
    # display call stack
    f()
    
if __name__=="__main__":
    main()