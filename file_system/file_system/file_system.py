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

    def do_create(self, name: str, file: bool=False) -> None:
        "Create a file or directory in the current directory. Usage: create <name> [--file]"
        newNode = Node()
        newNode.name = name
        newNode.isFile = file
        self.current_directory.children[name] = newNode
        print(f"{'File' if file else 'Directory'} created")

    def do_read(self, file: str):
        "Read the content of a file. Usage: read <file_name>"
        fileNode = self.current_directory.children[file]
        print(fileNode.content) # TODO enhance output

    def do_exit(self, argline:str) -> bool:
        """Exit the file system."""
        print("Exiting the file system.")
        return True
    
if __name__ == "__main__":
    FileSystem().cmdloop()