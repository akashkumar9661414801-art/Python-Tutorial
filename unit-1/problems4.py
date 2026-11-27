
import os

# Specify the directory path
path = "/New Folder"

# Print the contents of the directory
contents = os.listdir(path)

for item in contents:
    print(item)
