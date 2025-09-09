import pytest
from file_system.file_system.constants import NodeType
from file_system.file_system.file_system_manager import FileSystemManager

@pytest.fixture()
def file_system_manager():
    fsm = FileSystemManager()
    yield fsm

def test_get_path(file_system_manager):
    # initial path should be root
    expected_path = "/"
    actual_path = file_system_manager.get_path()
    assert actual_path == expected_path
    #TODO test more complex paths

def test_list_children(file_system_manager):
    expected_list = []
    actual_list = file_system_manager.list_children()
    assert actual_list == expected_list
    #TODO test more complex paths

def test_create_directory_by_default(file_system_manager):
    name = "testy"
    expected_type: NodeType = NodeType.DIRECTORY
    actual_node = file_system_manager.create_directory(name)
    assert actual_node.name == name
    assert actual_node.type.value == expected_type.value

def test_create_file(file_system_manager):
    name = "testy_file"
    expected_type: NodeType = NodeType.FILE
    actual_node = file_system_manager.create_file(name)
    assert actual_node.name == name
    assert actual_node.type.value == expected_type.value

def test_write(file_system_manager):
    expected_file_name ="testFile"
    content_to_add="word word words"
    expected_content=["word word words"]
    file_node = file_system_manager.create_file(expected_file_name)
    updated_node = file_system_manager.write(file=file_node.name, content=content_to_add)
    # TODO figure out why __dict__ is necessary//check code for other issues
    assert expected_content == updated_node.__dict__['content']
    assert expected_file_name == updated_node.__dict__['name']

def test_read(file_system_manager):
    expected_file ="testFile"
    content_1="word word words"
    content_2="evenmorewords"
    expected_content_1=[content_1]
    expected_content_2=[content_1, content_2]

    inital_file = file_system_manager.create_file(expected_file)
    updated_file = file_system_manager.write(inital_file.name, content_1)
    assert file_system_manager.read(updated_file.name) == expected_content_1
    assert updated_file.__dict__['content'] == expected_content_1

    updated_file_2 = file_system_manager.write(expected_file, content_2)
    assert file_system_manager.read(updated_file_2.name) == expected_content_2
    assert updated_file_2.__dict__['content'] == expected_content_2