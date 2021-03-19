
import pandas as pd

data=pd.DataFrame({
    "name":["Amy","Bob","Jack"],"salary":[50,55,60]
},index=["a","b","c"])
#觀察資料
# print("資料數量",data.size)
# print("資料形狀,(列:欄)",data.shape)
# print("資料索引",data.index)

#取得列(ROW/橫向)的Series 資料:根據順序、根據索引
# print("取得第二列",data.iloc[1],sep=("\n"))
# print("取得第c列",data.loc["c"],sep=("\n"))

#取得列(Colume/直向)的Series 資料:根據欄位名稱
# print("取得name 欄位",data["name"],sep=("\n"))
# names = data["name"]
# print("名字改大寫",names.str.upper(),sep="\n")
#計算薪水平均值
# salaries = data["salary"]
# print("薪水平均值",salaries.mean())

#建立新的欄位
data["revenue"]=[500,166,200]
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)


