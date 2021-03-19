# 7.1~3
# import unicodedata
# mystery = '\U0001f4a9'
# print(mystery)
# print(unicodedata.name(mystery))
# pop_bytes = mystery.encode('UTF-8')
# print(pop_bytes)
# pop1= pop_bytes.decode('UTF-8')
# print(pop1)
# print(pop1 == mystery)
#7.4
# poem='''My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s, And now thinks he is a %s.'''
# args=('roast beef','ham','head', 'clam')
#print( '''My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s, And now thinks he is a %s.''' % ('roast beef','ham','head', 'clam'))
#7.5-6
# letter = '''Dear {salutation} {name}, Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}. Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}. Thank you for your support. Sincerely, {spokesman} {job_title}'''
# respon
#7.7~11
# mammoth= '''We have seen the Queen of cheese, \n
# Laying quietly at your ease,\n
# Gently fanned by evening breeze --\n
# Thy fair form no flies dare seize.\n

# All gaily dressed soon you'll go\n
# To the great Provincial Show,\n
# To be admired by many a beau\n
# In the city of Toronto.\n

# Cows numerous as a swarm of bees --\n
# Or as the leaves upon the trees --\n
# It did require to make thee please,\n
# And stand unrivalled Queen of Cheese.\n

# May you not receive a scar as\n
# We have heard that Mr. Harris\n
# Intends to send you off as far as\n
# The great World's show at Paris.\n

# Of the youth -- beware of these --\n
# For some of them might rudely squeeze\n
# And bite your cheek; then songs or glees\n
# We could not sing o' Queen of Cheese.\n

# We'rt thou suspended from baloon,\n
# You'd cast a shade, even at noon;\n
# Folks would think it was the moon\n
# About to fall and crush them soon.'''
# import re
# findc = re.findall(r'\b\w*r\b', mammoth)
# print(findc)
# findaeiou = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b',mammoth)
# print(findaeiou)
#7.12
import binascii
asd='47494638396101000100800000000000ffffff21f9'+'0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(asd)
print(len(gif))










