# #編碼
# snowman = '\u2603'
# print(len(snowman))
# ds = snowman.encode('utf-8')
# print(len(ds))
# print(ds)
# # asc = snowman.encode('ascii')
# # print(asc) 
# #ascii無法編碼unicode字元
# #接下來以ignore丟棄無法編碼的東西
# ai = snowman.encode('ascii', 'ignore')
# print('ai=',ai)
# #或以?代替無法編碼的東西
# ar = snowman.encode('ascii', 'replace')
# print('ar =', ar)
# #產生python unicode字元字串
# ab = snowman.encode('ascii', 'backslashreplace')
# print(ab)
# #轉成可列印的Unicode轉譯序列印，可產生字元實體字串
# ab2 = snowman.encode('ascii', 'xmlcharrefreplace')
# print(ab2)
#解碼
place = 'caf\u00e9'
print(place)
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
# place2 = place_bytes.decode('ascii')
# print(place2)
place3 = place_bytes.decode('utf-8')
print(place3)
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)





