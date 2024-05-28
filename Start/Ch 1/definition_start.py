# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book(): #() needed only if the class inherites from another class
  def __init__(self,title):
    self.title = title 

# TODO: create instances of the class
book1 = Book("Brave New World") # this is how we construct an object 
book2 = Book("War and Peace") #no need to write self, object is automatically passes . self is just a convention

# TODO: print the class and property
print(book1) #this is the object itself
print(book1.title) # aproperty of that object 
