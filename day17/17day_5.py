import numpy as np
import pandas as pd

from pandas import Series,DataFrame
#创建
#Series是一维数据
s=Series(data=[120,136,128,99],index=['math','python','en','chinese'])
df=DataFrame(data=np.random.randint(0,150,size=(10,3)),index=list('abcdefhijk'),columns=['Python','En','Math'])
print(df)