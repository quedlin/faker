from locust import HttpUser, TaskSet, task, between
import random
import string

url = 'https://albqjzdb.top/login'

#email = ''
#password = ''
#_token = '5vVmiqgtPYnCUt5USMHKmuckcvNbfgpduHQvzEp8'


with open('names.txt') as file:
    names_list = [line.rstrip() for line in file]

with open('surnames.txt') as file:
    surnames_list = [line.rstrip() for line in file]
    
with open('passwords.txt') as file:
    passwords_list = [line.rstrip() for line in file]

email_providers = [
	'gmail.com',
    'yahoo.com',
	'hotmail.com',
    'aol.com',
	'hotmail.co.uk',
	'hotmail.fr',
	'msn.com',
	'yahoo.fr',
]



def genToken(length):    
    return ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length)))

def genNumbers(length):    
    return ''.join((random.choice('0123456789') for i in range(length)))

def genPassword():
    password = genToken(random.randint(8, 12))
    match random.randint(0, 1):
        case 0:
            password = random.choice(passwords_list)
        case 1:
            password = random.choice(passwords_list) + genToken(random.randint(1, 2)) 
    return password

def genWords(length):    
    return ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length)))


def genEmailProvider():
    asd = random.randint(1, 100)
    if (asd > 5):
        return 'gmail.com'
    else:
        return random.choice(email_providers)


def genEmail():
    email = genWords(10) + '@' + genWords(8) + '.' + genWords(3)
    match random.randint(0, 1):
        case 0:
            email = random.choice(names_list) +'.'+random.choice(surnames_list) + genToken(1) + genNumbers(random.randint(1, 4)) + '@' + genEmailProvider()
        case 1:
            email = random.choice(names_list).lower() + genToken(1) + genNumbers(random.randint(2, 4)) + '@' + genEmailProvider()
    return email




class WebsiteUser(HttpUser):
    
    wait_time = between(10, 15)
    host = 'https://albqjzdb.top'
    
	
    @task
    def login(self):
        self.client.post("/login", {"email":genEmail(), "password":genPassword(), "_token":genToken(40)})
    
