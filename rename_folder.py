#Write an automation script to rename the folder, user will run the program, it will ask for folder name, anywhere placed in the directory, and then rename it according to user provided folder name.

import os

def rename_folder():
    current_name = input("Enter the name of the folder you want to rename: ")
    new_name = input("Enter the new folder name: ")

    # Search for the folder in the current directory
    if os.path.exists(current_name) and os.path.isdir(current_name):
        os.rename(current_name, new_name)
        print(f"Folder renamed successfully: '{current_name}' → '{new_name}'")
    else:
        print(f"Error: Folder '{current_name}' not found in the current directory!")

if __name__ == "__main__":
    rename_folder()
