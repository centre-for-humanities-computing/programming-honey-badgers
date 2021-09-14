# Programming for the Humanities: Assignment 1 #

Assigment 1 tests your understanding of basic python syntax, components of flow control and procedural programming with functions. 

---

* 
* please explain the code execution line by line in your implementation


## 1. Pattern generation ##

__Task__: write a script that uses flow control statements to generate the following pattern. Ensure that your script can continue the pattern

```sh
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
```

See `assign1_0.py`for a possible solution

```py
j = 0
while j < 2:
    i = 10
    for i in range(1, i, 1):
        print('*'*i)
    for i in range(i-1, 0, -1):
        print('*'*i)
    j += 1
```

## 2. Authorization test ##

__Task__: write a script that uses at least one function to accept user input of `name` and `password`, prints a polite welcome to the user, and tests if the password is correct (you decide the correct password).

See `assign1_1.py` for possible solutions

```py
def authorization(name, password):
    print(f'Welcome {name}')
    if password == 'correct-password':
        print('You shall pass...')
    else:
        print('You shall not pass...')

def main():
    print('[INFO] Please input your name:')
    usr = input()
    print('[INFO] Please input your password')
    pwd =  input()
    authorization(usr, pwd)

if __name__=='__main__':
    main()
```

## 3. Sequence generation ##

__Task__: Write a script that uses at least one function that takes `15` as input and generates this sequence '0010102030508013021034055089014402330377'.

See `assign1_2.py` for possible solutions

```py
def stringer_join(l, join=False):
    result = [str(val) for val in l]
    if join:
        result = f'{join}'.join(result)
    
    return result

def baseline(n = 5):
    result = list()

    for i in range(n):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(i)
        else:
            result.append(result[i-2] + result[i-1])
    
    return result

if __name__=='__main__':
    res = baseline(n=15)
    print(stringer_join(res, join='0'))
```
