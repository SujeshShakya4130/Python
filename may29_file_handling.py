with open("ASSIGNMENT/assignment.txt", "r") as file:
    content = file.read()
    print(content)


with open("ASSIGNMENT/assignment.txt", "a") as file:
    file.write("new appended line\n")


import os

cwd = os.getcwd()
print("Current working dictionary:", cwd)

file_name = "ASSIGNMENT/assignment.txt"
absolute_path = os.path.abspath(file_name)
print("Absolute file path:", absolute_path)

file_path = "ASSIGNMENT/assignment.txt"

# Get the file name
file_name = os.path.basename(file_path)

# Get the size of a file
question1 = input("Do you want to know the File name and its size? (Yes/No): ")
if question1.lower() == "yes":
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print(F"File Name: {file_name} and File Size: {file_size} byte")


# Get the extension
extention = os.path.splitext(file_path)[1]
print(extention)


user = input("Do want to delete the file? (Yes/No): ")
if user.lower() == "Yes":
    os.remove("ASSIGNMENT/assignment.txt")
    print("file has been removed successfully")
else:
    print("File Not Deleted")


user2 = input("D0 you want to close the file? (Yes/No):")
if user2.lower() == "yes":
    file.close()
    print("Thank You")
