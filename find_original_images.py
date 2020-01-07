"""Find the original pictures so we can re-compress them for web use."""

import os
import shutil

source_base_dir = "/home/daxm/Pictures/Woodworking"
dest_dir = "/home/daxm/PycharmProjects/woodworkingwiki/content/docs/images"


def search_files(directory='.', filename=''):
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if name == filename:
                shutil.copyfile(os.path.join(dirpath, name), os.path.join(dest_dir, name))
                print(os.path.join(dirpath, name))


for bad_image in os.listdir(dest_dir):
    search_files(directory=source_base_dir, filename=bad_image)
