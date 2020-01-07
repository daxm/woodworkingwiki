"""Find the original pictures so we can re-compress them for web use."""

import os
import shutil

source_base_dir = "/home/daxm/Pictures/Woodworking"
dest_dir = "/home/daxm/PycharmProjects/woodworkingwiki/content/docs/images"


def search_files(directory='.', filename=''):
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if name == filename:
                source_file = os.path.join(dirpath, name)
                dest_file = os.path.join(dest_dir, name)
                shutil.copyfile(source_file, dest_file)
                print(source_file, dest_file)


for bad_image in os.listdir(dest_dir):
    search_files(directory=source_base_dir, filename=bad_image)
