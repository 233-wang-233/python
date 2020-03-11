import time
import tkinter
import tkinter.messagebox
def down_load():
    time.sleep(10)
    tkinter.messagebox.showinfo('提示','下载完成')
def show_about():
    tkinter.messagebox.showinfo('关于','作者：233-wang-233')

def main():
    top=tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',True)

    panel=tkinter.Frame(top)
    button1=tkinter.Button(panel,text='下载',command=down_load)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=down_load)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
if __name__ == '__main__':
    main()