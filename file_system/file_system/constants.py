from enum import Enum


SLASH = "/"

class NodeType(Enum):
    ROOT = "r"
    DIRECTORY = "d"
    FILE = "f"