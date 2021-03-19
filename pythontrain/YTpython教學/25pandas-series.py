#資料索引
import pandas as pd

# data = pd.Series([5,3,6,-4,8],index=["a","b","c","d","e"])
# print(data)

#觀察資料\
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)
#取的資料:根據順序、索引
# print(data[2],data[0])
# print(data["e"],data["a"])
# 數字基本運算、統計、順序
# print("最大值",data.max())
# print("最小值",data.min())
# print("總和",data.sum())
# print("中位數",data.median())
# print("最大三個數",data.nlargest(3))
# print("最小兩個數",data.nsmallest(2))
# print("所有相乘",data.prod())
# print("平均值",data.mean())
# print("標準差",data.std())


data = pd.Series(["您好","Python","Pandas"])
print(data.str.len())
print(data.str.lower())
print(data.str.upper())
print(data.str.cat(sep="-"))
print(data.str.contains("P"))
print(data.str.replace("您好","Hello"))




