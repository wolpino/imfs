from typing import List


class Node():
    """ a tree node that represents a directory or a file """
    def __init__(self):
        # the name of the file or directory 
        self.name: str = ""
        # distinguish between files and directories
        self.isFile: bool = False
        # file content as list of strings (directories have empty content)
        self.content: List[str] = []
        # dictionary of children files and directories of current directory
        self.children: dict[str, 'Node'] = {}

