"""
Collection of magic 8 balls from Sweigart 2019 to exemplify

flow controls (bool), list data type (list),

"""
import random


def fortune_getter_bool(answernumber):
    """Return your magic eight-ball answer, adapted from (Sweigart 2019)

    Positional arguments:
    answernumber -- int, in range 1 to 9
    """
    if answernumber == 1:
        return 'it is certain'
    elif answernumber == 2:
        return 'it is decidedly so'
    elif answernumber == 3:
        return 'yes'
    elif answernumber == 4:
        return 'reply hazy try again'
    elif answernumber == 5:
        return 'ask again later'
    elif answernumber == 6:
        return 'concentrate and ask again'
    elif answernumber == 7:
        return 'my reply is no'
    elif answernumber == 8:
        return 'outlook not so good'
    elif answernumber == 9:
        return 'very doubtful'

def fortune_getter_list():
    messages = ['it is certain',
                'it is decidedly so', 
                'yes',
                'reply hazy try again',
                'ask again later',
                'concentrate and ask again',
                'my reply is no',
                'outlook not so good',
                'very doubtful']
    return messages[random.randint(0, len(messages) - 1)]


def main():
    # boolean 8 ball
    r = random.randint(1, 9)
    fortune = fortune_getter_bool(r)
    print(f'[PREDICTION] regarding your future: {fortune}...')

    print(f'[PREDICTION] regarding your future: {fortune_getter_list()}...')



if __name__=="__main__":
    main()