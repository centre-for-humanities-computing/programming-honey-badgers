"""
zigzag pattern from (Sweigart 2019, 73)
"""
import time
import sys

def zigzag(line_width = 8 , pattern_width = 20):
    indent = 0
    indent_increasing = True
    try:
        while True:
            print(' ' * indent, end = '')
            print('*' * line_width)
            time.sleep(.1)

            if indent_increasing:
                indent += 1
                if indent == pattern_width:
                    indent_increasing = False

            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    
    except KeyboardInterrupt:
        sys.exit()

def main():
    zigzag(line_width = 5, pattern_width = 23)

if __name__=="__main__":
    main()