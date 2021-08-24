# This program says helo ad asks for my name
"""
1. how to write comments
2. print() function
3. input() function
4. printing name var
5. len()
6. str(), int(), float()

## additional concepts
7. f-strings
8. text and number equivalance
    * 42 == "42"
    * 42 == 42.0
    * 42 == 0042.000
"""

def main()
    print("Hello world!")
    print("What is you name?")
    my_name = input()
    print("It is good to meet you " + my_name)
    print("the length og your name is: ")
    print(len(my_name))
    print("What is you age?")
    my_age = input()
    print("You will be " + str(int(my_age) + 1) + " in a year")

if __name__=="__main__":
    main()