import datetime

class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]
    
    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age
    
    def setMood(self, happy=False):
        if happy:
            self.mood = 'happy'
            print(f'{self.name.split()[0]}: I have no regrets over past mistakes')
        else:
            self.mood = 'angry'
            print(f'{self.name.split()[0]}: #@*%')#grawlix
        
    def __repr__(self):
        return f'[Person: {self.name}, {self.age}, {self.sex}]'

class Researcher(Person):
    def __init__(self, pay=10, areas=['research'],  **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.pay = pay
        self.areas = areas

    def giveBonus(self, bonus):
        self.pay = self.pay + bonus

class PrincipalInvestigator(Researcher):
    def giveBonus(self, bonus, painandsuffering=.10):
        Researcher.giveBonus(self, bonus * (1 + painandsuffering))

if __name__=='__main__':

    kln = Person('Kristoffer L. Nielbo', age=44, sex="male")
    print(f'{kln.name} is a {kln.sex} specimen of {kln.age} years')
    print(f'Mr. {kln.getSurname()} was born in {kln.getBirthyear()}')
    kln.setMood()

    print(kln)

    kln = Researcher(
        name='Kristoffer L. Nielbo',
        age=44,
        sex="male",
        areas=['culture analytics', 'humanities computing'],
        )
    print(kln)
    #print(kln)
    #print(dir(kln))# operator overloading of repr or str in Person
    #print(kln)
    '''
    print(f'{kln.name} is a {kln.sex} specimen of {kln.age} years and earns {kln.pay} squishies')
    kln.giveBonus(1)
    print(kln.pay)
    for area in kln.areas:
        print(f'Dr. {kln.getSurname()} works in {area}')

    kln = PrincipalInvestigator(
        name='Kristoffer L. Nielbo', 
        age=44, sex="male", 
        areas=['culture analytics', 'humanities computing']
        )
    kln.giveBonus(1)
    print(kln.pay)
    kln.setMood(happy=True)
    '''
    