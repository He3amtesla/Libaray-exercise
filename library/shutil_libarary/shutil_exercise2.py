import os
import shutil

os.makedirs("./move_test", exist_ok = False)

with open("move_test/move_me.txt", "w") as f:
    f.write("help mia")

os.makedirs("./moved_here")

shutil.move("./move_test/move_me.txt", "./moved_here")