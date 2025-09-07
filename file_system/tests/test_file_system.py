import pytest
from file_system.file_system.file_system import FileSystem

def setup_function(function):
    print("setting up", function)

def test_do_path(capsys):
    fs = FileSystem()
    # initial path should be root
    expected_path = "['/']\n"
    fs.do_path()
    output = capsys.readouterr()
    assert output.out == expected_path
    #TODO test more complex paths

def test_do_list(capsys):
    fs = FileSystem()
    expected_list = "dict_keys([])\n"
    fs.do_list()
    output = capsys.readouterr()
    assert output.out == expected_list

def test_do_create_dir(capsys):
    fs = FileSystem()
    fs.do_create_dir(name="testDir")
    output = capsys.readouterr()
    assert output.out == "Directory created\n"

    fs.do_list()
    output = capsys.readouterr()
    assert output.out == "dict_keys(['testDir'])\n"
    
    # fs.do_create(name="testFile", file=True)
    # output = capsys.readouterr()
    # assert output.out == "File created\n"
    
    # fs.do_list()
    # output = capsys.readouterr()
    # assert output.out == "dict_keys(['testDir', 'testFile'])\n"

def test_do_create_file(capsys):
    #TODO check object for isFile not just print output
    fs = FileSystem()
    fs.do_create_file(name="testFile")
    output = capsys.readouterr()
    assert output.out == "File created\n"

def test_do_write(capsys):
    fs = FileSystem()
    file ="testFile"
    fs.do_create_file(name=file)
    capsys.readouterr() # clear output
    fs.do_write("testFile This is test content")
    output = capsys.readouterr()
    assert output.out == (f"Content written to {file}\n")

def do_read(capsys):
    fs = FileSystem()
    file ="testFile"
    fs.do_create_file(name=file)
    capsys.readouterr() # clear output
    fs.do_write("testFile This is test content")
    capsys.readouterr() # clear output      
    fs.do_read(file)
    output = capsys.readouterr()
    assert output.out == "This is test content\n"