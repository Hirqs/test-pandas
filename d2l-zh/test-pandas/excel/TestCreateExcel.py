import pandas as pd

result = pd.DataFrame({'序号':[1,2,3],'姓名':['张三','李四','王五']})  # 字典
result = result.set_index('序号')      # 将序号设置为索引
print(result)
result.to_excel(r'D:\create.xls')

