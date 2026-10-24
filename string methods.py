Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="python course"
a[-1:-8:-2]
'ero '
a[-2:-10:-3]
'son'
a[-3:-13:-4]
'r t'
a[-1:-12:-6]
'e '
a[-4:-9:-2]
'ucn'
a="cloud computing"
a[ : :5]
'c u'
a[ : :8]
'cm'
a[3: :11]
'ug'
a[5: : ]
' computing'
a[ :12: ]
'cloud comput'
a[ : :2]
'codcmuig'
#do's and do
a='python course'
a[9:5:2]
''
a[5:9:2]
'nc'
a[-10:-6:-2]
''
a[-6:-10:-2]
'cn'
a[ : :-1]
'esruoc nohtyp'
a[ : :1]
'python course'
#string methods
#len()
a='python'
len(a)
6

print(len(a))
6
b='python learning'
len(b)
15
a=''
len(a)
0
a="  "
len(a)
2

#count()
a='twinkle twinkle little star'
count(len(a))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    count(len(a))
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count("  ")
0
a.count(" ")
3
>>> a.count("")
28
>>> a="1234"
>>> a.count('3')
1
>>> a=1,2,3,4,5,,6
SyntaxError: invalid syntax
>>> a=1,2,3,4,5,6
>>> a.count(3)
1
>>> b=3,4,5,6,3,6,7
>>> b.count(3)
2
>>> #find a string
>>> a='code'
>>> a[2]
'd'
>>> a.find('d')
2
>>> b='hello'
>>> b.find('l')
2
>>> b[2:4]
'll'
>>> b.find("k")
-1
>>> a='name\nmobileno\tmailid\ncollege\tbranch'
>>> print(a)
name
mobileno	mailid
college	branch
>>> a='name-pranathi\nmobileno-98733 56223\tmailid:kasimkotapranathi@gmail.com\ncollege-nriit\tbranch-cse'
>>> 
>>> print(a)
name-pranathi
mobileno-98733 56223	mailid:kasimkotapranathi@gmail.com
college-nriit	branch-cse
>>> #replace()
>>> a='wait until you succeed'
>>> a.replace('wait','work')
'work until you succeed'
>>> m='hi'
>>> m.replace('h','e')
'ei'

