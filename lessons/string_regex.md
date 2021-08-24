# String search with Regex #
* search for patterns/strings with unknowns
‪‬  
## Finding patterns without regex

```py
def dk_phone(text):
    """ find dk phone number without regex
    example: 00 00 00 00
    """
    if len(text) != 11:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[2] != ' ':
        return False
    for i in range(3,5):
        if not text[i].isdecimal():
            return False
    if text[5] != ' ':
        return False
    for i in range(6,8):
        if not text[i].isdecimal():
            return False
    if text[8] != ' ':
        return False
    for i in range(9,11):
        if not text[i].isdecimal():
            return False
    return True
```

```py
if __name__ == '__main__':
  msg = 'Please return the call at 33 92 33 00, otherwise you will be fined 5,000 DKK'
  for i in range(len(msg)):
    chunk = msg[i:(i + 11)]
    if dk_phone(chunk):
      print(f'[INFO] Found a phone number {chunk}, please take appropriate action')
```

## Finding patterns with regex
* regex: descriptions for patterns of text

### Procedure
1. import regex module
2. create regex object with `compile()` and raw string `r''`
3. pass string-to-be-searched to `search()`
4. call `Match` object's `group()` to return matched substring

* Online resource: regex tester [pythex](https://pythex.org/)

## Additional pattern matching
### Grouping

### Special characters

| Special Chars | To Match |
| :-: | :-: |
| . | \\. |
| ^ | \\^ |
| $ | \\$ |
| * | \\* |
| + | \\+ |
| ? | \\? |
| { | \\} |
| } | \\{ |
| [ | \\[ |
| ] | \\] |
| \ | \\\ |
| \| | \\\| |
| (| \\( |
| ) | \\) |

### Matching multiple groups with the Pipe

* `|` pipe functions as XOR

```py
>>> captain_pattern = re.complie(r'Kirk|Picard')
>> mo1 = captain_pattern.search('Kirk and Picard')
>>> mo1.group()
'Kirk'
>>> mo2 = captain_pattern.search('Picard and Kirk')
>>> mo2.group()
'Picard'
```

```py
>>> star_pattern = re.compile(r'Star (Trek|Wars|in the sky)')
>>> mo = star_pattern.search('Star Trek is science fiction')
>>> mo.group()
'Star Trek'
>>> mo.group(1)
'Trek'
```

### Optional matching

* `()?` optional group

```py
>>> pattern = re.compile(r'James (T. )?Kirk')
>>> mo1 = pattern.search('James Kirk is the captain')
mo1.group()

>>> mo2 = pattern.search('James T. Kirk is the captain')
mo2.group()
```

optional country code
```py
pattern = re.compile(r'(\+\d{2} )?\d{2} \d{2} \d{2} \d{2}')
mo1 = pattern.search("MF's number is +45 33 92 33 00")
mo1.group()

mo2 = pattern.search("MF's number is 33 92 33 00")
mo2.group()
```

### Matching zero or more
* `*`: match zero or more, any group that precedes the asterisk can occur any number of times

```py
>>> pattern = re.compile(r'at(c)*t')
>>> mo1 = pattern.search('gatcctccat')
mo1.group()
'atcct'
>>> mo2 = pattern.search('gattccatga')
mo2.group()
'att'
```

### Matching one or more
* `+`: match one or more

```py
>>> pattern = re.compile(r'at(c)+t')
>>> mo1 = pattern.search('gatcctccat')
>>> mo1.group()
'atcct'

>>> mo2 = pattern.search('gatctccatt')
>>> mo2.group()
'atct'

>>> mo3 = pattern.search('gattccatga')
>>> mo3 == None
True
```

### Matching specific repetitions with Braces
* `(pat){n}` with match _n_ repetitions of _pat_
* `(pat){m,n}` with match from _m_ to _n_ repetitions of _pat_

```py
>>> pattern = re.compile(r'(tcct){1,2}')
>>> mo1 = pattern.search('gatcctccat')
>>> mo1.group()
'tcct'
>>> mo2 = pattern.search('tccttcctga')
>>> mo2.group()
'tccttcct'
>>> mo3 = pattern.search('tc')
>>> mo3 == None
True
```
## Greedy and non-greedy matching
* default regex is _greedy_: match the longest string possible
* _lazy_ matches the shortest version `{}?`

```py
>>> s = 'tccttcctga'

>>> pattern_greedy = re.compile(r'(tcct){1,2}')
>>> mo1 = pattern_greedy.search(s)
>>> mo1.group()
'tccttcct'

>>> pattern_lazy = re.compile(r'(tcct){1,2}?')
>>> mo2 = pattern_lazy.search(s)
>>> mo2.group()
'tcct'
```

## `findall()`
* returns every match for searched string

```py
>>> stein = 'a rose is a rose is a rose'
>>> pattern = re.compile(r'rose')
>>> mo = pattern.search(stein)
>>> mo.group()
'rose'

>>> pattern.findall(stein)
['rose', 'rose', 'rose']
```
* if there are groups in search pattern `findall()` will return a list of tuples

```py
>>> msg = 'Please return the call at 33 92 33 00, otherwise you will be fined 5,000 DKK'
>>> pattern = re.compile(r'(\d{2}) (\d{2}) (\d{2}) (\d{2})')
>>> pattern.findall(msg)
[('33', '92', '33', '00')]
```

## Character classes
* shorthand character classes, e.g., `\d` is ´(0|1|2|3|4|5|6|7|8|9)´

| Char  classe | Meaning |
| :-: | --- |
| `\d` | 0-9 |
| `\D` | any char not 0-9 |
| `\w` | any letter, 0-9, underscore|
| `\W` | any char not letter, 0-9, underscore|
| `\s` | any space, tab, newline char|
| `\S` | any char not space, tab, newline char |

```py
>>> s = '3 Engineering Consoles, 4 Science Consoles, and 2 Tactical Consoles.'
>>> pattern = re.compile(r'\d+\s\w+\s\w+')
>>> pattern.findall(s)
['3 Engineering Consoles', '4 Science Consoles', '2 Tactical Consoles']
```

### Custom char classes

```py
>>> s = 'At Tænke og Tro: Efterår 1939'
>>> pattern_vowel = re.compile(r'[aeiouæøåAEIOUÆØÅ]')
>>> pattern_vowel.findall(s)
```

* add range `[a-zA-Z0-9]`

```py
>>> s = 'At Tænke og Tro: Efterår 1939'
>>> pattern_vowel = re.compile(r'[a-zæøåA-ZÆØÅ0-9]')
>>> pattern_vowel.findall(s)
```

* inside `[]` normal regex are not interpreted (no need for escape chars)
* negative class indicated with `^` caret

```py
>>> s = 'At Tænke og Tro: Efterår 1939'
>>> pattern_consonant = re.compile(r'[^aeiouæøåAEIOUÆØÅ]')
>>> pattern_consonant.findall(s)
```

## `^` and `$`

* caret outside char class indicate that a match must occur in the beginning of a string

```py
>>> s = 'hello Spock'
>>> pattern = re.compile(r'^hello')
>>> mo = pattern.search(s)
>>> mo
<re.Match object; span=(0, 5), match='hello'>
>>> pattern.search('Spock says hello') == None
True
```

* dollar sign at the end indicates that a string must end with the pattern

```py
>>> s = "Spock's favorite number is 23"
>>> pattern = re.compile(r'\d+$')
>>> mo = pattern.search(s)
mo
<re.Match object; span=(26, 28), match='23'>

>>> pattern.search("Spock's favorite number is twenty three") == None
True
```

## Wildcard char

* `.`

```py
>>> s = 'a cat wears no hat'
>>> pattern = re.compile(r'.at')
>>> pattern.findall(s)
['cat', 'hat']
```
* match everything `.*`

```py
>>> s = 'first dataloader.py; second modeltraining.py'
>>> pattern = re.compile(r'first (.*); second (.*)')
>>> mo = pattern.search(s)
>>> mo.group(1)
'dataloader.py'
>>> mo.group(2)
'modeltraining.py'
```

* `.*` is greedy by default, matches as much text as possible
* for non-greedy `.*?`

```py
>>> s = '<state change> is a type of event>'
>>> nongreedy = re.compile(r'<.*?>')
>>> mo = nongreedy.search(s)
>>> mo.group()
'<state change>'

>>> greedy = re.compile(r'<.*>')
>>> mo = greedy.search(s)
>>> mo.group()
'<state change> is a type of event>'
```

* match newlines with dot char
* dot-start will match everything except newline½
* use `re.DOTALL` in `re.compile()` to match newline

```py
>>> spock = 'Computers make excellent and efficient servants,\nbut I have no wish to serve under them.'

>>> pattern = re.compile(r'.*')
>>> pattern.search(spock).group()
'Computers make excellent and efficient servants,'

>>> pattern = re.compile(r'.*', re.DOTALL)
>>> pattern.search(spock).group()
'Computers make excellent and efficient servants,\nbut I have no wish to serve under them.'
```

### Case-insensitive matching

```py
>>> s0 = 'Spock is a Vulcan'
>>> s1 = 'Spock is a vulcan'

>>> pattern = re.compile(r'vulcan', re.I)
>>> pattern.search(s0).group()
'Vulcan'

>>> pattern.search(s1).group()
'vulcan'

>>> s2 = '"vulcan" is spelled "Vulcan"'
>>> pattern.findall(s2)
['vulcan', 'Vulcan']
```

### Substituting with `sub()`

```py
>>> s = 'Captain Spock is part vulcan with a T-negative blood type'
>>> pattern = re.compile(r'Captain \w+')
>>> pattern.sub('ANON', s)
'ANON is half vulcan with a T-negative blood type'
```

* keep part of censored pattern

```py
>>> s = 'Captain Spock is part vulcan with a T-negative blood type'
>>> pattern = re.compile(r'Captain (\w)\w+')
>>> pattern.sub(r'\1****', s)
'S**** is half vulcan with a T-negative blood type'
```

### Managing complex regex

```py
s = 'my email is cpt.spock@enterprise.us.com'
pattern = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
pattern.search(s).group()
```

```py
pattern = re.compile(r'''
  [\w.+-]+  # username
  @         # @ symbol
  [\w-]+#
  \.[\w.-]
  +
  ''', re.VERBOSE)
pattern.search(s).group()

```


username, an @ symbol, domain name, a dot, and the domain.

pattern = re.compile(r'''
  [\w.+-]+
  ''', re.VERBOSE)

















--------------
