# 5.1
# import zoo                        
# print(zoo.hours())                
# 5.2
# import zoo as menagerie
# print(menagerie.hours())
# 5.3 直接從zoo匯入hours()，並呼叫他
# from zoo import hours
# print(hours())
# 5.4將hours會入圍info,並呼叫他
# from zoo import hours as info
# print(info())
# 5.5 
# plain={'a':1, 'b':2,'c':3}
# from collections import OrderedDict
# fancy= OrderedDict([('a','1'), ('b','2'),('c','3')])
# print(fancy)
# 5.7
from collections import defaultdict
def nogood():
    print('something for a')
dict_of_lists= defaultdict(nogood)
print(dict_of_lists['a'])










