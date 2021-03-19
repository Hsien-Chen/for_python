
import pandas as pd

data = pd.Series([10,20,13])

# print(data)
# print("MAX", data.max())
# print("MEDIAN", data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)

#建立DataFrame
data = pd.DataFrame({"name":["Wang","Ben","Lee"],"salary":["40000","50000","60000"]})
print(data)
print("------------------------------------------")
#取的特定欄位
print(data["name"])
print(data["salary"])
print("------------------------------------------")
#取的特定列
print(data.iloc[0])
print(data.iloc[1])
print(data.iloc[2])