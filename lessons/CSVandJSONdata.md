# CSV files and JSON data

Der er ikke læst korrektur på det her :-P


some intro about the different data structures and why it is important.
JSON allows complexity and different types.

2 hours of horoscope challenge  + short presentations about what they have done.

Bygning 1481: 264

## CSV files

A CSV file is a plain text file, meaning that they contain letters and numbers. CSV stands for 'comma-separated values' indicating that our data is separated by commas, structuring our data in tabular form.
Each line in the file represents a row in a table and the commas indicate the division into cells.

You might have worked with tables and spreadsheets in Microsoft Excel. You can read a CSV-file into Excel but the file itself lacks some of the information you will get from Excel, e.g., value types (everything is a string in a CSV-format). However, with CSV files we gain *simplicity*!

Opening a CSV file in a text editor (such as TextEdit) you will see something like figure A. When opening the same CSV file in Excel, Excel add som formatting to the dates. You will see something like figure B.

<center>
<table>
<tr>
<td> <img src="Images/csv_inTextEditor.png" alt="Drawing" style="width: 250px;"/>
A</td>
<td> <img src="Images/csv_inExcel.png" alt="Drawing" style="width: 250px;"/> B</td>
</tr></table>
</center>


As a string can contain commas within it, CSV files also have escape characters to distinguish between these and those making a boundaries between two cells.
In Python there exists a `csv` module for reading and writing tabular data in CSV format.

### CVS Reader
To read data from a CSV file we first need to create a `reader` object.
The `reader` object will iterate over the lines in the given CSV file.

```
import csv

zodiacFile =  open('zodiac.csv')
reader = csv.reader(zodiacFile)
zodiacData = list(reader)
zodiacData

>>>
[['Pisces', '19-02', '20-03'],
 ['Aries', '21-03', '19-04'],
 ['Taurus', '20-4', '20-05'],
 ['Gemini', '21-5', '20-6'],
 ['Cancer', '21-06', '22-07'],
 ['Leo', '23-07', '22-08'],
 ['Virgo', '23-08', '22-09'],
 ['Libra', '23-09', '22-10'],
 ['Scorpio', '23-10', '21-11'],
 ['Sagittarius', '22-11', '21-12']]
```


By calling the `list()` function on our `reader` object we get a list of lists. A list of lists is called a *matrix* and we can access the data in the list by specifying the row and column: ```list[row][col]```.

```
zodiacData[0][0]
>>>
'Pisces'

zodiacData[7][2]
>>>
'22-10'
```

**Remember**: The computer counts from 0!

### Read files with for loop
For larger files we want to use the reader in a `for` loop.

```
import csv

zodiacFile =  open('zodiac.csv')
reader = csv.reader(zodiacFile)
for row in reader:
    print(str(row))

>>>

['Pisces', '19-02', '20-03']
['Aries', '21-03', '19-04']
['Taurus', '20-4', '20-05']
['Gemini', '21-5', '20-6']
['Cancer', '21-06', '22-07']
['Leo', '23-07', '22-08']
['Virgo', '23-08', '22-09']
['Libra', '23-09', '22-10']
['Scorpio', '23-10', '21-11']
['Sagittarius', '22-11', '21-12']

```

From what is printed above we see that the first column contains the name of the zodiac sign, the second the start date and the third column the end date. This information can be added into a header row of our CSV file. To do this we use `DictReader` and `DictWriter`.

Instead of read and write a CSV file as lists, as the `reader` and `writer` objects, `DictReader` and `DictWriter` use dictionaries instead. The first row of the CSV file is used as the keys of the dictionaries.

```
import csv
zodiacFile =  open('zodiac.csv')
dictReader = csv.DictReader(zodiacFile, ['Zodiac Sign', 'Start Date', 'End Date'])
for row in dictReader:
    print(row['Zodiac Sign'], row['Start Date'], row['End Date'])

>>>

Pisces 19-02 20-03
Aries 21-03 19-04
Taurus 20-4 20-05
Gemini 21-5 20-6
Cancer 21-06 22-07
Leo 23-07 22-08
Virgo 23-08 22-09
Libra 23-09 22-10
Scorpio 23-10 21-11
Sagittarius 22-11 21-12

```


### CSV Writer
A sharp astrology enthusiast will notice that our data set does not contain data on aquarius and capricorn. To add this we need a `writer` object to write to our CSV file.

```
import csv
restOfZodiacFile = open('restOfZodiacFile.csv', 'w', newline='')
outputWriter = csv.writer(restOfZodiacFile)
outputWriter.writerow(['Capricorn', 22-12, 19-01])
outputWriter.writerow(['Aquarius', 20-01, 18-02])

>>>

22
```

