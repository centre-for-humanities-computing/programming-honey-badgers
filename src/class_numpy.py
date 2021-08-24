"""
Introduction to classes in Python with Numpy
"""
import numpy as np
from os import system, name# some OS helpers

def clear():
    """ clear terminal"""
    # TODO: transfer to utils.py
    # windows
    if name == 'nt':
        _ = system('cls')
    # nix
    else:
        _ = system('clear')

def transpose(M):
    return M.T

def addone(M):
    return M + 1

def tradone(M):
    return transpose(addone(M))


class MatrixObject:
    def __init__(self, list_input):
        self.matrix = np.array(list_input)
    
    def getDims(self):
        self.dims = (len(self.matrix[:,0]),len(self.matrix[0,:])) 
    
    def getTranspose(self):
        self.transpose = np.array([self.matrix[:, i] for i in range(len(self.matrix[0,:]))])

    def addInt(self, integer = 1):
        self.intergerUpdate = self.matrix + integer

def main():
    X = np.zeros((2,5))
    print(f'[INFO] original matrix: \n{X}\n')
    print(f'[INFO] transposed matrix: \n{transpose(X)}')
    print(f'[INFO] elementwise addition: \n{addone(X)}')
    print(f'[INFO] trainspose elementwise addition: \n{tradone(X)}')

    input("[INFO] Ready to continue...")
    clear()

    lsofls = [[1, 1, 2], [3, 5, 8]]
    print(lsofls)
    X = MatrixObject(lsofls)
    print(X.matrix)
    X.getDims()
    print(X.dims)
    X.getTranspose()
    print(X.transpose)
    X.addInt(integer=5)
    print(X.intergerUpdate)

if __name__=="__main__":
    main()