from dataclasses import dataclass
from typing import Optional

@dataclass
class Dependency:
    name:str
    operator:Optional[str]
    version:Optional[str]
    raw_line:str

    def __str__(self):
        if self.version:
            return f"{self.name}{self.operator}{self.version}"
        return self.name

if __name__ == "__main__":
    dep1 = Dependency("django","==","2.2.0","django==2.2.0")
    dep2 = Dependency("numpy",None,None,"numpy")
    print(dep1)
    print(dep2)