
from dataclasses import dataclass

@dataclass
class Protocol:
    name: str
    start_page: int
    end_page: int

    @property
    def pages(self):
        return range(self.start_page - 1, self.end_page) # start at page n-1 because pdf library is 0-indexed

class Config:
    def __init__(self, yaml_content):
        self.version = yaml_content["version"]
        self.protocols = []
        for protocol, content in yaml_content["protocols"].items():
            self.protocols.append(Protocol(protocol, content["start"], content["end"]))
