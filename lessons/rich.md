
Rich can highlight your terminal output based on variable data type

```py
from rich import print, pretty

print({'num_list1': [1, 2, 3], 'num_list2': [3, 4, 5]})
print((1, 2, 3, 4))
print(False, True)
```

Rick can also beatify docstring reports by replacing `help()` with `inspect()`

```py
from rich import inspect
from sklearn import datasets 

inspect(datasets, methods=True)
```

`Console()` provides a range of utility functionality for Rich

```py
from rich.console import Console
import pandas as pd

console = Console()

data = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
def edit_data(data):
    var_1 = 45
    var_2 = 30
    var_3 = var_1 + var_2
    data['a'] = [var_1,var_2,var_3]
    console.log(data, log_locals=True)

edit_data(data)
```