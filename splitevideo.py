import cv2
import os
# 打开视频文件
video = cv2.VideoCapture('sample.mp4')

# 检查视频是否打开成功
if not video.isOpened():
    print("无法打开视频文件")
    exit()

# 创建目标文件夹
output_folder = 'frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_number = 0
while True:
    # 读取下一帧
    ret, frame = video.read()

    # 如果读取成功，保存这一帧为图片
    if ret:
        cv2.imwrite(os.path.join(output_folder, f'frame_{frame_number}.jpg'), frame)
        frame_number += 1
    else:
        # 如果没有更多的帧，退出循环
        break

video.release()