"""
Illustration of computational thinking.
Inspired by 'Lesson 1: Computational Thinking' by Syed Faizan

"""
def solution(n):
    """ for n = 15
    """
    result = ''
    for i in range(1, n + 1, 1):
        if i == n:
            result += 'AB'
        elif i % 3 == 0:
            result += 'A'
        elif i % 5 == 0:
            result += 'B'
        else:
            result += str(i)
    return result

def solution2(n):
    """ for any value of n
    """
    result = str()
    for i in range(1, n + 1, 1):
        if (i % 3 == 0) and (i % 5 == 0):
            result += 'AB'
        elif (i % 3 == 0):
            result += 'A'
        elif (i % 5 == 0):
            result += 'B'
        else:
            result += str(i)
    
    return result

def solution3(n):
    """ for any value of n
    """
    result = str()
    for i in range(1, n + 1):
        flag = False
        if (i % 3 == 0):
            result += 'A'
            flag = True
        if (i % 5 == 0):
            result += 'B'
            flag = True
        if (flag == False):
            result += str(i)
    
    return result

if __name__ == '__main__':
    #problem = '12A4BA78AB11A1314AB'
    #print(f'[INFO] The problem is: {problem}')
    #one_solution = solution(n=15)
    #print(f'[INFO] The solution is: {one_solution}')
    #print(one_solution == problem)
    one_solution = solution(n=30)
    print(one_solution)
    print()
    another_solution = solution2(n=30)
    print(another_solution)
    print()
    yet_another_solution = solution3(n=30)
    print(yet_another_solution)
    print()
    print("".join([str(i) for i in list(range(1,31))]))