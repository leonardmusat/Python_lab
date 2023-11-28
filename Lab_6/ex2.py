import os
import sys

def change_name(directory_path):
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory not found:", directory_path)
    count = 1

    for filename in os.listdir(directory_path):
        old_path = os.path.join(directory_path, filename)
        string = "file"
        string = string + str(count)
        new_path = os.path.join(directory_path, string)

        if os.path.exists(directory_path + filename):
            raise Exception ("File already exists.")

        os.rename(old_path, new_path)
        count += 1



if len(sys.argv) != 2:
    print("Usage: python script.py <directory_path> <file_extension>")
else:

    directory_path = sys.argv[1]

    change_name(directory_path)
