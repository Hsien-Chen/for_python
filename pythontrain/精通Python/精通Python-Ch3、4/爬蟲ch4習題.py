# guess_me=7                                                       習題4.1
# #if guess_me<7:
# #    print('too low')
# #elif guess_me>7:
# #    print('too high')
# #elif guess_me==7:
# #    print('just right')    
# start = 1                                                        習題4.2
# while True:
#     if start < guess_me :
#         print('too low')
#     elif start==guess_me:
#         print('found it')
#         break
#     elif start > guess_me :
#         print('oops')
#         break
#     start+=1
# a=[3,2,1,0]                                                      習題4.3
# for b in a :
#     print(b)
# a_list=[number for number in range(10) if number % 2 ==0]        習題4.4
# print(a_list)
# number_thing=(number for number in range(1,6))   產生器生成式
# type(number_thing)
# squares={number:number*number for number in range(10)}           習題4.5
# print(squares)
# odd={number for number in range(10) if number % 2 !=0}           習題4.6
# print(odd)
# for thing in('Got %s' % number for number in range(10)):         習題4.7
#     print(thing)
# def good():                                                      習題4.8
#     return ['Harry','Ron','Hermione']
# print(good())
def echo(anything):
    'echo returns its input argument'
    return anything 
print(echo.__doc__)




