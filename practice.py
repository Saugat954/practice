#practice

#class in python
class info:
    name = "saugat"
    city = "Brisbane"
    def func(self):
        print(f"My name is {self.name} and I live in {self.city}")

a = info()
a.func()

#class using Constructors
class person:
    def __init__(self,name, city):
       
        self.name = name
        self.city = city
    def info(self):
        print(f'My name is {self.name} and I live in {self.city}')

personA = person("saugat", "Brisbane")
personA.info()

#Decorators in python

def greet(fx):
    def mfx(*arguments,**keyword):
        print("Good morning")
        fx(*arguments,**keyword)
        print("Thanks for using this function")
    return mfx
    
@greet
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)
 
greet(add)(5,4)
hello()
