Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1 = {'name':['akash','akshat','sunny'],'semester':[2,1,2]}
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'semester': [2, 1, 2]}
d1['name'] += ['bunny']
d1
{'name': ['akash', 'akshat', 'sunny', 'bunny'], 'semester': [2, 1, 2]}
d1['name'] += 'bunny'
d1
{'name': ['akash', 'akshat', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'][0] += ['bunny']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d1['name'][0] += ['bunny']
TypeError: can only concatenate str (not "list") to str
d1['name'][1] += ['bunny']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d1['name'][1] += ['bunny']
TypeError: can only concatenate str (not "list") to str
d1['name'][1] += 'palak'
d1
{'name': ['akash', 'akshatpalak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'][1] += ',palak'
d1
{'name': ['akash', 'akshatpalak,palak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1d1['name'][1] += ['palak']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d1d1['name'][1] += ['palak']
NameError: name 'd1d1' is not defined
d1['name'][1] = ['palak']
d1
{'name': ['akash', ['palak'], 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'][1] = 'palak'
d1
{'name': ['akash', 'palak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'].insert('palak')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d1['name'].insert('palak')
TypeError: insert expected 2 arguments, got 1
d1.insert('name':'palak')
SyntaxError: invalid syntax
d1.insert(['name':'palak'])
SyntaxError: invalid syntax
d1.insert(['name','palak'])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d1.insert(['name','palak'])
AttributeError: 'dict' object has no attribute 'insert'
d1.push('akshat')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d1.push('akshat')
AttributeError: 'dict' object has no attribute 'push'
d1.push()='akshat'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

d1.push()=='akshat'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d1.push()=='akshat'
AttributeError: 'dict' object has no attribute 'push'
d1['name']=='akshat'
False
d1['name'].insert(1,'akshat')
d1
{'name': ['akash', 'akshat', 'palak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name']
['akash', 'akshat', 'palak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y']
new_key=sem
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    new_key=sem
NameError: name 'sem' is not defined. Did you mean: 'sum'?
new_key='sem'
old_key='semester'
d1.pop(old_key)=new_key
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
new_key=d1.pop(old_key)
d1
{'name': ['akash', 'akshat', 'palak', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y']}
d1[new_key]=d1.pop(old_key)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d1[new_key]=d1.pop(old_key)
KeyError: 'semester'
d1 = {'name':['akash','akshat','sunny'],'semester':[2,1,2]}
d1[new_key]=d1.pop(old_key)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d1[new_key]=d1.pop(old_key)
TypeError: unhashable type: 'list'
d1['sem']=d1.pop('semester')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d1['sem']=d1.pop('semester')
KeyError: 'semester'
d1 = {'name':['akash','akshat','sunny'],'semester':[2,1,2]}
d1
{'name': ['akash', 'akshat', 'sunny'], 'semester': [2, 1, 2]}
d1['sem']=d1.pop('semester')
d1
{'name': ['akash', 'akshat', 'sunny'], 'sem': [2, 1, 2]}
##f-string/sting format
##f-string/sting format
a = 'Akshat'
b = 'upflairs'
f'Hi {a} welcome to {b}'
'Hi Akshat welcome to upflairs'
f'Hi {b} welcome to {a}'
'Hi upflairs welcome to Akshat'
f'Hi {} welcome to {}'.format('Akshat','upflairs')
SyntaxError: f-string: empty expression not allowed
'Hi {} welcome to {}'.format('Akshat','upflairs')
'Hi Akshat welcome to upflairs'
for i in [1,2,3,4,5]:
    print(i)

    
1
2
3
4
5
for i in ('a','b','c','d'):
    print(i)

    
a
b
c
d
for i in 'helloworld':
    print(i)

    
h
e
l
l
o
w
o
r
l
d
