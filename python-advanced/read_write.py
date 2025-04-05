"""Scripts to read the files with different system"""
import csv
import json
# normal file reading 
# open() -  opens file with the defined permission 
# read() - reads the file with specifed permission as 'r' - default mode in the python read write oprations
# close() - cleans up the workspace by closing the file
# readlines() - line by line file reading

# file = open("/Users/abhigyan709/git-live/python-advanced/student.txt", 'r')

# content = file.read()

# print(content)
# file.close()

# next we will use the readlines() - one by one reading of the file

# file = open("/Users/abhigyan709/git-live/python-advanced/student.txt", 'r')
# lines = file.readlines()

# for line in lines:
#     print(line, end=' ')

# file.close()

# file = open("/Users/abhigyan709/git-live/python-advanced/student.txt", 'w')
# file.write("This is abhigyan, and i am 25 years old.\n")
# file.write("I am a DevOps Engineer\n")
# file.close()

# file = open("/Users/abhigyan709/git-live/python-advanced/student.txt", 'a')
# file.write("I live in Delhi\n")
# file.write("I am a DevOps Trainer as well\n")
# file.close()

# read file in a binary mode.
# file = open("/Users/abhigyan709/git-live/python-advanced/student.txt", 'rb')
# content = file.read()
# print(content)
# file.close()

# import csv
# with open("/Users/abhigyan709/git-live/python-advanced/demo.csv") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
    
#     for line in csvreader:
#          print(line, type(line))

# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]

# with open("/Users/abhigyan709/git-live/python-advanced/demo2.csv", 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(data)

# print("CSV file created successfully.")

data = [
    {
        "Name": "Alice",
        "Age": 30,
        "City": "New"
    },
    {
        "Name": "Bob",
        "Age": 25,
        "City": "Los Angeles"
    },
    {
        "Name": "Charlie",
        "Age": 35,
        "City": "Chicago"
    }
]

with open("/Users/abhigyan709/git-live/python-advanced/demo3.csv", 'w') as csvfile:
    filename = ["Name", "Age", "City"]

    write_csv = csv.DictWriter(csvfile, fieldnames=filename)
    write_csv.writeheader()
    write_csv.writerows(data)
    print("CSV file created successfully.")

