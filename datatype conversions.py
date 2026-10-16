Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#integers
int(8)
8
int(3.0)
3
int('hello')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
int(8+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(8+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#flot

float(8)
8.0
float(4.3)
4.3
float('hello')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float('hello')
ValueError: could not convert string to float: 'hello'
float(5+8j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(5+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
string(8)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    string(8)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(3.9)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    string(3.9)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string('hi')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    string('hi')
NameError: name 'string' is not defined. Did you forget to import 'string'?
#strings
string(9)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    string(9)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string(9.0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    string(9.0)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> str(9)
'9'
>>> str(6.0)
'6.0'
>>> str('hello')
'hello'
>>> str(4=9j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> str(7+4j)
'(7+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(9)
(9+0j)
>>> complex(9.0)
(9+0j)
>>> complex('hi')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex('hi')
ValueError: complex() arg is a malformed string
>>> complex(3+7j)
(3+7j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(9)
True
>>> bool(8.9)
True
>>> bool('hi')
True
>>> bool(4+7j)
True
>>> bool(True)
True
>>> bool(False)
False
