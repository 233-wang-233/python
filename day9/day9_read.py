import time
def main():
    #一次性读取文件
    with open('D://练习.txt','r',encoding='utf-8',errors='ignore') as f:
        print(f.read())


    with open('D://练习.txt',mode='r') as f:
        for line in f:
            print(line,end='')#lines=f.readlines()
            time.sleep(0.5)
    print()
if __name__ == '__main__':
    main()