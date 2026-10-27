Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#upper()
a='code'
a.upper()
'CODE'
a='python is easy to learn'
a.upper()
'PYTHON IS EASY TO LEARN'
#lower()
c='good morning'
a.lower()
'python is easy to learn'
c='GOOD AFTERNOON'
c.lower()
'good afternoon'
#we use different methods but no use
a='python'
a.upper('P')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.upper('P')
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'P'
#capitalize()
a.capitalize()
'Python'
b='python course'
b.title()
'Python Course'
c='i am in class'
c.title()
'I Am In Class'
#isupper
a='python course'
a.isupper()
False
a=''PYTHON COURSE'
SyntaxError: unterminated string literal (detected at line 1)
a='PYTHON COURSE'
a.isupper()
True
#islower()

a='Vijayawada'
a.islower()
False
a='vijayawada'
a.islower()
True
a='hello'
a.isalpha()
True
a='hello world'
a.isalpha()
False
a='helloworld'
a.isalpha()
True
a.isdigit()
False
b=12345
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b='12345'
b.isdigit()
True
c='python course'
a.startswith('p')
False
c.startswith('p)
             
SyntaxError: unterminated string literal (detected at line 1)
c.startswith('p')
             
True
a.endswith('e')
             
False
b='PYTHON COURSE'
             
b.isupper()
             
True
m='pranathi125'
             
m.isalnum()
             
True
#strip is used for removing the whitespaces
             
#rstrip(),lstrip()
             
a='      pranathi        '
             
a.strip()
             
'pranathi'
a.rstrip()
             
'      pranathi'
a.lstrip()
             
'pranathi        '
#split()
             
a='python java flask c++'
             
a.split()
             
['python', 'java', 'flask', 'c++']
b='i am learning python'
             
b.split()
             
['i', 'am', 'learning', 'python']
c[1].upper()
             
'Y'
c=b.split()
             
c
             
['i', 'am', 'learning', 'python']
c[1].upper()
             
'AM'
#join()
             
a='apple','mango','grapes'
             
"".join(a)
             
'applemangograpes'
" ".join(a)
             
'apple mango grapes'
"s".join(a)
             
'applesmangosgrapes'
b='hello'
             
"k".join(b)
             
'hkeklklko'
#concatenation()
             
a='code'
             
b='gnan'
             
print(a+b)
             
codegnan
a='python'
             
b='course'
             
pritn(a+b)
             
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    pritn(a+b)
NameError: name 'pritn' is not defined. Did you mean: 'print'?
print(a+b)
             
pythoncourse
print(a+''+b)
             
pythoncourse
print(a+' '+b)
             
python course
fname='pranathi'
             
lname='kasimkota'
             
print(fname+lname)
             
pranathikasimkota
print(fname+" "+lname)
             
pranathi kasimkota
print(fname.title()+" "+lname.title())
             
Pranathi Kasimkota
print((fname+" "+lname).title())
             
Pranathi Kasimkota
print(fname+'.'+lname)
             
pranathi.kasimkota
print(fname+' '+lname......)
             
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname+' '+lname(....))
             
SyntaxError: invalid syntax
#formatting()
             
a=5
             
b=7
             
print(a+b)
             
12
print('the sum is',a+b)
             
the sum is 12
print('the sum is a+b')
...              
the sum is a+b
>>> city='guntur'
...              
>>> print('city is',city)
...              
city is guntur
>>> #format()
...              
>>> a='sweety'
...              
>>> b='pinky'
...              
>>> print('hello {}{}'.format(a,b))
...              
hello sweetypinky
>>> print('hello {} {}'.format(a,b))
...              
hello sweety pinky
>>> print('hello {} hello {}'.format(a,b))
...              
hello sweety hello pinky
>>> print('sweety{and} pinky {both are friends}'.format(a,b))
...              
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print('sweety{and} pinky {both are friends}'.format(a,b))
KeyError: 'and'
>>> #fstring()
...              
>>> a='sweety'
...              
>>> b='cuty'
...              
>>> print(f"hello{a}{b}")
...              
hellosweetycuty
>>> print(f"hello {a}{b}")
...              
hello sweetycuty
>>> print(f"hello {a} {b}")
...              
hello sweety cuty
>>> print(f"hello {a} hello {b}")
...              
hello sweety hello cuty
