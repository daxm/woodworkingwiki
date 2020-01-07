import tinify
import os

tinify.key = "3NdxKltc9RKNQ4QKMqL769nN9KxxVbLj"
source_dir = os.path.join(os.getcwd(), "content", "docs", "images")
dest_dir = os.path.join(os.getcwd(), "content", "docs", "dest_images")
max_width = 1024
max_height = 768
max_compressions = 490

"""
# https://tinypng.com/developers/reference/python

# Example 1
source = tinify.from_file("blah.jpg")
source.to_file("blah2.jpg")

# Example 2
with open("asdf", "rb") as source:
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_buffer()

# Resize Image
source = tinify.from_file("large.jpg")
resized = source.resize(
    method="fit",
    width=150,
    height=100
)
resized.to_file("thumbnail.jpg")

# Method "fit" requires max width/height and will size all images to bound to that size.

# Get compression count for this month
compressions_this_month = tinify.compression_count
"""

compression_count = tinify.compression_count
if compression_count is None:
    compression_count = 0

for image in os.listdir(source_dir):
    source_filename = os.path.join(source_dir, image)
    dest_filename = os.path.join(dest_dir, image)
    compression_count = tinify.compression_count
    if max_compressions > compression_count:
        print(f"Processing {compression_count} of {max_compressions} compressions: "
              f"{source_filename} --> {dest_filename}")
        source = tinify.from_file(source_filename)
        resized = source.resize(
            method="fit",
            width=max_width,
            height=max_height
        )
        source.to_file(dest_filename)
