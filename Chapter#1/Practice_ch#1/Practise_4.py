# Practise 4:
# write a python program to print the content of a directory using the os module

import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        print(f"Contents of directory '{directory}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the directory you want to list
directory_path = '.'  # '.' refers to the current directory

# Call the function
list_directory_contents(directory_path)

'''
Explanation:
1. Import the "os" module: Provides a way to interact with the operating system.
Define the list_directory_contents function:
os.listdir(directory): Lists all files and directories in the specified path.
Exception handling:
FileNotFoundError: Catches errors if the directory does not exist.
PermissionError: Handles cases where you don't have permission to access the directory.
Generic Exception: Catches any other unforeseen errors.
Specify the directory: The variable directory_path is set to '.', which refers to the current working directory. You can change this to any directory path you wish to check.
Call the function: Prints the contents of the specified directory.
You can modify directory_path to point to any directory you want to inspect. 
For example, if you want to list the contents of C:\Users\YourUsername\Documents (on Windows) or /home/yourusername/Documents (on Linux/macOS), just replace directory_path with the appropriate path.'''