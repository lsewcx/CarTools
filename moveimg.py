import os
import shutil

# 定义源文件夹、XML文件夹和目标文件夹
source_dir = r'C:\Users\lsewcx\Desktop\2024AI模型\DatasetVocSASU_ForIcarM2023\DatasetVocSASU_ForIcarM2023\Images/'
xml_dir = r'C:\Users\lsewcx\Desktop\2024AI模型\bridge\xml/'
target_dir = r'C:\Users\lsewcx\Desktop\2024AI模型\bridge\img/'

# 获取XML文件夹中所有XML文件的文件名（不包括扩展名）
xml_files = [os.path.splitext(f)[0] for f in os.listdir(xml_dir) if f.endswith('.xml')]

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_dir):
    # 如果文件名（不包括扩展名）在XML文件名列表中
    if os.path.splitext(filename)[0] in xml_files:
        # 检查目标文件夹中是否已经存在该文件
        if not os.path.exists(target_dir + filename):
            # 移动文件
            shutil.move(source_dir + filename, target_dir + filename)