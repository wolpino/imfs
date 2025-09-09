# In Memory File System
a cli app to create an in memory file system with basic actions


**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)

## Installation
Pre install requirements: `Python3` and `pip`

On macOS from the base `file_system` folder (where the `.toml` file is located)

```sh
$ pip install -e .
```

## Execution

To run the In Memory File System:

from the `imfs/file_system/file_system` folder, (where the `file_system_cli.py` file is located) run the following command:

```sh
$ python3 file_system_cli.py
```

To run tests 

from the `imfs/file_system/tests` folder

```sh
$ pytest
```


## Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Functionality

`change_dir <directory_to_change_to>`

`create <name>` (include optional  `--file` to make a file instead of directory)  

`list`  will return list of files and directories of current directory

`path`  will list the path of the current directory

`read <file_name>` will return file content

`search <search_term>` search for all files and directories with a certain term

`write <file_to_write_to>` add content to a file 

`help` get help

## Future functionality (partially implemented):

- switch change user (this works, but without permissions it doesn't do anything)

- set permission on files and directories (this is close, I think I need to get rid of my enum and write some tests)

- walk through file_system and find first file at specific depth 
