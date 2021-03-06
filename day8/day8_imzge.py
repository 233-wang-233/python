'''
图形用户界面和游戏开发
基于tkinter模块的GUI(五个步骤)
1.导入tkinter模块中我们需要的东西。
2.创建一个顶层窗口对象并用它来承载整个GUI应用。
3.在顶层窗口对象上添加GUI组件。
4.通过代码将这些GUI组件的功能组织起来。
5.进入主事件循环(main loop)。
'''
#两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，
# 那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
#修改嵌套作用域
import tkinter
import tkinter.messagebox
def main():
    flag=True
    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg=('red','hello world!')if flag else ('blue','GOODBUY world')
        label.config(text=msg,fg=color)

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗？'):
            top.quit()
#创建顶层窗口
    top=tkinter.Tk()
#设定窗口大小
    top.geometry('240x160')
    #设定窗口标题
    top.title('小游戏')
    #创建标签对象并添加到顶层窗口
    label=tkinter.Label(top,text='hello world!',font='Arial -32',fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()