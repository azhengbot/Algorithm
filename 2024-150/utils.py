import os

# 获取当前目录
current_dir = os.getcwd()

# 列出当前目录下的文件和文件夹
files = [
    f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))
]

# 输出文件个数
print(f"当前目录下文件个数: {len(files)}")
