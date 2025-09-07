import argparse
import cmd
from model import Node

class FileSystem(cmd.Cmd):
    prompt = "(In Memory FileSystem) >>"
    intro = "Welcome to a simple in-memory file system. Enter 'help' for avail commmands"
    
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.current_directory = self.root
        self.current_path = ["/"]
        self.root.name = "/"

    def do_path(self, argline:str="") -> None:
        "Returns the current directory path"
        #TODO make sure this return path > join array on /
        print(self.current_path)

    def do_list(self, argline:str="") -> None:
        "List files and directories in the current directory."
        print(self.current_directory.children.keys())

    def do_create_dir(self, name: str) -> None:
        #TODO combine creates and add file flag
        "Create a file or directory in the current directory. Usage: create_file <name>"
        newNode = Node()
        newNode.name = name
        newNode.isFile = False
        self.current_directory.children[name] = newNode
        print(f"Directory created")

    def do_create_file(self, name: str) -> None:
        "Create a file or directory in the current directory. Usage: create_file <name>"
        newNode = Node()
        newNode.name = name
        newNode.isFile = args.file
        self.current_directory.children[name] = newNode
        print(f"File created")

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

    