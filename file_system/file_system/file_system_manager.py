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

    # TODO add an optional variable + function to get path for any file/dir
    def get_path(self) -> str:
        if self.current_directory.name == self.file_system.root:
            return SLASH
        else:
            return f"{SLASH.join(self.current_path[:])}"

    # TODO implement recursive list to get all children of children etc
    def list_children(self, argline:str="") -> List[str]:
        "List files and directories in the current directory."
        return list(self.current_directory.children.keys())

    # depth first search from current directory
    def _dfs(self, current: Node, search_results: List[str], path:List[str]) -> List[str]:
        # save paths for 
        if current.name == self.search_term:
            path_name = f"{SLASH.join(path[:])}"
            search_results.append(path_name)
        current_dir = current
        path.append(current_dir.name)
        for child in current_dir.children.keys():
            if current_dir.children[child].type == str(NodeType.FILE) or current_dir.children[child].children == {}:
                return search_results
            # if the current path element is the current directory, set the current directory pointer
            else:
                self._dfs(current_dir.children[child], search_results, path) # recursive call to move up the tree
        return search_results


    def search(self, search_term: str):
        search_results = []
        self.search_term = search_term
        results = self._dfs(self.current_directory, search_results, self.current_path)
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

    def create(self, name: str, type=NodeType.DIRECTORY, parent=None) -> Node:
        self._validate_name_availability(name)
        newNode = Node(name, type, self.current_directory)
        self.current_directory.children[newNode.name] = newNode
        print(newNode)
        return newNode

    def _validate_file_exists(self, file: str) -> bool:
        if file not in self.current_directory.children.keys():
            return False
        if not self.current_directory.children[file].type == NodeType.DIRECTORY:
            return False
        return True

    def write(self, file: str, content: str):
        if not self._validate_file_exists(file):
            return "File not found"
        fileNode = self.current_directory.children[file]
        print(fileNode.__dict__)

        fileNode.content.append(content)
        return fileNode

    def read(self, file: str):
        "Read the content of a file. Usage: read <file_name>"
        file_node = self.current_directory.children[file]
        read_content = file_node.content
        return list(read_content)
    