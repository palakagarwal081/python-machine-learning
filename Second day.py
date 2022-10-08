Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'skeijmd'
b=
SyntaxError: invalid syntax
b = '''nudkcniev
jurjfirrkrir
uhhjvi4ji4j4'''
print(b)
nudkcniev
jurjfirrkrir
uhhjvi4ji4j4
a = 'Hello world'
print(a)
Hello world
a[0]
'H'
a[7]
'o'
a[6]
'w'
a[-1]
'd'
a[10]
'd'
a[0][1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[0][1]
IndexError: string index out of range
a[0,1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[0,1]
TypeError: string indices must be integers
a[1,2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[1,2]
TypeError: string indices must be integers
a[0:2]
'He'
a[3:5]
'lo'
a[-4:-7]
''
a[-7:-4]
'o w'
a[-6:-5]
' '
a[-6:-5]
' '
a[-6:-4]
' w'
a[-8:-6]
'lo'
a[:2]
'He'
a[:2:1]
'He'
a[:10:2]
'Hlowr'

a[:11:2]
'Hlowrd'
a[6:11]
'world'
a{-5:]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[-5:]
'world'
a[6:]
'world'
a6[:1111]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a6[:1111]
NameError: name 'a6' is not defined. Did you mean: 'a'?
a[6:111]
'world'
#dlrow olleh
a[-1::-1]
'dlrow olleH'
a[::-1]
'dlrow olleH'
a[-11:0:-1]
''
a[-11::-1]
'H'
a[-1:0:-11]
'd'
[-1:-10:]
SyntaxError: invalid syntax
a[-1:-10:]
''
a[0::-1]
'H'
a
'Hello world'
a = 'hello world'
a.capitalize()
'Hello world'
a
'hello world'
a=a.capitalize()
a
'Hello world'
a = 'hello world'
a.title()
'Hello World'
a
'hello world'
a=a.title()
a
'Hello World'
a.center(50)
'                   Hello World                    '
a.center(50,'#')
'###################Hello World####################'
a.count('1')
0
a.count('l')
3
a=a.center(50)
a
'                   Hello World                    '
a.lstrip()
'Hello World                    '
a.rstrip()
'                   Hello World'
a.strip()
'Hello World'
a=a.strip()
a
'Hello World'
a.isupper()
False
a.islower()
False
a.upper()
'HELLO WORLD'
a=a.upper()
a
'HELLO WORLD'
a.lower()
'hello world'
a.islower()
False
a=a.lower()
a
'hello world'
a.islower()
True
a.startswith('he')
True
a.endswith('D')
False
len(a)
11
a[0]='M'
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a[0]='M'
TypeError: 'str' object does not support item assignment
del a[0]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
b = 'palak123@gmail.com'
b.split('@')
['palak123', 'gmail.com']
b
'palak123@gmail.com'
b=b.split()
b
['palak123@gmail.com']
'@'.join(b)
'palak123@gmail.com'
b='@'.join(b)
b
'palak123@gmail.com'
############################################################################################################################################################################################################################################
m = [12,'hi',2.3 500]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
m = [12,'hi',2.3,500]
m[0]
12
m[1:3]
['hi', 2.3]
m[0:3]
[12, 'hi', 2.3]
'hi' in m
True
12 in m
True
11 in m
False
'hello' in m
False
'hi' not in m
False
11 not in m
True
2*m
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
m += ['new val']
m
[12, 'hi', 2.3, 500, 'new val']
m -= ['new val']
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    m -= ['new val']
TypeError: unsupported operand type(s) for -=: 'list' and 'list'
m.append('abc')
m
[12, 'hi', 2.3, 500, 'new val', 'abc']
m.append('palak',11)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    m.append('palak',11)
TypeError: list.append() takes exactly one argument (2 given)
m += ['palak',11]
m
[12, 'hi', 2.3, 500, 'new val', 'abc', 'palak', 11]
m.extend(['x','y','kuch bhi'])
m
[12, 'hi', 2.3, 500, 'new val', 'abc', 'palak', 11, 'x', 'y', 'kuch bhi']
m.insert(2,'hello')
m
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'palak', 11, 'x', 'y', 'kuch bhi']
m.pop()
'kuch bhi'
m
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'palak', 11, 'x', 'y']
m.pop()
'y'
m
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'palak', 11, 'x']
mp=m.pop()
mp
'x'
m
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'palak', 11]
m.pop(10)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    m.pop(10)
IndexError: pop index out of range
m.pop(4)
500
m
[12, 'hi', 'hello', 2.3, 'new val', 'abc', 'palak', 11]
m.clear()
m
[]
m.reverse()
m
[]
n = [12,23,56,45]
n.reverse()
n
[45, 56, 23, 12]
n.sort()
n
[12, 23, 45, 56]
n.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    n.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
n.sort(reverse=True)
n
[56, 45, 23, 12]
max(n)
56
min(n)
12
m = [12,'hi',2.3,500,'new valve']
m.index()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    m.index()
TypeError: index expected at least 1 argument, got 0
m.index('hi')
1
m.index(500)
3
m[1:2]
['hi']
m[1][0]
'h'
############################################################################################################################################################################################################################################################
t = 52,23,'abc'
type(t)
<class 'tuple'>
len(t)
3
t.index('abc')
2
t[0]
52
t[:2]
(52, 23)
t[:3]
(52, 23, 'abc')
t[0]=42
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    t[0]=42
TypeError: 'tuple' object does not support item assignment
del [1]
SyntaxError: cannot delete literal
del t[1]
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    del t[1]
TypeError: 'tuple' object doesn't support item deletion
k = (12,52,85,(5,'abc',5.5),100)
type(k)
<class 'tuple'>
k[3]
(5, 'abc', 5.5)
k[4]
100
k[2]
85
k[1]
52
k[0]
12
k[3][1]
'abc'
k[3][1][1]
'b'
t
(52, 23, 'abc')
############################################################################################################################################################################################################################################################
s = {1,1,2,2,3,4,4,3}
tupe(s)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    tupe(s)
NameError: name 'tupe' is not defined. Did you mean: 'tuple'?
type(s)
<class 'set'>
print(s)
{1, 2, 3, 4}
s[0]
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[0:2]
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    s[0:2]
TypeError: 'set' object is not subscriptable
s2 = {23,3,41,4,'abc'}
type(s2)
<class 'set'>
s,intersection(s2)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    s,intersection(s2)
NameError: name 'intersection' is not defined
s.intersection(s2)
{3, 4}
s.union(s2)
{1, 2, 3, 4, 41, 'abc', 23}
s.add(100)
s
{1, 2, 3, 100, 4}
s.discard(100)
s
{1, 2, 3, 4}
s.remove(3)
s
{1, 2, 4}
s.pop()
1
s
{2, 4}
s.pop(4)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    s.pop(4)
TypeError: set.pop() takes no arguments (1 given)
s1 = {44,22,33}
s.update(s1)
s
{2, 33, 4, 44, 22}
s.clear()
s
set()
s = {1,1,2,2,3,4,4,3}
s
{1, 2, 3, 4}
max(s)
4
min(s)
1
len(s)
4
