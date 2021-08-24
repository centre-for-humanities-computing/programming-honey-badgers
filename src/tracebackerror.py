"""
Breakdown of traceback error message of SyntaxError
* breaking down the error message
    * The file name where the invalid syntax was encountered
    * The line number and reproduced line of code where the issue was encountered
    * A caret (^) on the line below the reproduced code, which shows you the point in the code that has a problem
    * The error message that comes after the exception type SyntaxError, which can provide information to help you determine the problem
"""

def main():
    2 +* 3

if __name__=="__main__":
    main()