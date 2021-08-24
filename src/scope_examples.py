"""
Examples of scope in Python

global keyword: https://www.programiz.com/python-programming/global-keyword

"""

# global scope
s =  'iama a global var'

def print_global_local():
    print(f'var inside function: {s}')

def modify_global_err():
    """ erroneous use of global variable
    """
    s = s + ' , what are you?'
    print(f'var inside function: {s}')

def modify_global():
    """ use of global keyword to modify global in local
    """
    global s
    s = s + ', what are you?'
    print(f'var inside function: {s}')

def print_local_err():
    """ declare local variable
    """
    ss = 'iama a local var'

def print_local():
    """ declare local variable and print
    """
    ss = 'iama a local var'
    print(f'var indside function: {ss}')

def print_nameoverlap():
    nameoverlap = 'i am local'
    print(nameoverlap)

if __name__=="__main__":
    print('_'*50)
    print()
    print('[INFO] an example in variable scope for Python\n'.upper())

    print('[INFO] global scope:')
    print_global_local()
    print(f'var outside function: {s}')

    print('\n[INFO] local modification changes scope:')
    #modify_global_err()
    # comment: need to declare s as global in function
    print(f'var before local update: {s}') 
    modify_global()
    print(f'var after local update: {s}')

    print('\n[INFO] local scope:')
    #print_local_err()
    #print(ss)
    print_local()

    print('\n[INFO] local and glocal vars with name overlap')
    nameoverlap = 'i am global'
    print_nameoverlap()
    print(nameoverlap)
    print('_'*50)


