import argparse
import cmd
from typing import List
from constants import SLASH, NodeType
from models import FileSystem, Node

class FileSystemManager():
    def __init__(self):
        self.file_system: FileSystem = FileSystem()
        self.current_directory: Node = self.file_system.root
        self.current_path: List[str] = [self.file_system.root.name]
        self.search_term: str = ""
        self.requested_depth: int = 0

    # TODO add an optional variable + function to get path for any file/dir
    def get_path(self) -> str:
        if self.current_directory.name == self.file_system.root:
            return SLASH
        else:
            
            return f"{SLASH}{SLASH.join(self.current_path[1:])}"

    # TODO implement recursive list to get all children of children etc
    # TODO add flag to choo se children in current working directory, or all children below the current working directory
    def list_children(self, argline:str="") -> List[str]:
        "List files and directories in the current directory."
        return list(self.current_directory.children.keys())

    # TODO make this work :(
    # walk tree from current dir to first node [n] layers deep
    def _walk_subtree(self, current: Node, path:List[str], depth) -> str:
        while depth <= self.requested_depth:
            if current.type != str(NodeType.FILE) or current.children != []:
                current_dir = current
                for child in current_dir.children.keys():
                    path.append(child)
                    depth=+1
                    self._walk_subtree(current_dir.children[child], path, depth)
        return f"{SLASH}{SLASH.join(path[1:])}"
          
        
    # depth first search from current directory
    def _dfs(self, current: Node, search_results: List[str], path:List[str]) -> List[str]:
        if current.name == self.search_term:
            path_name = f"{SLASH}{SLASH.join(path[1:])}"
            search_results.append(path_name)
        if current.type != str(NodeType.FILE) or current.children != []:
            current_dir = current
            for child in current_dir.children.keys():
                path.append(child)
                self._dfs(current_dir.children[child], search_results, path) # recursive call to move up the tree
        return search_results


    def search(self, search_term: str):
        search_results = []
        self.search_term = search_term
        results = self._dfs(self.current_directory, search_results, self.current_path)
        return results
    
    def walk_to_depth(self, depth: int):
        self.requested_depth = depth
        results = self._walk_subtree(self.file_system.root, ["/"] , 0)
        return results

    def update_to_child(self, dir_name: str) -> None:       
        self.current_path.append(dir_name)
        self.current_directory = self.current_directory.children[dir_name]
        return

    def update_to_parent(self) -> None:       
        self.current_path.pop()
        self.current_directory = self.current_directory.parent or self.file_system.root
        return

    # TODO add more validations and move to file
    def _validate_name_availability(self, name: str) -> bool:
        if name in self.current_directory.children.keys():
            print("File or directory already exists")
            return False
        if not name:
            print("no dir name provided. Usage: create_dir <name>")
            return False
        return True

    def create_directory(self, name: str) -> Node:
        #TODO combine creates and add file flag
        self._validate_name_availability(name)
        dir_node = Node(name=name, type=NodeType.DIRECTORY)
        self.current_directory.children[dir_node.name] = dir_node
        dir_node.parent = self.current_directory
        return dir_node

    def create_file(self, name:str) -> Node:
        print('into create file')
        self._validate_name_availability(name)
        try:
            file_node = Node(name=name, type=NodeType.FILE)
            self.current_directory.children[file_node.name] = file_node
            file_node.parent = self.current_directory
            print(file_node)
            return file_node

        except Exception as e:
            print(e.__dict__)
            raise e

    def _validate_file_exists(self, file: str) -> bool:
        if file not in self.current_directory.children.keys():
            return False
        if self.current_directory.children[file].type == NodeType.DIRECTORY:
            return False
        return True

    def write(self, file: str, content: str):
        if not self._validate_file_exists(file):
            return "File not found"
        fileNode = self.current_directory.children[f"{file}"]
        fileNode.content.append(content)
        return fileNode

    def read(self, file: str):
        "Read the content of a file. Usage: read <file_name>"
        file_node = self.current_directory.children[f"{file}"]
        read_content = file_node.content
        return list(read_content)
    