class FileSystemElement:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class File(FileSystemElement):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.content = ""

    def read_content(self):
        try:
            with open(self.location + self.name, 'r') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"File '{self.name}' not found.")

    def write_content(self, data):
        try:
            with open(self.location + self.name, 'w') as file:
                file.write(data)
        except FileNotFoundError:
            print(f"File '{self.name}' not found.")

class Directory(FileSystemElement):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.contents = []

    def add_file(self, file):
        self.contents.append(file)

    def add_directory(self, directory):
        self.contents.append(directory)

    def list_contents(self):
        for element in self.contents:
            print(element.name)

# Creating a directory structure
root_directory = Directory("Root", "/")
file1 = File("file1.txt", "/root/")
file2 = File("file2.txt", "/root/")
sub_directory = Directory("Subdirectory", "/root/")

root_directory.add_file(file1)
root_directory.add_file(file2)
root_directory.add_directory(sub_directory)

# Writing content to a file
file1.write_content("Hello, world!")

# Reading content from a file
file1.read_content()
print(f"Content of {file1.name}:")
print(file1.content)

# Listing contents of a directory
print("Contents of Root directory:")
root_directory.list_contents()

""" 
In this program:

We define a base class FileSystemElement that has attributes for the name and location of the file or directory.

We create two derived classes, File and Directory, which inherit from the FileSystemElement class. The File class has methods for reading and writing file content, while the Directory class has methods for adding files and subdirectories and listing their contents.

We create instances of the File and Directory classes, organize them into a directory structure, and perform file operations such as writing and reading content from a file.

We demonstrate how to list the contents of a directory.
"""
