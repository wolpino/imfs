import logging
from file_system_manager import FileSystemManager

class FileSystemCli():
    logger = logging.Logger
    
    def __init__(self):
        self.manager = FileSystemManager()
    def path(self):
        """Returns the current directory path"""
        try:
            path = self.manager.get_path()
            print(path)
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    def list(self):
        """List files and directories in the current directory."""
        try:
           list = self.manager.list_children()    
           print(list) 
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    def create(self, args):
        """ create a file or directory create <name> (creates directory by default add -f to create a file)"""
        try:
            if args.file:
                created = self.manager.create_file(args.name)
                print("created!")
            else:
                created = self.manager.create_directory(args.name)
            print(created)
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    def write(self, args):
        """Write content to a file. Usage: write <file_name> <content>"""
        try:
            fileNode = self.manager.write(args.file_name, args.content)
            print(f"Content written to {args.file_name}")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
    def read(self, args):
        """Read the content of a file. Usage: read <file_name>"""
        try:
            content_to_read = self.manager.read(args.file_name)
            print(content_to_read) # TODO enhance output
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    def search(self, args):
        """search for a file or directory Usage: search <search_term>"""
        try:
            search_results = self.manager.search(args.search_term)
            if not search_results:
                print("no matches found")
            else:
                for result in search_results:
                    print(result)
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
        

    


    