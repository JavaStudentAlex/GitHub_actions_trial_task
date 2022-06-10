import os

import numpy as np
import scipy as sp
import pandas as pd
from tqdm import tqdm


with open(os.environ["OUTPUT_FILE_TXT"], "wt") as file_descriptor:
    for letter in tqdm(list("Hello world")):
        file_descriptor.write(f"{letter}\n")
