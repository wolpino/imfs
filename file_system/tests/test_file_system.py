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

def test_do_create(capsys):
    fs = FileSystem()
    fs.do_create(name="testDir")
    output = capsys.readouterr()
    assert output.out == "Directory created\n"

    fs.do_list()
    output = capsys.readouterr()
    assert output.out == "dict_keys(['testDir'])\n"
    
    fs.do_create(name="testFile", file=True)
    output = capsys.readouterr()
    assert output.out == "File created\n"
    
    fs.do_list()
    output = capsys.readouterr()
    assert output.out == "dict_keys(['testDir', 'testFile'])\n"
