"""
Create: 

n numbers from the Finonacci sequence starting from F(0)

"""
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

## solution 1: recursion
def recur(i):
    if i == 0 or i == 1:
        return i
    else:
        return recur(i-1) + recur(i-2)

def solution1(n = 5):
    result = list()
    for i in range(n):
        result.append(recur(i))
    
    return result

## solution 2: procedural
def solution2(n = 5):
    result = list()
    result.append(0)
    result.append(1)
    result_size = len(result)
    for _ in range(result_size, n):
        result.append(sum(result[-2:]))
    
    return result

class Solution3():
    def __init__(self):
        self.result = list()
        self.result.append(0)
        self.result.append(1)
    
    def __call__(self, i):
        var = 0
        if (i == 0) or (i == 1):
            return self.result[i]
        
        elif i >= len(self.result):
            var = self.__call__(i-1) + self.__call__(i-2)
            self.result.append(var)
            
        #else:
        #    var = self.result[i-1]+self.result[i-2]
        
        return self.result[i]


def main():
    base = baseline(n=15)
    print(base)
    
    sol1 = solution1(n=15)
    print(sol1)
    
    sol2 = solution2(n=15)
    print(sol2)
    
    sol3 = Solution3()
    result = list()
    for i in range(15): result.append(sol3(i))
    print(result)

    str_list = stringer_join(result)
    print(str_list)

    join_list = stringer_join(result, join="0")
    print(join_list)


if __name__=='__main__':
    main()
