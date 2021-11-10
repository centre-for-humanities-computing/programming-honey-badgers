from rich import print, pretty
from rich import inspect
from rich.console import Console
import pandas as pd


def print_output():
    print('A dictionary of lists:', {'num_list1': [1, 2, 3], 'num_list2': [3, 4, 5]})
    print(f'A tuple of integers {(1, 2, 3, 4)}')
    print(f'Booleans {False} and {True}')


def inspector(object):
    inspect(object, methods=True)


def edit_data(data):
    console = Console()
    var_1 = 45
    var_2 = 30
    var_3 = var_1 + var_2
    data['a'] = [var_1, var_2, var_3]
    console.log(data, log_locals=True)


if __name__ == '__main__':
    #print_output()
    #from sklearn import datasets
    #inspector(datasets)
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    edit_data(data)
