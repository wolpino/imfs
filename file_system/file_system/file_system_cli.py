import argparse
import cmd
from typing import List
from constants import SLASH, NodeType
from file_system_manager import FileSystemManager

class FileSystemCli(cmd.Cmd):
    prompt = "(In Memory FileSystem)>> "
    intro = "Welcome to a simple in-memory file system. Enter 'help' for avail commmands"
    
    def __init__(self):
        super().__init__()
        self.fsm = FileSystemManager()

    def do_path(self, argline:str="") -> str:
        """Returns the current directory path"""
        return "test"

    def do_list(self, argline:str="") -> List[str]:
        """List files and directories in the current directory."""
        return self.fsm.list_children()
    

    def do_search(self, search_term: str):
        search_results = self.fsm.search(search_term)
        if not search_results:
            return "no matches found"
        else:
            for result in search_results:
                print(result)
            return 
    
    def do_change_dir(self, dir_name: str) -> None:
        "Change the current directory. Usage: change_dir <directory_name>"
        # Move to child directory
        if dir_name in self.fsm.current_directory.children.keys():
            target_node = self.fsm.current_directory.children[dir_name]
            if target_node.type == NodeType.FILE:
                print(f"{dir_name} is a file, not a directory")
                return
            self.fsm.update_to_child(dir_name)
            return
        else:
            # TODO implement search and add ability to move to a different directory
            print(f"{dir_name} is not a parent or child of the current working directory")
        # move to parent directory
        if self.fsm.current_path == self.fsm.file_system.root:
            print("Already at root directory")
            return
        if dir_name == self.fsm.current_directory.parent.name:
            self.fsm.update_to_parent()
            return

    # TODO add file flag
    def do_create(self, name: str, flag: bool=False) -> str:
        """Create a file or directory in the current directory. Usage: create_dir <name>"""
        if flag:
            new_file = self.fsm.create_file(name)
            # TODO handle possible failures if new_file not returned
            return "File created"
        new_dir = self.fsm.create_directory(name)
        return "Directory created"

    def do_write(self, file:str, content:str):
        "Write content to a file. Usage: write <file_name> <content>"
        self.fsm.write(file, content)
        return f"Content written to {file}"

    def do_read(self, file: str):
        "Read the content of a file. Usage: read <file_name>"
        return self.fsm.read(file)

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
    FileSystemCli().cmdloop()

    