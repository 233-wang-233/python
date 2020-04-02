import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#读取美国各州的面积
areas=pd.read_csv('C:\\Users\\peng\\Desktop\\popution\\state-areas.csv')
#print(areas)
#美国各州的缩写
abbrevs=pd.read_csv('C:\\Users\\peng\\Desktop\\popution\\state-abbrevs.csv')
#美国人口数据
pop=pd.read_csv('C:\\Users\\peng\\Desktop\\popution\\state-population.csv')
#print(pop.shape)
#print(pop.head())#看前五行的数据
#进行级联,outer外连接，inner内连接,left_on和right_on表示左右相对应
pop2=pop.merge(abbrevs,how='outer',left_on='state/region',right_on='abbreviation')
#print(pop2.head())
#print(pop2.shape)
#print(pop2.isnull().any)#后两行有空值,USA的数据缺少
cond=pop2['state'].isnull()#定位为空的数据,state为空时返回True
#print(cond)
#去除重复值
#删除一列
pop2.drop(labels='abbreviation',axis=1,inplace=True)
pop2[cond]['state/region'].unique()
cond=pop2['state/region']=='PR'
#pop2['state'][cond]='Puerto Rico'
#cond=pop2['state/region']=='USA'
#pop2['state'][cond] = 'United State'
#print(cond)
#print(pop2.isnull().any())
cond=pop2['population'].isnull()
#print(pop2[cond].shape)
#将难以进行补全的空数据删除
pop2.dropna(inplace=True)
#print(pop2.shape)
#print(pop2.isnull().any())

#print(pop2.head())
pop3=pop2.merge(areas,how='outer')
#print(pop3.isnull().any())

pop3.dropna(inplace=True)
#print(pop3.head())
#计算人口密度
pop_density = (pop3['population']/pop3['area (sq. mi)']).round(1)
#print(pop_density)
pop_density=DataFrame(pop_density)
pop_density.columns = ['pop_density']
#print(pop_density.head())
pop4 = pop3.merge(pop_density,left_index=True,right_index=True)
pop4['year'].unique()
pop4['ages'].unique()
#print(pop4.head())
# 查找2012年美国各州的全民人口数据
# pandas非常强大的，可以像查询数据库一样进行数据查询
pop5=pop4.query("year==2012 and ages=='total'")
#print(pop5)
pop5.set_index(keys=['state/region','ages'],inplace=True)#按列索引，变成二维表
print(pop5.sort_values(by = 'pop_density'))#排序