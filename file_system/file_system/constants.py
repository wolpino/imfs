from enum import Enum

SLASH = "/"

class NodeType(Enum):
    ROOT = "r"
    DIRECTORY = "d"
    FILE = "f"

help_category = "Help options:"

class Permission(Enum):
    OPEN = 0
    NEED_READ_ACCESS = 1
    NEED_WRITE_ACCESS = 2
    NEED_READANDWRITE_ACCESS = 3

Users = {"Lisa":{"permission": 3}, 
        "Bart":{"permission": 1}, 
        "Marge":{"permission": 2}, 
        "Homer":{"permission": 0}}


