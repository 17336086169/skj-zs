# 组合视频并输出
from moviepy import *
from moviepy.video.compositing.concatenate import concatenate_videoclips

l = bytes()
w = []
for n in range(20, 60):
    try:
        with open("D:\\film\\乡村爱情12\\a\\{}.ts".format(n), 'rb') as f:
            a = f.read()
            l = l + a
            print(n)
    except:
        w.append(n)

# a.to_videofile("target1.mp4", fps=24, remove_temp=False)


with open("D:\\film\\乡村爱情12\\乡村爱情.mp4", 'wb') as f:  # 以二进制写的方式将r的二进制内容写入path
    f.write(l)
    f.close()
