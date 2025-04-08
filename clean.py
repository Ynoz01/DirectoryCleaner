import os
import shutil
import sys

#

def move_file(file_path, old_path, file):
    file_type = str(file).split(".")[len(str(file).split("."))-1]
    new_path = old_path + "/" + file_type
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    shutil.move(file_path, new_path)


def clean(path) -> None:
    directory = os.listdir(path)
    print(directory)
    for file in directory:
        file_path = os.fspath(path + "/" + file)
        if os.path.isfile(file_path):
            move_file(file_path, path, file)
            

def main():
    clean(sys.argv[1])
    path = os.fspath(sys.argv[1])


if __name__ == "__main__":
    main()
