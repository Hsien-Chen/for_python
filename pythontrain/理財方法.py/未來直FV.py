import numpy as np
title =input('計算什麼的未來值FV:')
rate = float(input('rate(/12):'))
nper = int(input('分幾期(月):'))
count= 0
ct =0
pmt = float(input('PMT:'))
pv = float(input('單筆現值PV:'))
while ct <= nper:
    
    print(ct)
    ct+=1
while count <= nper:
    
    print(title +str(count)+'後期本利和:',np.fv(rate/12, count,pmt,pv,when='end'))
    count+=1





