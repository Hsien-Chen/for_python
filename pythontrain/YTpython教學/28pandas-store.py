import pandas as pd
#讀取資料
data = pd.read_csv("googleplaystore.csv")
#觀察資料
# print("資料數量",data.shape)
# print("資料欄位",data.columns)
# print("=================================================")
# 分析資料
# condition = data["Rating"]<=5
# data = data[condition]
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("前一百個應用程式平均",data["Rating"].nlargest(100).mean())
# print("前一千個應用程式平均",data["Rating"].nlargest(1000).mean())

#分析資料:安裝數量的各種統計數據
# print(data["Installs"])
# to_numeric 是 pandas裡將字串轉成數字
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# print(data["Installs"][10470])
# print(data["Installs"].mean())
# condition = data["Installs"]>100000
# print("安裝數大於100000",data[condition].shape[0])




# 基於資料應用:關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword ,case=False) #忽略大小寫
print("包含關 劍字的app",data[condition].shape[0])







