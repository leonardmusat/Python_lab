import os
import sys

def sum_size(directory_path):
    sum = 0
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory not found:", directory_path)

    for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isdir(file_path):
                sum =sum + sum_size(file_path)
            else:
                sum = sum + os.path.getsize(file_path)

    return sum

if len(sys.argv) != 2:
    print("Usage: python script.py <directory_path> <file_extension>")
else:

    directory_path = sys.argv[1]

    print(sum_size(directory_path))