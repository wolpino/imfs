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
    actual_node = file_system_manager.create(name)
    assert actual_node.name == name
    assert actual_node.type.value == expected_type.value

def test_create_file(file_system_manager):
    name = "testy_file"
    actual_node = file_system_manager.create(name, NodeType.FILE, file_system_manager.current_directory)
    assert actual_node.name == name
    assert actual_node.type == NodeType.FILE


def test_write(file_system_manager):
    expected_file_name ="testFile"
    expected_content="word word words"
    
    file = file_system_manager.create(expected_file_name, NodeType.FILE, file_system_manager.current_directory)
    actual_file = file_system_manager.write(file=file.name, content=expected_content)
    assert expected_content == actual_file
    assert expected_file_name == actual_file

def test_read(file_system_manager):
    expected_file ="testFile"
    expected_content_1="word word words"
    expected_content_2="evenmorewords"
    expected_content=[expected_content_1, expected_content_2]

    inital_file = file_system_manager.create(expected_file, NodeType.FILE, file_system_manager.current_directory)
    updated_file = file_system_manager.write(inital_file.name, expected_content_1)
    
    assert file_system_manager.read(updated_file.name) == [expected_content_1]
    assert updated_file.content == [expected_content_1]

    updated_file_2 = file_system_manager.write(expected_file, expected_content_2)
    assert file_system_manager.read(updated_file_2) == [expected_content_1]
    assert updated_file_2.content == expected_content