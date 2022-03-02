import pandas as pd
import xlwt
result=pd.DataFrame({'姓名':['张三','李四','王五']})
# result=pd.DataFrame({'序号':[1,2,3],'姓名':['张三','李四','王五']})
result.to_excel('D:\\test_create.xls')