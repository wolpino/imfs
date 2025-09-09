import argparse
import logging
import cmd2
from file_system_manager import FileSystemManager

class FileSystemCli(cmd2.Cmd):
    logger = logging.Logger
    
    def __init__(self):
        super().__init__()
        self.manager = FileSystemManager()

    print("Welcome to your in memory file system")
    print("Welcome to a simple in-memory file system. Enter 'help' for avail commmands")
    
    create_argparser = cmd2.Cmd2ArgumentParser()
    create_argparser.add_argument('name', type=str, help= "the new directory or file name")
    create_argparser.add_argument('-f', '--file', action='store_true', help="add file to create a file")

    write_argparser = cmd2.Cmd2ArgumentParser()
    write_argparser.add_argument('name', type=str, help= "file name to write to")
    write_argparser.add_argument('content', type=str, help="content to add file")

    read_argparser = cmd2.Cmd2ArgumentParser()
    read_argparser.add_argument('name', type=str, help= "name of file you want to read")

    search_write_argparser = cmd2.Cmd2ArgumentParser()
    search_write_argparser.add_argument('search_term', type=str, help= "file name you'd like to search for")


    def do_path(self, args):
        """Returns the current directory path"""
        try:
            path = self.manager.get_path()
            print(path)
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    def do_list(self, args):
        """List files and directories in the current directory."""
        try:
           list = self.manager.list_children()    
           print(list) 
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")

    @cmd2.with_argparser(create_argparser)
    def do_create(self, args):
        """ create a file or directory create <name> (creates directory by default add -f to create a file)"""
        print(args)
        print(args.file)
        print(str(args.name))
        try:
            if args.file:
                created = self.manager.create_file(str(args.name))
                print("created!")
            else:
                created = self.manager.create_directory(args.name)
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_argparser(write_argparser)
    def do_write(self, args):
        """Write content to a file. Usage: write <file_name> <content>"""
        try:
            fileNode = self.manager.write(args.name, args.content)
            print(f"Content written to {args.name}")
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_argparser(read_argparser)
    def do_read(self, args):
        """Read the content of a file. Usage: read <file_name>"""
        try:
            content_to_read = self.manager.read(args.name)
            print(content_to_read) # TODO enhance output
        except Exception as e:
            # TODO add more specific exception excepts to give a better error message
            print(f"oopsie")
            print(e)

    @cmd2.with_argparser(search_write_argparser)
    def do_search(self, args):
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
            print(e)
        
    
if __name__ == "__main__":
    FileSystemCli().cmdloop()    