from __future__ import annotations
from typing import Any


DIR_MAX_ELEMS = 10
MAX_BUF_FILE_SIZE = 15
DELIMITER = '/'


class FileSystem():
    def __init__(self):
        self.root = Directory(self, path=[], name="~")
        self.cwd = self.root

    def string_to_path(self, string: str) -> list[Node]:
        pass

    def path_to_string(self, path: list[Node]) -> str:
        pass

    def get_node(self, path) -> Node:
        pass

    def create_directory(self, path: str, name: str) -> Directory:
        pass

    def create_binary_file(self, path: str, name: str, information: str) -> BinaryFile:
        pass

    def create_log_file(self, path: str, name: str, information: str = None) -> LogFile:
        pass

    def create_buffer(self, path: str, name: str) -> BufferFile:
        pass

    def print_elements(self) -> None:
        pass


class Node():
    def __init__(self, path: list[Node], name: str):
        pass

    def delete(self):
        pass

    
class Directory(Node):
    def __init__(self, fs: FileSystem, path: list[Node], name: str):
        super().__init__(path, name)
        self.childs = []
        self.fs = fs

    def __repr__(self):
        return f"<DIR | Path: {DELIMITER.join([d.name for d in self.path]) if self.path else ''}/[ {self.name} ]>"

    def move(self, filename: str, destination: str):
        pass

    def can_create_file(self, new_file_name: str) -> bool:
        if len(self.childs) == DIR_MAX_ELEMS:
            raise AttributeError(f"Directory can't contain more than {DIR_MAX_ELEMS} nodes")

        for child in self.childs:
            if child.name == new_file_name:
                raise AttributeError("File with that name already exists!")

        return True

    def create_directory(self, name: str) -> Directory:
        pass

    def create_binary_file(self, name: str, information: str) -> BinaryFile:
        pass


    def create_log_file(self, name: str, information: str = None) -> LogFile:
        pass

    def create_buffer(self, name: str) -> BufferFile:
        pass

    def print_elements(self, lvl=0) -> None:
        pass

    def string_to_path(self, string: str, path: list[Node]) -> list[Node]:
        pass

    def get_node_helper(self, path):
        pass


class BinaryFile(Node):
    def __init__(self, path: list[Node], name: str, information: str):
        super().__init__(path, name)
        self.information = information

    def read(self) -> None:
        return self.information


class LogFile(Node):
    def __init__(self, path: list[Node], name: str, information: str = None):
        super().__init__(path, name)
        self.information = information

    def read(self) -> str:
        return self.information

    def append(self, information: str) -> str:
        self.information += information


class BufferFile(Node):
    def __init__(self, path: list[Node], name: str):
        super().__init__(path, name)
        self.items = []

    def push(self, element: Any) -> bool:
        pass

    def pop(self) -> bool:
        pass
