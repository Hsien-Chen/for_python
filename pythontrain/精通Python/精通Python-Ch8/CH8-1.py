# 讀寫byte
bdata = bytes(range(0,256))
# print(len(bdata))
# fout = open('bfile','wb')
# size=len(bdata)
# offset=0
# chunk=100
# while True:
#     if offset > size:
#         break
#     fout.write(bdata[offset:offset+chunk])
#     offset+= chunk
# fout.close()

# fin = open('bfile', 'rb')
# fin.seek(255)
# bdata = fin.read()
# # print(len(bdata))
# # print(fin.seek(255)
# print(len(bdata))
# print(bdata[0])

# CSV格式
import csv
villains=[['Doctor','No'],['R','K'],['M','B'],['A','G'],['E','B']]
with open('villains','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains','rt') as fin:
    cin=csv.reader(fin)
    villains = [row for row in cin]
print(villains)

import csv
with open('villains','rt') as fin:
    cin=csv.DictReader(fin,fieldnames=['last','first'])
    villains=[row for row in cin]
print(villains)

import csv
with open('villains','wt') as fout:
    cout=csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(villains)








