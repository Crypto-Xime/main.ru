import os
import time

print("Current Directory: ", os.getcwd())

def traverse_directory(directory: str):
    """
    Traverse the specified directory and print details about each file.

    :param directory: The directory to traverse.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)  # Form the full file path
            filetime = os.path.getmtime(filepath)  # Get the last modification time
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Format the modification time
            filesize = os.path.getsize(filepath)  # Get the file size
            parent_dir = os.path.dirname(filepath)  # Get the parent directory

            print(f'File found: {file}, Path: {filepath}, Size: {filesize} bytes, '
                  f'Modified time: {formatted_time}, Parent directory: {parent_dir}')

# Specify the directory to traverse (parent folder of your file)
directory = r"C:\PythonProject1UNI\PythonProject1\Mami_Excel"
traverse_directory(directory)




