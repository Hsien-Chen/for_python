# import matplotlib.pyplot as plt

# xpt = [1,3,5]
# ypt = [1,9,25]
# plt.plot(xpt,ypt) #畫線
# plt.show() #顯示繪製的圖形
import numpy as np

def calc_irr(lv, fp, n):
    values = np.full(n + 1, fp)
    values[0] = -lv
    return np.irr(values)

print('如果貸款10萬，每年還 9439.29 元，貸款20年，則貸款利率為: ', calc_irr(100000, 9439.29, 20))