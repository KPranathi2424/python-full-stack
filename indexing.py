Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #indexing

>>> a='vijayawada'
>>> a[4]
'y'
>>> a[0]
'v'
>>> a[0],a[1]
('v', 'i')
>>> a[0]+a[1]
'vi'
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[5]+a[6]
'in'
>>> a[2]+a[3]
'am'
>>> a[0]
'i'
>>> a[1]
' '
>>> a[1]+a[4]+a[7]
'   '
>>> a='i am learning python full stack
SyntaxError: unterminated string literal (detected at line 1)
>>> a='i am learning python full stack'
>>> a=[14]
>>> a=[14]+[15]+[16]+[17]+[18]+[19}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a=[14]+[15]+[16]+[17]+[18]+[19]
>>> 
>>> a='i am learning python full stack'
>>> a[14]+[15]+[16]+[17]+[18]+[19]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a[14]+[15]+[16]+[17]+[18]+[19]
TypeError: can only concatenate str (not "list") to str
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[2]+a[3]
'am'
>>> a[21]+a[22]+a[23]
'ful'
a[21]+a[22]+a[23]+a[24]
'full'
b='time is very precious'
b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
#negative indexing
a='vijayawada is a royal city'

a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-15]+a[-14]
'is'
'is'
'is'
b='vizag is a city of destiny
SyntaxError: unterminated string literal (detected at line 1)
b'vizag is a city of destiny'
b'vizag is a city of destiny'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'recious'
b='vizag is a city of destiny'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
#Slicing concept
a='codegnan'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a='work until you succeed'
a[15:22]
'succeed'
a[0:4]
'work'
a[5:10]
'until'
a[11:14]
'you'
b='simple is better than complex'
b[10:16]
'better'
b[0:6]
'simple'
b[22:29]
'complex'
b[7:9]
'is'
b[:6]
'simple'















3
3
3
#negative index
a='pyhton is easy to learn'
a='python is easy to learn'
a[-13:-9]
'easy'
a[-23:-17]
'python'
a[-5:-0]
''
a[-5:-1]
'lear'
a[-5: ]
'learn'
b='god is great'
b[-5:]
'great'
b[-12:-9]
'god'
b[-8:-6]
'is'
b[--5: ]
's great'
#striding concept
'cloud computing'
'cloud computing'
a[::5]
'pneta'
#striding concept
a='cloud computing'


