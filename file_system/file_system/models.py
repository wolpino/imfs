from typing import List

from constants import NodeType


# TODO make Node base class and create File and Dir classes that inherit Node
class Node:
    """a tree node that represents a file or directory"""
    def __init__(self, name: str, node_type: NodeType = NodeType.DIRECTORY):
        # the name of the file or directory 
        self.name: str = name
        self.type: NodeType = node_type
        self.content: List[str] = []
        self.children: dict[str,'Node'] = {}
        self.parent: 'Node' = None

    def get_type(self):
        return self.type
    
    def get_children(self):
        return self.children
    
    def read(self):
        return self.content
    
    def write(self, val):
        self.content.append(val)
        return self
    
class FileSystem:
    """tree structure to hold file system"""
    def __init__(self):
        self.root = Node("/", NodeType.DIRECTORY)        
    