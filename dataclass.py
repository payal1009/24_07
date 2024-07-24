#without dataclass
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
obj=person("payal",21)
print(obj)


#with dataclass example 1
from dataclasses import dataclass
@dataclass
class student:
    name:str
    age:int
    profession:str
    #profession:str="student"  gives default value for profession as student
obj2=student("payal",21,"CSE Student")
print(obj2)


#with dataclass example 2
@dataclass
class x:
    name:str
    age:int
@dataclass
class y(x):
    id:int
    dept:str
obj3=x("payal",21)
obj4=y("payal",21,10,"UI")
print(obj3)
print(obj4)