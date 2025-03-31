"""Write an automation script to rename the folder, user will run the program, 
it will ask for folder name, anywhere placed in the directory, and then rename it
 according to user provided folder name."""
import os
import os

old_folder = "AMAN HW"
new_folder = "new_folder_name"
if os.path.exists(old_folder):
    os.rename(old_folder, new_folder)
    print(f"Folder renamed from '{old_folder}' to '{new_folder}'")
else:
    print(f"Error: The folder '{old_folder}' does not exist.")


