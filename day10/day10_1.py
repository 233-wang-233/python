#从一段文字中提取国内手机号
import re
def main():
    pattern=re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence='''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylisy=re.findall(pattern,sentence)
    print(mylisy)
    print('*'*30)
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('*' * 30)
    m=pattern.search(sentence)
    while m:
        print(m.group())
        m=pattern.search(sentence,m.end())
if __name__ == '__main__':
    main()