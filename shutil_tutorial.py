import shutil
import os
from loguru import logger

# تنظیم لاگر
logger.add("shutil_exercises.log", rotation="1 MB")

def create_sample_files():
    """ایجاد فایل‌های نمونه برای تمرین"""
    # ایجاد دایرکتوری تمرین
    os.makedirs('exercise_folder', exist_ok=True)
    os.makedirs('exercise_folder/subfolder', exist_ok=True)
    
    # ایجاد فایل‌های نمونه
    files = [
        ('exercise_folder/file1.txt', 'محتوای فایل اول'),
        ('exercise_folder/file2.txt', 'محتوای فایل دوم'),
        ('exercise_folder/subfolder/file3.txt', 'محتوای فایل سوم'),
    ]
    
    for file_path, content in files:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    logger.info("فایل‌های نمونه ایجاد شدند")

def demonstrate_shutil_functions():
    """نمایش توابع مختلف shutil"""
    
    print("=== آموزش کتابخانه shutil ===\n")
    
    # 1. shutil.copy() - کپی کردن فایل
    print("1. shutil.copy() - کپی کردن فایل")
    print("   shutil.copy('source', 'destination')")
    print("   مثال: shutil.copy('file1.txt', 'file1_copy.txt')\n")
    
    # 2. shutil.copy2() - کپی کردن فایل با حفظ metadata
    print("2. shutil.copy2() - کپی کردن فایل با حفظ metadata")
    print("   shutil.copy2('source', 'destination')")
    print("   مثال: shutil.copy2('file1.txt', 'file1_copy2.txt')\n")
    
    # 3. shutil.copytree() - کپی کردن دایرکتوری
    print("3. shutil.copytree() - کپی کردن دایرکتوری")
    print("   shutil.copytree('source_dir', 'destination_dir')")
    print("   مثال: shutil.copytree('exercise_folder', 'exercise_folder_copy')\n")
    
    # 4. shutil.move() - انتقال فایل یا دایرکتوری
    print("4. shutil.move() - انتقال فایل یا دایرکتوری")
    print("   shutil.move('source', 'destination')")
    print("   مثال: shutil.move('file1.txt', 'moved_file.txt')\n")
    
    # 5. shutil.rmtree() - حذف دایرکتوری و محتویات آن
    print("5. shutil.rmtree() - حذف دایرکتوری و محتویات آن")
    print("   shutil.rmtree('directory')")
    print("   مثال: shutil.rmtree('temp_folder')\n")

def run_examples():
    """اجرای مثال‌های عملی"""
    logger.info("شروع اجرای مثال‌ها")
    
    # ایجاد فایل‌های نمونه
    create_sample_files()
    
    # مثال 1: کپی کردن فایل
    shutil.copy('exercise_folder/file1.txt', 'exercise_folder/file1_copy.txt')
    logger.info("فایل file1.txt کپی شد")
    
    # مثال 2: کپی کردن دایرکتوری
    shutil.copytree('exercise_folder', 'exercise_folder_backup')
    logger.info("دایرکتوری exercise_folder کپی شد")
    
    # مثال 3: انتقال فایل
    shutil.move('exercise_folder/file2.txt', 'exercise_folder/moved_file2.txt')
    logger.info("فایل file2.txt انتقال یافت")
    
    print("مثال‌ها با موفقیت اجرا شدند!")
    print("فایل‌های ایجاد شده:")
    for root, dirs, files in os.walk('.'):
        if 'exercise_folder' in root:
            print(f"  {root}: {files}")

if __name__ == "__main__":
    demonstrate_shutil_functions()
    run_examples() 