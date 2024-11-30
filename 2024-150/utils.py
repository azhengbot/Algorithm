import os

# 获取当前目录
current_file_path = os.path.abspath(__file__)

# 获取当前脚本文件所在的文件夹
current_dir = os.path.dirname(current_file_path)
# 列出当前目录下的文件和文件夹
print(current_dir)
files = [
    f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))
]
print(files)
# 输出文件个数
print(f"当前目录下文件个数: {len(files)}")
