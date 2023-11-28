import os
import sys

def read_files(directory_path, file_extension):
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory not found:", directory_path)

    if not file_extension.startswith("."):
        raise Exception("File extension should start with '.'")

    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory_path, filename)

            try:
                content = open(file_path, 'r').read()
                print("Contents of", filename, ": ", content)
            except Exception as e:
                print("Error reading file", filename, ":", e)



if len(sys.argv) != 3:
    #lines = [line.strip() for line in open(file_path, 'r').readlines()]
    print("Usage: python script.py <directory_path> <file_extension>")
else:

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_files(directory_path, file_extension)



