def test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s", name = "%s",value2 = "%s"' % (value, name, value2))
test('A')
test('\u2603')
test('\u00e9')
place = 'café'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)
