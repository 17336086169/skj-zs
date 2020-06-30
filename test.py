l = bytes(0)
for n in range(100, 220):
    with open("D:\\video\\{}.mp4".format(n), 'rb') as f:
        a = f.read()
        print(a)
        l = l + a

with open("D:\\叉手1.mp4", 'wb') as f:  # 以二进制写的方式将r的二进制内容写入path
    f.write(l)
    f.close()


