# class Thing():
#     pass
# print(Thing)
# example = Thing()
# print(example)

# class Thing2:
#     letters = 'abc'
# print(Thing2.letters)

# class Thing3:
#     def __init__(self):
#         self.letters = 'xyz'
# asd = Thing3()
# print(asd.letters)

# class Element:
#     def __init__(self,name,symbol,number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
    # def dump():
    #     print('name','symbol','number')
# hydrogen = Element('Hydrogen','H','1')
# part = {'name':'Hydrogen','symbol':'H','number':'1'}
# # hydrogen=Element(part['name'],part['symbol'],part['number'])
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
# print(hydrogen.dump)
#6.6
# from collections import namedtuple
# Element = namedtuple('Element', 'name symbol number')
# part = {'name':'Hydrogen','symbol':'H','number':'1'}
# hydrogen2 = Element(**part)
# print(hydrogen2)
#6.7
# class Element:
#     def __init__(self,name,symbol,number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def __str__(self):
#         return ('name %s, symbol %s, number %s' %(self.name, self.symbol, self.number))
# part = {'name':'Hydrogen','symbol':'H','number':'1'}
# hydrogen = Element(**part)
# print(hydrogen)
#6.8
# class Element:
#     def __init__(self,name,symbol,number):
#         self.__name = name
#         self.__symbol = symbol
#         self.__number = number
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def symbol(self):
#         return self.__symbol
#     @property
#     def number(self):
#         return self.__number
# hydrogen = Element('Hydrogen', 'H', '1')
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
#6.9
# class Bear:
#     def eats(self):
#         return 'berries'
# class Rabbit:
#     def eats(self):
#         return 'clover'
# class Octothorpe:
#     def eats(self):
#         return 'campers'
# b = Bear()
# r = Rabbit()
# o = Octothorpe()
# print(b.eats())
#6.10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser=Laser()
        self.claw=Claw()
        self.smartphone=SmartPhone()
    def does(self):
        return  '''I have many attachment: my laser, to %s. my claw, to %s. my smartphone, to %s.''' % (self.laser.does(), self.claw.does(), self.smartphone.does())
r=Robot()
print(r.does())






















