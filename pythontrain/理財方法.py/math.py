from openpyxl import Workbook
from openpyxl.chart import (
    AreaChart,
    Reference,
    Series,
)
from openpyxl.utils.dataframe import dataframe_to_rows
wb = Workbook()
ws = wb.active
for i in range(10):
    ws.append([i])


wb.save('test.xlsx')
