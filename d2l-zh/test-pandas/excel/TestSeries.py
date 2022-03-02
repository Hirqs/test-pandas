import pandas as pd
# Series [index:data] 类似于字典的 key value
# Series 在excel表中代表一行或者一列 只有加到dataFrame上才知道是行还是列
s1=pd.Series(data=[4,5,6],index=[1,2,3],name='A')  # A列 插入数据4 5 6 分别插到 1 2 3 索引下
s2=pd.Series(data=[10,20,30],index=[1,2,3],name='B')  # B列
s3=pd.Series(data=[100,200,300],index=[2,3,4],name='C')  # C列
df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})  # 以字典形式加入DataFrame
print(df)



