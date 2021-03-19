import pandas as pd
#篩選條件-series
# data = pd.Series([30,15,20])
# condition =data>18#= [True,False,True]
# filterData = data[condition]
# print(filterData)

# data = pd.Series(["您好","Python","Pandas"])
# condition = data.str.contains("P")
# print(condition)
# filterData = data[condition]
# print(filterData)

#篩選條件-DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Jack"],"salary":[50,55,60]
})
condition =data["name"]=="Amy"#=data["salary"]>53#= [False,True,True]
filterData=data[condition]
print(filterData)







