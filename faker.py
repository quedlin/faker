from locust import HttpUser, TaskSet, task, between
import random
import string

url = 'https://albqjzdb.top/login'

#email = ''
#password = ''
#_token = '5vVmiqgtPYnCUt5USMHKmuckcvNbfgpduHQvzEp8'

def genToken(length):    
    return ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length)))

def genWords(length):    
    return ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length)))

def genEmail():
    return genWords(10) + '@' + genWords(8) + '.' + genWords(3)




class WebsiteUser(HttpUser):
    
    wait_time = between(10, 15)
    host = 'https://albqjzdb.top'
    
	
    @task
    def login(self):
        self.client.post("/login", {"email":genEmail(), "password":genToken(12), "_token":genToken(40)})
    
