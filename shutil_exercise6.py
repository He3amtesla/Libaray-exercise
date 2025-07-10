import shutil


print(".")
disk = shutil.disk_usage(".")
print(f"""
      Disk Free:{disk.free}
      Disk total:{disk.total}
      Disk used :{disk.used}
      """
)
print("----")
print("/")
disk = shutil.disk_usage("/")
print(f"""
      Disk Free:{disk.free}
      Disk total:{disk.total}
      Disk used :{disk.used}
      """
)