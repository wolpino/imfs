import logging
import cmd2
from constants import NodeType, Users, help_category
from helpers import args_change_dir, args_create, args_read, args_search, args_write
from file_system_manager import FileSystemManager

class FileSystemCli(cmd2.Cmd):
    intro = "Welcome to your in memory file system"
    prompt = '>>imfs>> '

    # TODO finish setting up logger
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.INFO)
    
    def __init__(self):
        super().__init__()
        self.manager = FileSystemManager()
        
    args_create = args_create()
    args_change_dir = args_change_dir()
    args_write = args_write()
    args_read = args_read()
    args_search = args_search()

    @cmd2.with_category(help_category)
    def do_path(self, args):
        """Returns the current directory path. Usage: path"""
        try:
            path = self.manager.get_path()
            print(path)
        except Exception as e:
            logging.info("There was a problem, check log file for more details.")
            logging.debug(e)

    @cmd2.with_category(help_category)
    def do_list_contents(self, args):
        """Returns list of files and directories in the current directory. Usage: list_contents"""
        try:
           list = self.manager.list_children()    
           print(list) 
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    @cmd2.with_category(help_category)
    @cmd2.with_argparser(args_create)
    def do_create(self, args):
        """ Create a directory  Usage: create <NAME> [include --file to create a file]"""
        try:
            if args.file:
                created = self.manager.create_file(str(args.name))
                type_created = "File"
            else:
                created = self.manager.create_directory(args.name)
                type_created = "Directory"
            if created:
                print(f"{type_created} created successfully.")
            else:
                ("Something went wrong.")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_category(help_category)
    @cmd2.with_argparser(args_change_dir)
    def do_change_dir(self, args) -> None:
        """Change the current directory. Usage: change_dir <DIRECTORY NAME>"""
        # TODO move the majority of logic out of this function
        # TODO implement search and add ability to move to a different directory
        try:
            # If the directory name is in the current directory's list of children
            if args.dir_name in self.manager.current_directory.children.keys():
                target_node = self.manager.current_directory.children[args.dir_name]
                # if the target node is a file, it can not be the current directory
                if target_node.type != str(NodeType.FILE):
                    print(f"{args.dir_name} is a file, not a directory.")
                    return
                # Update the current directory to the child
                self.manager.update_to_child(args.dir_name)
                return
            # If the directory name is the parent
            elif args.dir_name == self.manager.current_directory.parent:
                    # Update to the parent directory
                    self.manager.update_to_parent()
                    return
            # move to parent directory
            elif self.manager.current_path == self.manager.file_system.root:
                print("Already at root directory.")
                return
            else:
                print(f"{args.dir_name} is not a parent or child of the current working directory")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_category(help_category)
    @cmd2.with_argparser(args_write)
    def do_write(self, args):
        """Write content to a file. Usage: write <file_name> <content>"""
        try:
            fileNode = self.manager.write(args.name, args.content)
            print(f"Content written to {args.name}")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_category(help_category)
    @cmd2.with_argparser(args_read)
    def do_read(self, args):
        """Read the content of a file. Usage: read <file_name>"""
        try:
            content_to_read = self.manager.read(args.name)
            print(content_to_read) # TODO enhance output
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_category(help_category)
    @cmd2.with_argparser(args_search)
    def do_search(self, args):
        """Search for a file or directory. Usage: search <search_term>"""
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
            print(e)

    #WIP to switch user to different user with different permissions
    @cmd2.with_category(help_category)
    def switch(self, args):
        try:
            print(self.manager.user)
            if args.user in Users.keys():
                self.manager.user = Users[args.user]
                print(self.manager.user)
            else:
                print("Currently the only users are Lisa, Bart, Marge, and Homer")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)
    
    
if __name__ == "__main__":
    FileSystemCli().cmdloop()    