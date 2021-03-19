import numpy as np
title =input('計算現值PV:')
rate = float(input('rate:'))
nper = int(input('分幾期(年):'))
pmt = float(input('PMT:'))
fv = float(input('單筆現值FV:'))
print(title ,np.pv(rate, nper,pmt,fv,when='end'))

