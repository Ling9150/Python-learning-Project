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

def parse_req(file_path):
    deps = []
    operators = ["==", ">=", "<=", "~=", ">", "<"]
    with open(file_path,"r",encoding="utf-8")as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        operator_found = None
        for op in operators:
            if op in line:
                operator_found = op
                break
        if operator_found is None:
            dep = Dependency(
                name=line,
                operator=None,
                version=None,
                raw_line=line
            )
            deps.append(dep)
            continue
        name,version = line.split(operator_found,1)
        dep = Dependency(
            name = name.strip(),
            operator = "==",
            version=version.strip(),
            raw_line=line
        )
        deps.append(dep)
    return deps

if __name__ == "__main__":
    parse_req("../test_files/sample_requirements.txt")
