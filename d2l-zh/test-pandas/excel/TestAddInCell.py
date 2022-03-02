import pandas
from datetime import date,timedelta

books=pandas.read_excel(r'D:/桌面/testAdd.xlsx',
                        skiprows=1,                                 # 跳过一行空白行
                        usecols="B:H",                              # 读取B-E列的数据
                        dtype={'ID':str,'InStore':str,'Date':str}   # 将单元格数据类型设置为str
                        )
date=date(2022,3,2)
for i in books.index:
    # books['ID'].at[i] = i+1     # 用Series的at方法加
    # books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
    # books['Date'].at[i]=date
    books.at[i,'ID']=i+1        # 用DataFrame的at方法加
    books.at[i,'InStore'] = 'Yes' if i%2==0 else 'No'
    books.at[i,'Date',]=date
books['Price']=books['ListPrice']*books['Discount']  # 乘号出现时 左右两边是列的情况下 会将两列一个个相乘
print(books)
books=books.set_index('ID')
books.to_excel(r'D:/桌面/testAdd-output.xlsx')











