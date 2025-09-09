import argparse
import cmd
from typing import List
from constants import NodeType
from file_system_manager import FileSystemManager
from models import Node

class FileSystem(cmd.Cmd):
    prompt = "(In Memory FileSystem) >>"
    intro = "Welcome to a simple in-memory file system. Enter 'help' for avail commmands"
    
    def __init__(self):
        self.manager = FileSystemManager()

    def do_path(self, argline:str="") -> str:
        "Returns the current directory path"
        return self.manager.get_path()

    def do_list(self, argline:str="") -> List[str]:
        "List files and directories in the current directory."
        return self.manager.list_children()

    def do_create(self, argline) -> str:
        parts = argline.split(' ', 1)
        if(len(parts) == 2) and parts.flag:
            self.manager.create_file(parts.name)
        else:
            self.manager.create_directory(parts.name)

        return "Directory created"

    def do_write(self, argline:str):
        "Write content to a file. Usage: write <file_name> <content>"
        parts = argline.split(' ', 1)
        if len(parts) != 2:
            print("Usage: write <file_name> <content>")
            print("Ex: write myfile 'test content'")

            return
        file, content = parts
        fileNode = self.current_directory.children[file]
        fileNode.content = content
        print(f"Content written to {file}")

    def do_read(self, file: str):
        "Read the content of a file. Usage: read <file_name>"
        fileNode = self.current_directory.children[file]
        print(fileNode.content) # TODO enhance output

  
    def do_exit(self, argline:str) -> bool:
        """Exit the file system."""
        print("Exiting the file system.")
        return True
    
# Set up argument parser
parser = argparse.ArgumentParser(description='File renaming tool.')
parser.add_argument('-f', '--file', help='Create a file.', default=False, action='store_true')
parser.add_argument('-r', '--replace', nargs=2, help='Replace a substring in each file name. Usage: -r old_string new_string')

args = parser.parse_args()

    
if __name__ == "__main__":
    FileSystem().cmdloop()

    