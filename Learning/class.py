class Dep:
    def __init__(self,name,operator,version):
        self.name = name
        self.operator = operator
        self.version = version

dep1 = Dep("django","==","2.2.0")

print(dep1.name)

from  dataclasses import dataclass

@dataclass
class D:
    n:str
    o:str
    v:str
    r:str
dep2 = D("dja","=","2.2.1","dja=2.2.1")
print(dep2.o)