import os
import shutil
from os import listdir


def create_empty_dir(directory: str):
    if not os.path.exists(directory):
        os.mkdir(directory)


def copy_file(input_dir: str, output_dir: str, filename: str):
    in_filename = input_dir + "/" + filename
    input_file = open(in_filename).read()
    out_filename = output_dir + '/' + filename
    output_file = open(out_filename, 'w')
    output_file.write(input_file)
    output_file.close()
    print("Copied file: " + in_filename + " to: " + out_filename)


def clear_dir(directory: str):
    for filename in listdir(directory):
        full_path = directory + '/' + filename
        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
