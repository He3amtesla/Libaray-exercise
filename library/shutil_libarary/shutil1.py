import shutil
import os

with open('source_file.txt', 'w') as f:
    f = f.write("hesam yesss")

shutil.copy("source_file.txt", "./source.txt")