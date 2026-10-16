Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=9
print(a)
9
x=10
print(x)
10
X=5
print(x)
10
9=1
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
9=1
A2=8
print(A2)
8
8E=7
SyntaxError: invalid decimal literal
w098765=1
print(1)
1
print(w09876)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(w09876)
NameError: name 'w09876' is not defined. Did you mean: 'w098765'?
name="pooja"
print(name)
pooja
print("name")
name
print(pooja)
Traceback (most recent call last):

  File "<pyshell#17>", line 1, in <module>
    print(pooja)
NameError: name 'pooja' is not defined
country=india
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    country=india
NameError: name 'india' is not defined
@=9
SyntaxError: invalid syntax
%=2
SyntaxError: invalid syntax
_=3
print(_)
3
_9=29
print(_9)
29
 e=(
     
SyntaxError: unexpected indent
#keywords

if=34
SyntaxError: invalid syntax
else=90
SyntaxError: invalid syntax
>>> #building functions
>>> int="Pranathi"
>>> print(int)
Pranathi
>>> float=80

>>> print(float)
80

>>> print(80)
80
>>> #single variable
>>> a=5,b=2
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=7;b=8
>>> print(a+b)
15
>>> a=6
>>> b=8
>>> print(a+b)
14
>>> a,b=2,7
>>> print(a+b)
9
>>> a=123456
>>> print(a)
123456
>>> a=1,2,3,4,5,6
>>> print(a)
(1, 2, 3, 4, 5, 6)
>>> a,b,c=(123)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c=(123)
TypeError: cannot unpack non-iterable int object
>>> a,b,c=1,2,3
>>> print(a,b,c)
1 2 3
>>> a=1,2,3,4
>>> print(a)
(1, 2, 3, 4)
>>> a=4 5 7 8 3
SyntaxError: invalid syntax
>>> a=d=g=29
>>> print(a,d,g)
29 29 29
>>> nnum name="pooja"
SyntaxError: invalid syntax
nnum name="pooja"
print(nnum name)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
num_name="pooja"
print(num_name)
pooja
fname="prana"
lname="prana"
print(fname+lname)
pranaprana

print(fname+lname)
pranaprana
pranaprana
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    pranaprana
NameError: name 'pranaprana' is not defined
NAME="pranathi"
print("NAME")
NAME
print(NAME)
pranathi
name="pranathi"
print(name)
pranathi
A,B,C=200
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    A,B,C=200
TypeError: cannot unpack non-iterable int object
A=B=C=200
pirnt(A,B,C)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    pirnt(A,B,C)
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print(A,B,C)
200 200 200
print(a.B.C)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(a.B.C)
AttributeError: 'int' object has no attribute 'B'
print(A.B.C)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(A.B.C)
AttributeError: 'int' object has no attribute 'B'
a=10
print(a)
10
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'A'?
