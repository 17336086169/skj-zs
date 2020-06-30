# 主要是需要moviepy这个库
from moviepy.editor import *
import os

# 定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk("D://film//乡村爱情12//a"):
    print(files)
    # 按文件名排序
    # files.sort()
    # 遍历所有文件
    # files = ["D://film//乡村爱情12//乡村爱情12.mp4"]
    for file in files:
        # 如果后缀名为 .mp4
        # 拼接成完整路径
        filePath = os.path.join(root, file)
        # 载入视频
        video = VideoFileClip(filePath)
        # 添加到数组
        L.append(video)



# 拼接视频
final_clip = concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile("target2.mp4", fps=24, remove_temp=False)
