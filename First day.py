Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5+3
8
8*9
72
10/3
3.3333333333333335
10//3
3
'hello'*3
'hellohellohello'
hello*3
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hello*3
NameError: name 'hello' is not defined. Did you mean: 'help'?
'hello'+ 'world'
'helloworld'
'hello '+'world
SyntaxError: unterminated string literal (detected at line 1)
'hello '+'world'
'hello'+' world'
'hello world'
'hello'+' '+ 'world'
'hello world'
print('hello python')
hello python
a='python'
b=10
id(a)
1871889476528
id(b)
1871852995088
a = 'machine learning'
print(a)
machine learning
print(b)
10
print(a,b)
machine learning 10
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlst)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    len(keyword.kwlst)
AttributeError: module 'keyword' has no attribute 'kwlst'. Did you mean: 'kwlist'?
len(keyword.kwlist)
35
1='python'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a 1='python'
SyntaxError: invalid syntax
a$='python'
SyntaxError: invalid syntax
with = 'hii'
SyntaxError: invalid syntax
a_1=200
-='hello'
SyntaxError: invalid syntax
_='hello'
#a=200
a=20
b=55
a,b,c=20,55,60
print(a,b,c)
20 55 60
print(a)
20
print(b)
55
print(c0

print(c)
      
SyntaxError: '(' was never closed
print(c)
      
60
x=y=z=100
      
print(x)
      
100
print(x,y,z)
      
100 100 100
.
5+3
      
8
5-3
      
2
5/2
      
2.5
5//2
      
2
5*2
      
10
5**2
      
25
5%2
      
1
5<2
      
False
5>2
      
True
5<=2
      
False
5>=2
      
True
5!=2
      
True
5!=5
      
False
5==2
      
False
5==5
      
True
a=5
      
a+=5
      
print(a)
      
10
b=5
      
print(b)
      
5
c-=5
      
print(c)
      
55
d -= 6
      
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d -= 6
NameError: name 'd' is not defined. Did you mean: 'id'?
d-=6
      
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d-=6
NameError: name 'd' is not defined. Did you mean: 'id'?
a=10
      
a*=10
      
print(a)
      
100
2<5 and 10<100
      
True
2<5 or 10<100
      
True
2<5 and 10>100
      
False
2>5 or 10<100
      
True