The `writerow()`method takes a list as argument. The list will be a row in the outputted CSV file and each value in the list is placed in a cell.
The `writerow()`method returns and integer which tell us how many characters have been written to our file.

However, this have added the data about aquarius and capricorn in a separate file. If we want to add it to the existing file we need to pass our `zodiacFile` to the `writer` object open for appending - note the `a+` in the following code example.
We use `DictWriter` to add the headers in the first row:

```
import csv

allZodiacFile = open('zodiac.csv', 'a+', newline='')
outputWriter = csv.DictWriter(allZodiacFile,fieldnames = ['Zodiac Sign', 'Start Date', 'End Date'])
outputWriter.writerow({'Zodiac Sign': 'Capricorn', 'Start Date': '22-12', 'End Date':'19-01'})
outputWriter.writerow({'Zodiac Sign': 'Aquarius', 'Start Date': '20-01', 'End Date':'18-02'})

>>>

22
```

Our CSV file ```zodiac.csv``` now contains data on all the zodiac signs:

```
Pisces,19-02,20-03
Aries,21-03,19-04
Taurus,20-4,20-05
Gemini,21-5,20-6
Cancer,21-06,22-07
Leo,23-07,22-08
Virgo,23-08,22-09
Libra,23-09,22-10
Scorpio,23-10,21-11
Sagittarius,22-11,21-12
Capricorn,22-12,19-01
Aquarius,20-01,18-02
```



## pandas
Additional to the `csv` module there are multiple other Python libraries for reading and writing to data sets as well as doing data analysis.

`pandas` is a common used library used for working with data sets. It has powerful built-in functions for analysing, cleaning, exploring, and manipulating data.

### Series

`pandas` series is a one dimensional array which can hold any type of data (contrary to our CSV-files which only contain string values)

```
import pandas as pd

list = ['aries', 'leo', 'virgo', 2]
var = pd.Series(list)
print(var)

>>>

0       aries
1       leo
2       virgo
3       2
dtype:  object

```

### DataFrames
When creating a `Series` we can add a key/value object - like a dictionary. A `Series` object is like a column in a table. Hence, multiple `Series` can make up a multidimensional table - also called a `DataFrame`.


```
import pandas as pd

elements = {
  "fire": ['Aries', 'Leo', 'Sagittarius'],
  "earth": ['Taurus', 'Virgo', 'Capricorn'],
  "air": ['Gemini', 'Libra', 'Aquarius'],
  "water": ['Cancer', 'Scorpio', 'Pisces']
}

df = pd.DataFrame(elements)
print(df)

>>>

          fire      earth       air    water
0        Aries     Taurus    Gemini   Cancer
1          Leo      Virgo     Libra  Scorpio
2  Sagittarius  Capricorn  Aquarius   Pisces


```

With the `loc` method we can access specific rows in our DataFrame.

```
print(df.loc[1])
>>>

fire          Leo
earth         Virgo
air           Libra
water         Scorpio
Name: 1, dtype: object

```

### Load data sets
We can use ```pandas``` to read CSV-files. We add the headers to the `DataFrame` otherwise will `pandas` treat the first row  of our data set (`Pisces  19-02  20-03`) as the header.:

```
import pandas as pd

df = pd.read_csv('zodiac.csv', names = ['Zodiac Sign', 'Start Date', 'End Date'])

print(df.to_string())

>>>

      Zodiac Sign Start Date End Date
0        Pisces      19-02    20-03
1         Aries      21-03    19-04
2        Taurus       20-4    20-05
3        Gemini       21-5     20-6
4        Cancer      21-06    22-07
5           Leo      23-07    22-08
6         Virgo      23-08    22-09
7         Libra      23-09    22-10
8       Scorpio      23-10    21-11
9   Sagittarius      22-11    21-12
10    Capricorn      22-12    19-01
11     Aquarius      20-01    18-02
```

The `to_string()` method prints out the entire data frame. If we work on a big data set and wnat to get an idea of how the data set looks like, we can print the first five rows with the `head()` methods and the last five rows with the `tail()` method.

In the example below, the values in the CSV file is not separated by a comma but by a `|`. We pass this information to our `pandas read_csv` object with: `sep='|'`.

