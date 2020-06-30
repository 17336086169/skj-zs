from multiprocessing import Process
import requests


class f5(Process):

    def __init__(self):
        super().__init__()

    def run(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                          'Safari/537.36',
            'Cookie': 'time_http://youku.cdn5-okzy.com/20200209/14377_d8ae3ad8/index.m3u8=83.32100000000004'}
        # l = bytes(0)
        n = 720
        while n < 820:
            url = 'http://youku.cdn10-okzy.com/20200210/12646_32e89dea/1000k/hls/2b5ec12034a{}.ts'.format(
                '0' * (6 - len(str(n))) + str(n))
            try:
                r = requests.get(url, headers=headers)  # 获取到目标视频的所有信息
                if r.status_code == 200:
                    print(r.status_code)
                    # l = l + r.content
                    # 打印访问的状态码是否为200
                    with open("D:\\video\\{}.mp4".format(n), 'wb') as f:  # 以二进制写的方式将r的二进制内容写入path
                        f.write(r.content)
                        f.close()
                        print('第', n, "个文件保存成功！")
                    n = n + 1
                else:
                    print('下载结束或者文件保存失败！')
                    break
            except:
                print('请求出错！')



