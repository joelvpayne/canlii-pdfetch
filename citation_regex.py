import re

p = re.compile(r'((\b[0-9]{4})(\s)([a-zA-Z]{,8})(\s)([0-9]+\b))')
m = p.search('hello:2021 bcsc 2, the dogs ran away')

if m:
    print('Match found: ', m.group())
    year = m.group(2)
    forum = m.group(4)
    decision = m.group(6)
    citation = m.group(0)
    juris = forum[0:2]
    print(m)
    print(year, forum, decision, citation)
    print(juris)
    
else:
    print('No match')



