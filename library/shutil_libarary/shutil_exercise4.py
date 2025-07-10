import shutil
import os
import time

os.makedirs ("delete_me")
n=0

while(n<2):
    with open(f"delete_me/{n}.text", 'w') as f:
        f.write("sdf")
    n+=1
time.sleep(4)
shutil.rmtree("delete_me")