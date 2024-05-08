#! /usr/bin/env python3
import sys
import re
import os
from os.path import isfile
from tqdm import tqdm

# given a dir path, create two folder, one for jpg, one for raw
# assume dir have raw and jpg files only
# input: dir_path
# output: None
def sort_raw_pic(dir_path):
    #check dir_path
    if not os.path.exists(dir_path):
        print("dir_path does not exist")
        return
    
    #create two folder name jpg and raw
    jpg_path = os.path.join(dir_path, "jpg")
    raw_path = os.path.join(dir_path, "raw")
    if not os.path.exists(jpg_path):
        os.makedirs(jpg_path)
    if not os.path.exists(raw_path):
        os.makedirs(raw_path)
    
    #move files
    for file in tqdm(os.listdir(dir_path)):
        if not isfile(os.path.join(dir_path, file)):
            continue
        if re.search(r'.*\.JPG$', file):
            os.rename(os.path.join(dir_path, file), os.path.join(jpg_path, file))
        elif re.search(r'.*\.ARW$', file):
            os.rename(os.path.join(dir_path, file), os.path.join(raw_path, file))
        else:
            print(f"{file} file in {dir_path} is not jpg or raw, ignore")
            continue
    # print("sort done")
    return

# sort raw pic in a list of directories
def sort_raw_pic_list(dirs):
    for dir in dirs:
        sort_raw_pic(dir)
        print(f"sorted folder: {dir}")
    return

# sort raw pic in all directories in a folder
# input: folder
def sort_raw_pic_all_dir(dir):
    dirs = [os.path.join(dir, d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
    sort_raw_pic_list(dirs)
    return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_raw_pic.py dir_path")
        sys.exit(1)
    # sort_raw_pic(sys.argv[1])
    sort_raw_pic_all_dir(sys.argv[1])
    sys.exit(0)