```
import pandas as pd

df = pd.read_csv('horoscopes_NYtimes_2013-2016.csv', sep='|')
df.columns = ['number', 'horoscope', 'date', 'zodiac sign']
df.head()

>>>
      number 	horoscope 	                                     date 	   zodiac sign
0 	     0 	 You’re not the sort to play safe and even if y... 	12-01-2013 	aries
1 	     1 	 There is no such thing as something for nothin... 	12-02-2013 	aries
2 	     2 	 As the new moon falls in one of the more adven... 	12-03-2013 	aries
3 	     3 	 You will hear something amazing today but can ... 	12-04-2013 	aries
4 	     4 	 A friend or colleague you have not seen for a ... 	12-05-2013 	aries
```

### Cleaning Data
A useful feature of the `pandas` library is the way we can clean data and handle missing data.

If there are empty cells in a data set our data analysis might be wrong. With the method `dropna()` we remove all rows which contains empty cells. When working with big data sets it is usually OK to remove a few rows.

```
import pandas as pd

df = pd.read_csv('example.csv')
new_df = df.dropna()
```

The method `dropna()` returns a new `DataFrame` -- here saved in the variable `new_df` -- and does not change in the original `DataFrame`.

If we want to makes changes in the original `DataFrame` we add the argument `inplace = True` to the `dropna()` method:

```
import pandas as pd

df = pd.read_csv('example.csv')
df.dropna(inplace = True)
```

Instead of removing an entire row we can also replace empty cells with a value using the `fillna()` method.

```
import pandas as pd

df = pd.read_csv('example.csv')

# replacing empty cells in a specific column:
df['Example Column'].fillna(130, inplace = True)

# replacing empty cells for entire DataFrame
new_df = df.fillna(130, inplace = True)
```

## JSON Data


Data sets can be stored as JSON and is often used when sending and receiving data from servers. A JSON file plain text file, but has the format of an object.

JSON stands for **J**ava**S**cript **O**bject **N**otation and was originally developed for JavaScript. However, JSON files is saved as plain text, so we do not need to learn/write any JavaScript to in order to work with JSON data.

Many websites and APIs use JSON format for their data. It is therefore highly useful to learn to work with JSON data.

If you open a JSON file in a text editor, like TextEdit, you will something like this:


![JSON file opened in TextEdit](Images/JSON_inTextEdit.png =500x)


### Import JSON Data with pandas

`pandas` has a built-in `read_json` function which import JSON strings and files into a `pandas DataFrame`.


```
import pandas as pd

df = pd.read_json('horoscopes.json')

print(df.head())

>>>

    sign       date                      horoscope
0  aquarius 2021-08-19  You've been like a diamond in the rough in rec...
1    pisces 2021-08-19  As a Pisces, you're cosmically guided by the e...
2     aries 2021-08-19  Youve been pushing harder than ever to make he...
3    taurus 2021-08-19  The universe knows you're prone to holding bac...
4    gemini 2021-08-19  As a Gemini, your world revolves around the in...


```

Again, we can access a specific element in the `DataFrame` with the `loc` method:

```
print(df.loc[7][2])
>>>

The world has been testing your lifestyle, Virgo.
You've been working hard to deepen your relationship
with your work and body. Thursdays skies act as a progress
check, as the illuminating sun locks eyes with growth-giving
Jupiter. This optimistic pairing highlights what still needs
releasing and renewal, before you can fully embrace
a work/life balance that supports all your needs.


```

### Read JSON respons from a link

The webpage [http://ohmanda.com/api/horoscope/](http://ohmanda.com/api/horoscope/) offers daily horoscopes in JSON format. Here is a small code example which receives JSON data on the daily horoscope for aquarius:
```
url = "https://ohmanda.com/api/horoscope/aquarius/"

response = urlopen(url)
data_json = json.loads(response.read())
df = pd.json_normalize(data_json)
print(df)

>>>

    sign        date                       horoscope
0  aquarius  2021-08-20  It seems as if the universe has supplied you w...

```

## Horoscope Challange

Write a program which gives you today's horoscope!

### Ideas
1. Write a program which receives today's horoscope for your zodiac sign.
Access the horoscope string and save it in a text file.


- Hint:
```
# save a txt-file
outputfile = open('outputfile.text', 'w')
n = outputfile.write("text you want to output)
outputfile.close()
```


2. Let the program take a user input which is one of the 12 zodiac signs. Your program should return the daily horoscope of the inputted zodiac sign and save it in a text file.

- Hint:
```
userInput = input("[Message to user]")

```
3. Write a program that receives JSON data on the daily horoscopes for all the zodiac signs and save it in a CSV-file.

* Hint: Use `for` loops.

4. Let the user input birth date, find the matching zodiac sign and return today's horoscope.

* Hint: The dates for the zodaic signs can be found in the file `zodiac_dates.csv`.

5. Is your programme robust? Or does it crash if the user input something which is not a zodiac sign?
.
