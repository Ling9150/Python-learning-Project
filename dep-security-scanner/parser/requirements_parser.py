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
    box = []
    with open(file_path,"r",encoding="utf-8")as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        part = line.split("==")
        pac_name = part[0].strip()
        pac_version = part[1].strip()
        card = Dependency(
            name = pac_name,
            operator = "==",
            version=pac_version,
            raw_line=line
        )
        box.append(card)
    return box

if __name__ == "__main__":
    parse_req("../test_files/sample_requirements.txt")
