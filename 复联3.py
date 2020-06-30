import requests
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                  'Safari/537.36'}
urls = []

for n in range(2300):
    if len(str(n)) < 3:
        u = 'https://yushou.qitu-zuida.com/20180730/10436_460523b5/800k/hls/c9d2ca77f3f{}.ts'.format(
            '0' * (3 - len(str(n))) + str(n))
        urls.append(u)
    else:
        u = 'https://yushou.qitu-zuida.com/20180730/10436_460523b5/800k/hls/c9d2ca77f3f{}.ts'.format(str(n))
        urls.append(u)


def run(url):
    try:
        r = requests.get(url, headers=headers)  # 获取到目标视频的所有信息
        if r.status_code == 200:
            print(r.status_code)
            # l = l + r.content
            # 打印访问的状态码是否为200
            with open("D:\\film\\复仇者联盟3\\复仇者联盟3\\{}.mp4".format(urls.index(url)), 'wb') as f:  # 以二进制写的方式将r的二进制内容写入path
                f.write(r.content)
                f.close()
                # print('第', urls.index(url), "个文件保存成功！")
                print('下载进度:', urls.index(url) / len(urls), '%')
        else:
            print('下载结束或者文件保存失败！')
    except:
        print('请求出错！')


# 利用并发加速爬取，最大线程为50个，本文章中一共有50个网站，可以加入50个线程
# 建立一个加速器对象，线程数每个网站都不同，太大网站接受不了会造成数据损失
executor = ThreadPoolExecutor(max_workers=12)
# submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
future_tasks = [executor.submit(run, url) for url in urls]
# 等待所有的线程完成，才进入后续的执行
wait(future_tasks, return_when=ALL_COMPLETED)
