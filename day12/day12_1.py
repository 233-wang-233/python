from  PIL import Image#读取和处理图像
image=Image.open('C:\\Users\\peng\\Pictures\\Screenshots\\屏幕截图(1).png')
image.format,image.size,image.mode\
    ('JPEG',(500,750),'RGB')
#(格式，尺寸，红绿蓝)
#剪裁图像
rect=80,20,310,360
image.crop(rect).show()#crop裁剪
#生产缩略图
size=128,128
image.thumbnail(size)#thumbnail缩略图
image.show()