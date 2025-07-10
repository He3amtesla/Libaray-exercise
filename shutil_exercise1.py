import os
import shutil

os.makedirs("./test_dir", exist_ok=True)
with open("./test_dir/hello.txt","w") as f:
    f.write("salam")

shutil.copy("./test_dir/hello.txt", "./test_dir/hello_copy.txt")