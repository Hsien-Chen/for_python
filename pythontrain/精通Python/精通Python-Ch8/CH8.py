
poem='''There was a young lady named Bright, \n
Whose speed was far faster than light,\n
She set out one day\n
In a relative way,\n
And returned on the previous night.'''
# print(len(poem))
fout = open('relatively.txt', mode='wt')
fout.write(poem)
print(poem,sep='',end='')
fout.close()
# try:
#     fout = open ('relatively.txt', mode='xt')
#     fout.write('openjun')
# except FileExistsError:
#     print('Its already have' )
# fin=open('relatively.txt','rt')
# poem=fin.read()
# fin.close()
# poem = ''
# fin = open('relatively.txt','rt')
# aaa=100
# while True:
#     bbb=fin.read(aaa)
#     if not bbb:
#          break
#     poem +=bbb
# fin.close()
# print('\n --------------------------------------------')
# print(len(poem))

# poem = ''
# fin = open('relatively.txt','rt')
# while True:
#     line=fin.readline()
#     if not line:
#         break
#     poem+=line
# fin.close()

# poem = ''
# fin = open('relatively.txt','rt')
# for line in fin:
#     poem+=line
# fin.close()

fin=open('relatively.txt','rt')
lines=fin.readlines()
fin.close()
print('\n------------------------')
for line in lines:
    print(line,end='')







