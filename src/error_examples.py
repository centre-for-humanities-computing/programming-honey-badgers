"""
Examples of error handling in Python

"""

def vanilla_division(demoninator, numerator = 23):
    return numerator / demoninator

def division(demoninator, numerator = 23):
    try:
        return numerator / demoninator
    except ZeroDivisionError:
        print('[ERROR] divide by zero no permitted')

if __name__=='__main__':
    #print('[INFO] without error handling')
    #print(vanilla_division(2))
    #print(vanilla_division(3))
    #print(vanilla_division(0))
    #print(vanilla_division(5))

    print('\n[INFO] with try-except statements')
    print(division(2))
    print(division(3))
    print(division(0))
    print(division(5))

    

