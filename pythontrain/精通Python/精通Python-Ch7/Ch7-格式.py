import re
source = 'Young Frankenstein'
# m = re.match('You', source)   #match 只會在模式位於來源開頭 
# if m:
#     print(m.group())
# m = re.search('Frank', source) #search不管模式在任哪
# if m:
#     print(m.group())
# m = re.match('.*Frank', source) # '  .*  '代表前方任何字元
# if m:
#     print(m.group())
m = re.findall('n.?', source) 
print(m)
m = re.split('n', source) 
print(m)
m = re.sub('n', '?', source) 
print(m)
















