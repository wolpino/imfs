import pytest
from file_system.file_system.constants import NodeType
from file_system.file_system.file_system_manager import FileSystemManager
from file_system.file_system.models import Node

def setup_function(function):
    print("setting up", function)


def _tree_to_search(fs: FileSystemManager):
    fs.create_directory(name="testDir_1")
    fs.create_directory(name="testDir_4")
    fs.create_directory(name="testDir_5")
    fs.create_directory(name="testDir_6")
    fs.create_directory("testDir_1")
    fs.create_directory(name="testDir_2")
    fs.create_file("testy2")
    fs.create_file("testy")
    fs.update_to_child("testDir_2")
    fs.create_file("secrets")
    fs.update_to_parent()
    fs.create_directory(name="testDir_3")
    fs.update_to_child("testDir_3")
    fs.create_directory("mystery")
    fs.update_to_parent()
    fs.create_file("mystery")
    return fs


# def test_tree_to_search():
#     fsm = FileSystemManager()
#     _tree_to_search(fsm)
#     expected = ["stuff"]
#     assert fsm.__dict__ == expected



def test_get_path():
    fsm = FileSystemManager()
    # initial path should be root
    expected_path = "/"
    actual_path = fsm.get_path()
    assert actual_path == expected_path
    #TODO test more complex paths



def test_list_children():
    fsm = FileSystemManager()
    expected_list = []
    actual_list = fsm.list_children()
    assert actual_list == expected_list
    #TODO test more complex paths


def test_create_directory():
    fsm = FileSystemManager()
    name = "testy"
    actual_node = fsm.create_directory(name)
    assert actual_node.name == name

def test_update_to_child():
    fsm = FileSystemManager()
    name = "testy_file"
    actual_node = fsm.create_directory(name)
    assert fsm.current_directory.name == "/"
    assert actual_node.name == name
    fsm.update_to_child(actual_node.name)
    assert fsm.current_directory.name == actual_node.name

def test_update_to_parent():
    fsm = FileSystemManager()
    root_node = fsm.file_system.root
    name = "testy_file"
    actual_node = fsm.create_directory(name)
    assert fsm.current_directory.name == "/"
    assert actual_node.name == name
    fsm.update_to_child(actual_node.name)
    assert fsm.current_directory.name == actual_node.name
    fsm.update_to_parent() 
    assert fsm.current_directory.name == root_node.name


def test_create_file():
    fsm = FileSystemManager()
    name = "testy_file"
    actual_node = fsm.create_file(name)
    assert actual_node.name == name

def test_write():
    fsm = FileSystemManager()
    expected_file_name ="testFile"
    expected_content="word word words"
    file = fsm.create_file(name=expected_file_name)
    fsm.write(file=file, content=expected_content)
    assert expected_content == file.content
    assert expected_file_name == file.name

def test_read_file():
    fsm = FileSystemManager()
    expected_file ="testFile"
    expected_content_1="word word words"
    expected_content_2="evenmorewords"
    expected_content=[expected_content_1, expected_content_2]
    inital_file = fsm.create_file(expected_file)
    updated_file = fsm.write(inital_file.name, expected_content_1)
    assert fsm.read(updated_file.name) == [expected_content_1]
    assert updated_file.content == [expected_content_1]
    updated_file_2 = fsm.write(expected_file, expected_content_2)
    assert fsm.read(updated_file_2) == [expected_content_1]
    assert updated_file_2.content == expected_content


def test_do_search(capsys):
    fsm = FileSystemManager()
    _tree_to_search(fsm)
    expected = "/testDir_1/testDir_2/secrets"
    fsm.search("secret") 
    output = capsys.readouterr()
    assert output.out == expected
