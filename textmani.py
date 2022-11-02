import re

'''s = 'First sentence. Sencond Sentence.'
ss1 = s.split('e.')
ss2 = re.split('e.',s)
print(s)
print('s.split()')

for ss in ss1:
    print('\t',ss,'"',sep='')
print('re.split()')
for ss in ss2:
    print('\t"',ss,'"',sep='')'''
    
s = 'This is a sentence'
wds = s.split()
hyphen = '-'
hyphenated = hyphen.join(wds)
print(s)
print(hyphenated)