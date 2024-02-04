import cv2
import os

frame_fps = 20
frame_width = 320
frame_height = 240

# 创建 VideoWriter 对象
writer = cv2.VideoWriter('Car2024.avi', cv2.VideoWriter_fourcc('P','I','M','1'), frame_fps, (frame_width, frame_height))

print("frame_width is ", frame_width)
print("frame_height is ", frame_height)
print("frame_fps is ", frame_fps)

# 获取文件夹中所有的.jpg文件
image_files = [f for f in os.listdir("Car2024/images") if f.endswith('.jpg')]


for image_file in image_files:
    image_name = os.path.join("Car2024/images", image_file)

    img = cv2.imread(image_name)
    if img is not None:
        writer.write(img)

writer.release()