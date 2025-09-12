from cmd2 import CommandResult
import cmd2_ext_test
import pytest

from file_system.file_system.file_system_cli import FileSystemCli

class FileSystemCliTester(cmd2_ext_test.ExternalTestMixin, FileSystemCli):
    #TODO add more edge case testing
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

@pytest.fixture
def test_cli():
    app = FileSystemCliTester()
    app.fixture_setup()
    yield app
    app.fixture_teardown()

def test_do_path(test_cli):
    expected_path = "/"

    out = test_cli.app_cmd("path")
    
    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == expected_path

def test_do_path_complex(test_cli):
    expected_path = "/stuff/another_one"
    test_cli.app_cmd("create documents")
    test_cli.app_cmd("create_dir stuff")
    test_cli.app_cmd("create morestuff")
    test_cli.app_cmd("change_dir stuff")
    test_cli.app_cmd("create anotherone")
    test_cli.app_cmd("change_dir another_one")

    out = test_cli.app_cmd("path")

    # validate the command output
    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == expected_path



def test_do_list_contents(test_cli):
    expected_initial_contents = "[]"
    
    out = test_cli.app_cmd("list_contents")
    
    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == expected_initial_contents


# TODO test with a name with spaces
# TODO test a name that already exists
def test_do_create_default(test_cli):
    expected_response = "Directory stuff created successfully."
    
    out = test_cli.app_cmd("create stuff")

    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == expected_response

def test_do_create_file(test_cli):
    expected_response = "File notes created successfully."
    
    out = test_cli.app_cmd("create notes --file")

    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == expected_response

# def test_do_write(test_cli):
#     expected_response = "Content written to notes."
    
#     test_cli.app_cmd("create notes --file")
#     out = test_cli.app_cmd("write blahblahblah")
    
#     # validate the command output and result data
#     assert isinstance(out, CommandResult)
#     assert str(out.stdout).strip() == expected_response
#     assert out.data == "a node"

# # def test_do_read(test_cli):
# #     expected_read_response = ""
    
# #     out = test_cli.app_cmd("read")
    
# #     # validate the command output and result data
# #     assert isinstance(out, CommandResult)
# #     assert str(out.stdout).strip() == expected_read_response

# # def test_do_search(test_cli):
# #     expected_search_response = "[]"
    
# #     out = test_cli.app_cmd("search")
    
# #     # validate the command output and result data
# #     assert isinstance(out, CommandResult)
# #     assert str(out.stdout).strip() == expected_search_response

# # def test_do_switch(test_cli):
# #     expected_switch_response = ""
    
# #     out = test_cli.app_cmd("switch")
    
# #     # validate the command output and result data
# #     assert isinstance(out, CommandResult)
# #     assert str(out.stdout).strip() == expected_switch_response
