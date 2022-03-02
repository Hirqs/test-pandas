import pandas

print('\n********************************读取excel文件***************************************')
result1=pandas.read_excel(r'D:\桌面\2021级新生学号.xls')
print(result1)


print('\n**********************读取excel文件，并指定第一列为行索引*******************************')
result=pandas.read_excel(r'D:\桌面\2021级新生学号.xls',index_col=0)
print(result)


print('\n*******************************读取第二个sheet**************************************')
result=pandas.read_excel(r'D:\桌面\2021级新生学号.xls',sheet_name=1)
print(result)

print('\n***************************读取第二个sheet,指定列名***********************************')
result=pandas.read_excel(r'D:\桌面\2021级新生学号.xls',sheet_name=1,names=['id','name','class'])
print(result)

print('\n**************************查看指定前几行，默认前5行，指定行数写小括号里********************')
print(result1.head())


print('\n*****************************查看数据的（行数、列数）**********************************')
print(result1.shape)


print('\n******************************查看列索引列表*****************************************')
print(result1.columns.values)


print('\n******************************查看行索引列表*****************************************')
print(result1.index.values)





