import os

from tqdm import tqdm

with open(os.environ["SOURCE_FILE_TXT"], "wt") as input_file_descriptor:
    with open(os.environ["OUTPUT_FILE_TXT"], "wt") as output_file_descriptor:
        for line in tqdm(input_file_descriptor.readlines()):
            output_file_descriptor.write(f"{line}\n")
