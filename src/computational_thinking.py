"""
Illustration of computational thinking.
Inspired by 'Lesson 1: Computational Thinking' by Syed Faizan

"""
def solution(n):
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


if __name__ == '__main__':
    problem = '12A4BA78AB11A1314AB'
    print(f'[INFO] The problem is: {problem}')
    one_solution = solution(n=15)
    print(f'[INFO] The solution is: {one_solution}')
    print(one_solution == problem)