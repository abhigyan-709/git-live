import os

def create_folder(folder):
    while True:
        try:
            os.mkdir(folder)
            print(f"Folder '{folder}' has been created successfully.")
            break  # Exit the loop once the folder is created
        except FileExistsError:
            print(f"Error: The folder '{folder}' already exists. Please enter a different name.")
            folder = input("Enter a new folder name: ")  # Ask for a new name

def main():
    folder_name = input("Please enter the folder name: ")
    create_folder(folder_name)

if __name__ == "__main__":
    main()
