"""
Regex examples


Assignments:
    1. Add national code to non-regex searches
"""
import re

def us_phone(text):
    """ find us phone number without regex
    example: 000-000-0000
    
    """
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    
    return True


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




def main():
    print('[INFO] Welcome to fun til regex...\n')


    print('\n'+'*'*50)
    print('\n[INFO] search for Danish phone numbers in')
    # test data
    num_str = '314-398-4725'
    dk_num = '26 83 26 08'

    print('[INFO] Finding phone numbers without regex in:\n')
    msg = 'Please return the call at 33 92 33 00, otherwise you will be fined 5,000 DKK'
    print(msg)
    for i in range(len(msg)):
        chunk = msg[i:(i + 11)]
        if dk_phone(chunk):
            print(f'[RESULT] Found a phone number {chunk}, please take appropriate action')

    print(f'\n[INFO] Finding phone numbers with regex in:\n {msg}')
    pattern = r'\d\d \d\d \d\d \d\d'
    pattern = r'\d{2} \d{2} \d{2} \d{2}'
    print(pattern)
    dk_phone_pattern = re.compile(pattern)
    mo = dk_phone_pattern.search(f'My number is {dk_num}')# match object
    print(f'Phone number found {mo.group()}')

    print('\n[INFO] Grouping with parenthesis')
    pattern = r'(\d{2} \d{2}) (\d{2} \d{2})'
    print(pattern)
    dk_phone_pattern = re.compile(pattern)
    mo = dk_phone_pattern.search(f'My number is {dk_num}')
    for i in range(3):
        print(f'Group {i}: {mo.group(i)}')


    print('\n'+'*'*50)
    print('\n[INFO] search for RFC 5322 compliant emails in:\n')
    strwemail = 'my email is cpt.spock@enterprise.us.com'
    email = 'cpt.spock@enterprise.us.com'
    print(strwemail+'\n')

    # compact pattern
    print('[INFO] compact pattern')
    pattern0 = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    print(pattern0.search(strwemail).group())
    
    # less compact with VERBOSE argument
    ## validate email pattern: https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression
    print('[INFO] verbose pattern')
    pattern1 = re.compile(r'''
        [\w.+-]+  # username
        @         # @ symbol
        [\w-]+    # domain name
        \.        # dot
        [\w.-]+   # domain
        ''', re.VERBOSE)
    print(pattern1.search(strwemail).group())
    ## componenents of an email
    # username, numerals, letters and '.' (one or more) and '-'
    print('[INFO] username')
    pattern2 = re.compile(r'[\w.+-]+') 
    print(pattern2.search(email).group())

    # '@'
    print('[INFO] add "@"')
    pattern3 = re.compile(r'[\w.+-]+@')
    print(pattern3.search(email).group())

    # domain name
    print('[INFO] add domain')
    pattern4 = re.compile(r'[\w.+-]+@[\w-]+')
    print(pattern4.search(email).group())

    # dot
    print('[INFO] add "."')
    pattern5 = re.compile(r'[\w.+-]+@[\w-]+\.')
    print(pattern5.search(email).group())

    # domain
    print('[INFO] add domain')
    pattern6 = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    print(pattern6.search(email).group())

if __name__=="__main__":
    main()