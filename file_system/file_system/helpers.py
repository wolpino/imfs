import cmd2

""" Arg parsers"""
def args_create():
    ap_create = cmd2.Cmd2ArgumentParser()
    ap_create.add_argument('name', type=str, help= "The name of the new directory or file.")
    ap_create.add_argument('-f', '--file', action='store_true', help="Add --file to create a file")
    return ap_create

def args_change_dir():
    ap_change = cmd2.Cmd2ArgumentParser()
    ap_change.add_argument('dir_name', type=str, help= "Directory to move to")
    return ap_change

def args_read():
    ap_read = cmd2.Cmd2ArgumentParser()
    ap_read.add_argument
    return ap_read

def args_write():
    ap_write = cmd2.Cmd2ArgumentParser()
    ap_write.add_argument('name', type=str, help= "File to write to")
    ap_write.add_argument('content', type=str, help="Content to add to file")
    return ap_write

def args_search():
    ap_search = cmd2.Cmd2ArgumentParser()
    ap_search.add_argument('search_term', type=str, help= "Name of file/directory you'd like to search for")
    return ap_search

def args_switch_user():
    ap_switch = cmd2.Cmd2ArgumentParser()
    ap_switch.add_argument('user', type=str, choices=["Lisa","Bart","Marge","Homer"], help="Switch to a new user by choosing from the choices")
    return ap_switch