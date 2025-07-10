import os
import shutil

os.makedirs("./tree_test")
n=0

while(n<2):
    with open(f"./tree_test/{n}.text", 'w') as file:
        file.write("anything")
    n+=1

shutil.copytree("./tree_test", "./tree_test_copy")