import requests
from concurrent.futures import wait, ALL_COMPLETED, ThreadPoolExecutor
import re

# 查找缺失的视频片段并重新抓取
w = []
for n in range(2246):
    try:
        with open("D:\\film\\复仇者联盟1\\复仇者联盟1\\{}.mp4".format(n), 'rb') as f:
            a = f.read()
            print(n)
    except:
        w.append(n)


urls = []

for i in w:
    if len(str(i)) < 3:
        u = 'https://haoa.haozuida.com/20180414/UdIpW9pw/800kb/hls/IQ7OZ7793{}.ts'.format(
            '0' * (3 - len(str(i))) + str(i))
        urls.append(u)
    else:
        u = 'https://haoa.haozuida.com/20180414/UdIpW9pw/800kb/hls/IQ7OZ7793{}.ts'.format(str(i))
        urls.append(u)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                  'Safari/537.36'}
w1 = []


def parser(url):
    # url = 'https://haoa.haozuida.com/20180415/0CTAPRlT/800kb/hls/JRguTUCI4019{}.ts'.format(str(n))
    try:
        r = requests.get(url, headers=headers)  # 获取到目标视频的所有信息
        if r.status_code == 200:
            print(r.status_code)
            # l = l + r.content
            # 打印访问的状态码是否为200
            with open("D:\\film\\复仇者联盟1\\复仇者联盟1\\{}.mp4".format(re.findall(r'7793(\d+?).ts', url)[0]), 'wb')as f:  # 以二进制写的方式将r的二进制内容写入path
                f.write(r.content)
                f.close()
                print('第', re.findall(r'7793(\d+?).ts', url)[0], "个文件保存成功！")
                # print('下载进度:', urls.index(url) / len(urls), '%')
        else:
            print('下载结束或者文件保存失败！')
            w1.append(url)
    except:
        print('请求出错！')


executor = ThreadPoolExecutor(max_workers=12)

tasks = [executor.submit(parser, url) for url in urls]

wait(tasks, return_when=ALL_COMPLETED)

"""
def p():
    import requests
    # 查找缺失的视频片段并重新抓取
    w = []
    for n in range(2246):
        try:
            with open("D:\\film\\复仇者联盟2\\复仇者联盟2\\{}.mp4".format(n), 'rb') as f:
                a = f.read()
                print(n)
        except:
            w.append(n)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                      'Safari/537.36'}
    w1 = []
    for n in w:

        url = 'https://haoa.haozuida.com/20180415/0CTAPRlT/800kb/hls/JRguTUCI4019{}.ts'.format(str(n))
        try:
            r = requests.get(url, headers=headers)  # 获取到目标视频的所有信息
            if r.status_code == 200:
                print(r.status_code)
                # l = l + r.content
                # 打印访问的状态码是否为200
                with open("D:\\film\\复仇者联盟2\\复仇者联盟2\\{}.mp4".format(n), 'wb') as f:  # 以二进制写的方式将r的二进制内容写入path
                    f.write(r.content)
                    # f.close()
                    print('第', n, "个文件保存成功！")
                    # print('下载进度:', urls.index(url) / len(urls), '%')
            else:
                print('下载结束或者文件保存失败！')
                w1.append(url)
        except:
            print('请求出错！')
"""





