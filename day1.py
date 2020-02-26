#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
身份验证

version：0.1
autor: 233-wang-233
'''
print('welcom to my word!')
print('please input  your six numbers id:')
id=input('')
if id == '123456':
      print('welcome!')
else:
      print('NONE!')


# In[7]:


'''
百分制成绩转化为等级制成绩
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

version：0.1
autor: 233-wang-233
'''
score=float(input('请输入分数:'))
if score>=90:
    grade='A'
elif 80<=score<90:
    grade='B'
elif 70<=score<80:
    grade='C'
else:
    grade='D'
print('对应等级:',grade)


# In[14]:


'''
计算三角形的周长和面积
要求：输入三条边长，如果能构成三角形就计算周长和面积。

version：0.1
autor: 233-wang-233
'''
print('输入三角形的边长:')
l_1=float(input(''))
l_2=float(input(''))
l_3=float(input(''))
#判断是否可构成三角形
if l_1+l_2>l_3 or l_1+l_3>l_2 or l_3+l_2>l_1:
    L=l_1+l_2+l_3
    area=(L*(L-l_1)*(L-l_2)*(L-l_3))**0.5 #海伦公式
    print('周长:%f'%L,"面积：%f"%area)
else:
    print('无法构成三角形')


# 
