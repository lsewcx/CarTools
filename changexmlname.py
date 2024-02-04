import os
import xml.etree.ElementTree as ET

# 定义XML文件的目录
xml_dir = 'C:/Users/lsewcx/Desktop/2024AI模型/crosswalk/xml/'

# 遍历文件夹中的所有文件
for filename in os.listdir(xml_dir):
    # 如果文件是一个XML文件
    if filename.endswith('.xml'):
        # 解析XML文件
        tree = ET.parse(xml_dir + filename)
        root = tree.getroot()

        # 找到所有的 <name> 标签
        for name in root.iter('name'):
            # 如果当前的名字是 "CrossWalk"，则更改它
            if name.text == 'CrossWalk':
                name.text = 'crosswalk'

        # 保存修改后的XML文件
        tree.write(xml_dir + filename)