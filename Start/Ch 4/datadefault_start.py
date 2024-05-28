# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass,field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared - if one default all must 
    # be default or there is an error and a way to override it is to use field 
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func) #this allows to set a function for the default value 


# b1=Book()
# print(b1)

b2 = Book("War and Peace", "Leo Tolstoy",1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
# no price but it is set to default
print(b2)
print(b3)