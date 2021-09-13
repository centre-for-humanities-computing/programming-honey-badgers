def authorization(name, password):
    print(f'Welcome {name}')
    if password == 'correct-password':
        print('You shall pass...')
    else:
        print('You shall not pass...')

def main():
    print('[INFO] Please input your name:')
    usr = input()
    print('[INFO] Please input your password')
    pwd =  input()
    authorization(usr, pwd)

if __name__=='__main__':
    main()