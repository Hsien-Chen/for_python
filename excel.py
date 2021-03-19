from openpyxl import Workbook

 # 創建一個空白活頁簿物件
wb = Workbook()
ws = wb.active
ws['A1'] = '我是儲存格'
wb.save('create_sample.xlsx')