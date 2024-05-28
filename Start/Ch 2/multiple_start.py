# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


class C(A, B): #inherites from both A and B
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name) #class A but why? because it goes by the order A,B so A is first . when change to B we get class B


c = C()
print(C.__mro__) #Class C -> Class A -> Class B -> object 
c.showprops()