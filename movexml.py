import os
import xml.etree.ElementTree as ET
import shutil

# 定义XML文件的目录和目标目录
xml_dir = r'C:\Users\lsewcx\Desktop\2024AI模型\DatasetVocSASU_ForIcarM2023\DatasetVocSASU_ForIcarM2023\Annotations/'
target_dir = r'C:\Users\lsewcx\Desktop\2024AI模型\bridge\xml/'

# 遍历文件夹中的所有文件
for filename in os.listdir(xml_dir):
    # 如果文件是一个XML文件
    if filename.endswith('.xml'):
        # 解析XML文件
        tree = ET.parse(xml_dir + filename)
        root = tree.getroot()

        # 找到所有的 <name> 标签
        for name in root.iter('name'):
            # 如果当前的名字是 "bridge"，则移动文件
            if name.text == 'bridge':
                # 检查目标文件夹中是否已经存在该文件
                if not os.path.exists(target_dir + filename):
                    # 移动文件
                    shutil.move(xml_dir + filename, target_dir + filename)