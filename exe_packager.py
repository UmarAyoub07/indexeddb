```python
import os
import shutil
import zipfile

def create_package(exe_list, package_name):
    with zipfile.ZipFile(package_name, 'w') as zipf:
        for exe in exe_list:
            zipf.write(exe)

def main():
    exe_list = ["file1.exe", "file2.exe", "file3.exe"]  # Add your exe file names here
    package_name = "package.zip"  # Name of the output package file
    create_package(exe_list, package_name)

if __name__ == "__main__":
    main()
```