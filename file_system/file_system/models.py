from typing import List, Optional

from file_system.file_system.constants import NodeType, Permission


class Node:
    """ a tree node that represents a directory or a file """
    def __init__(self, name, type, parent=None, permissions=0):
        # the name of the file or directory 
        self.name: str = name
        # distinguish between files and directories
        self.type: NodeType = type
        # file content as list of strings (directories have empty content)
        self.content: List[str] = []
        # dictionary of children files and directories of current directory
        self.children: dict[str, 'Node'] = {}
        # parent node
        self.parent: Optional['Node'] = parent
        # required permission level
        self.permission: int = 0
    
    def get_content(self):
        return self.content


class FileSystem:
    """tree structure to hold file system"""
    def __init__(self):
        self.root = Node("/", NodeType.ROOT, None)
        self.name = '/'     