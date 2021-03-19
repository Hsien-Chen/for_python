# nl=[number*0.01 for number in range(1,6)]
# print(nl)
# count= 0
# rate = int(input('rate:'))
# while count < rate:
#     print(count)
#     count+=1
from openpyxl import Workbook
import numpy as np
from openpyxl.chart import (
    AreaChart,
    Reference,
    Series,
)
lv=float(input('貸款金額:'))
repay='本息攤還' #input('還款方式:')
yr=int(input('貸款年數:'))
yrate=float(input('年利息:'))
 # 創建一個空白活頁簿物件
wb = Workbook()
# 選取正在工作中的表單
ws = wb.active
# 指定值給 A1 儲存格
ws['A1'] = '貸款金額'
ws['A2'] = '還款方式'
ws['A3'] = '貸款年數'
ws['A4'] = '年利息'
ws['A5'] = '總繳利息'

ws['B1'] = lv
ws['B2'] = repay
ws['B3'] = yr
ws['B4'] = yrate


ws['A7'] = '期數(年)'
ws['B7'] = '貸款餘額'
ws['C7'] = '本金攤還'
ws['D7'] = '利息'
ws['E7'] = '繳款金額'
rf= (1+(yrate*0.01/12))**(yr*12)
rf1=rf*(yrate*0.01/12)
rf2=rf-1
rf3=(rf1)/(rf2)
# rowfirst={[1+(int(yrate)*0.01)**int(yr)]*int(yr)/[1+(int(yrate)*0.01)**int(yr)]-1}
ct=1


while ct <= yr*12:
    ws.cell(row=ct+8,column=1,value=str(ct))
    ws.cell(row=ct+8,column=5,value=rf3*lv)
    ct += 1 
dt=1
ws['B8']=lv
ws['D9']=lv*2.5*0.01/12
ws['C9']=ws['E9'].value - ws['D9'].value
ws['B9']=ws['B8'].value - ws['C9'].value
# while dt <= yr:
#     # ws.cell(row=dt+9,column=4)
#     # ws.cell(row=dt+9,column=2).value = 
#     a=ws.cell(row=dt+8,column=2)
#     # ws.cell(row=dt+9,column=4).value= a
#     # d9 = b8 * 2.5*0.01/12
#     dt += 1 
for ct in range(1,yr*12):

    a=ws.cell(row=ct+8,column=2) #上一期貸款餘額
    b=a.value #上一期貸款餘額 int
    ws.cell(row=ct+9,column=4).value=b*yrate*0.01/12
     #利息
    
    d=ws.cell(row=ct+9,column=5).value #繳款金額
    ws.cell(row=ct+9,column=3).value=d - (b*yrate*0.01/12)#本期繳款本金
    aplusaone=ws.cell(row=ct+9,column=2)#本期貸款餘額
    aplusaone.value=b-d+(b*yrate*0.01/12)

allrate=(rf3*lv)*yr*12
ws['B5'] = allrate 
rows=ws['A9':'E248']
for row in ws.iter_rows(min_row=8,min_col=1,max_row=8+yr*12,max_col=5):
    for cell in row:
        print(cell.value)

chart = AreaChart()
chart.title = "AreaChart"
chart.style = 13
chart.x_axis.title = 'test'
chart.y_axis.title = 'Percentage'

cats = Reference(ws, min_col=1, min_row=9, max_row=40)
data = Reference(ws, min_col=23, min_row=9, max_col=4, max_row=40)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

ws.add_chart(chart, "I9")
   

 # 向下新增一列並連續插入值

# 儲存成 create_sample.xlsx 檔案
wb.save('creat.xlsx')