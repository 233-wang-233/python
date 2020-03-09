def main():
    try:
        with open('guido.jpg','rb') as f1:
            data=f1.read()
            print(type(data))
        with open('极多.jdp','wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print('无法打开指定文件')
    except IOError as e:
        print('读写文件时出错')
    print('程序执行完毕！')
if __name__ == '__main__':
    main()