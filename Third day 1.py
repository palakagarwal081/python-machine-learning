Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1 = {'name':['akash','akshat','sunny'],}
d1 = {'name':['akash','akshat','sunny'],'age':[25,20,22],}
type(d1)
<class 'dict'>
len(d1)
2
d1[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d1[0]
KeyError: 0
d1['name']
['akash', 'akshat', 'sunny']
d1['age']
[25, 20, 22]
d1
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1.keys()
dict_keys(['name', 'age'])
d1.values()
dict_values([['akash', 'akshat', 'sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['akash', 'akshat', 'sunny']), ('age', [25, 20, 22])])
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1['ph_no']=[1234567890,9087654321,5678904321]
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [1234567890, 9087654321, 5678904321]}
d1['name']=['somya','palak']
print(d1)
{'name': ['somya', 'palak'], 'age': [25, 20, 22], 'ph_no': [1234567890, 9087654321, 5678904321]}
d1['name'][0]
'somya'
d1['name'][0][::-1]
'aymos'
d1['name'][0][::1]
'somya'
d1['name'][1][::1]
'palak'
d1['name'][0]= ['akash']
d1['name']
[['akash'], 'palak']
d1['name']+= ['somya']
d1['name']
[['akash'], 'palak', 'somya']
d1['name']-='palak'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d1['name']-='palak'
TypeError: unsupported operand type(s) for -=: 'list' and 'str'
del d1['name']
print(d1)
{'age': [25, 20, 22], 'ph_no': [1234567890, 9087654321, 5678904321]}
del d1['ph_no'][1]
print(d1)
{'age': [25, 20, 22], 'ph_no': [1234567890, 5678904321]}
d1.captalize['name']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d1.captalize['name']
AttributeError: 'dict' object has no attribute 'captalize'
d1.get('email')
d1.get('name')
d1('age')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d1('age')
TypeError: 'dict' object is not callable
d1.get('age')
[25, 20, 22]
a=20
b='ML'
print(a,b)
20 ML
print(a,b,sep='        ')
20        ML
print(a,b,sep='@')
20@ML
print(a,b,sep=',')
20,ML
print(a)
20
print(b)
ML

======= RESTART: C:/Users/91882/Desktop/day_4/p.py =======
20###ML

======= RESTART: C:/Users/91882/Desktop/day_4/p.py =======
20
ML
a=input('enter your name: ')
enter your name: somya
a
'somya'

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter first number:11
enter second number:22
1122

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter first number:10
enter second number:22
32

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
Traceback (most recent call last):
  File "C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py", line 1, in <module>
    if age < 18 :
NameError: name 'age' is not defined

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
Traceback (most recent call last):
  File "C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py", line 1, in <module>
    if age < 18 :
NameError: name 'age' is not defined

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
Traceback (most recent call last):
  File "C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py", line 1, in <module>
    if age < 18 :
NameError: name 'age' is not defined

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter age18
A gift
a task

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter age12
A gift
enter age34
koi gift nahi hai

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter age13
A gift
enter age20
A gift
a task
enter daysunday
enter the condition:sick
party

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter age
= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter day Sunday
enter the condition:sick
party

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter day Sunday
enter the condition:Sick
party


= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter day: sunday
enter the condition: sick
Traceback (most recent call last):
  File "C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py", line 28, in <module>
    if condition=='sick':
NameError: name 'condition' is not defined. Did you mean: 'codition'?

= RESTART: C:/Users/91882/AppData/Local/Programs/Python/Python310/p.py
enter day: sunday
enter the condition: sick
take rest






range(0,11)
range(0, 11)
list()
[]
list(range(0,11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list(range(2,101,3))
[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
list(range(1,101,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
