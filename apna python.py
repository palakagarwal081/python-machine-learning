Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"Tony Stark"
'Tony Stark'
name = "Tony"
last name = "Stark"
SyntaxError: invalid syntax
first_name = "Tony"last_name = "Stark"
SyntaxError: invalid syntax
first_name = "Tony"
last_name = "Stark"
print(first_name,last_name)
Tony Stark
tony_age = 51
print(tony_age)
51
is_genius = True
print(is_genius)
True
Tony_is_genius = True
print(Tony_is_genius)
True
name = input("superhero_name")
superhero_namespider man.
print(name)
spider man.
name = input("secert superhero is ")
secert superhero is Tony
print(name)
Tony
name = input("secert superhero is ")
secert superhero is  Tony
print(name + "is secret  superhero")
 Tonyis secret  superhero
print(name + " is secret  superhero")
 Tony is secret  superhero
old_age = input("Enter your old age")
Enter your old age22
new_age = int(old_age)+2
print(new_age)
24
first = input("Enter the first number")
Enter the first number 2
second = input("Enter the second number")
Enter the second number 3
sum = first + second
print(sum)
 2 3
sum = int(first) + int(second)
print(sum)
5
print("the sum is",sum)
the sum is 5
name = "Tony Stark"
print(name.upper())
TONY STARK
print(name.lower())
tony stark
print(name)
Tony Stark
print(name.find('s'))
-1
print(name.find('S'))
5
print(name.find('Stark'))
5
print(name.find('Stark'))
5
'
name = "Tony Stark"
print(name.replace("Tony Stark","Ironman"))
Ironman
print(name)
Tony Stark
print(name.replace("Stark","Ironman"))
Tony Ironman
print(name)
Tony Stark
print(name.replace("S","Ironman"))
Tony Ironmantark
print(name.replace("T","Ironman"))
Ironmanony Stark
print(name.replace("T","M"))
Mony Stark
print('M')
M
print('M' in name)
False
print('T' in name)
True
print('Tony' in name)
True
print(5+2)
7

print(5/2)
2.5
print(5//2)
2
print(5*2)
10
print(5-2)
3
print(5%2)
1
print(5**2)
25
i=5
i=i+5
i += 5
i -= 5
i *= 5
rerult = 2+3*5
print(result)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined. Did you mean: 'rerult'?
result = 2+3*5
print(result)
17
result = 2+3/5
print(result)
2.6
result = (2+3)*5
print(result)
25
print(3>2)
True
print(3<2)
False
print(3==2)
False
print(3!=3)
False
print(3!=2)
True
or and not
SyntaxError: invalid syntax
print(2 > 3 or 2<3)
True
print(2 > 3 and 2<3)
False
print(not 2 > 3)
True
print(not 2 < 3)
False
age = 19
if age >= 18:
    print("you are adult")
    print("you can vote")
print("thank you")
SyntaxError: invalid syntax
age = 19
print(age)
19
if age >= 18:
    print("you are adult")
    print("you can vote")
print("thank you")
SyntaxError: invalid syntax
if age >= 18:
    print("you are adult")
    print("you can vote")

    
you are adult
you can vote
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3
SyntaxError: expected ':'
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3:
    print("you are teenager")

    
you are adult
you can vote
age = 17
print(age)
17
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3:
    print("you are teenager")

    
you are teenager
age = 17
print(age)
17
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3:
    print("you are teenager")
else:
    
SyntaxError: multiple statements found while compiling a single statement
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3:
    print("you are teenager")
else:
    print("you are a child")

    
you are teenager
age = 2
age
2
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age< 18 and age > 3:
    print("you are teenager")
else:
    print("you are a child")

    
you are a child
first = input("Enter first operator")
Enter first operator
= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py
Enter first number: 56
Enter the operator(+,-,*,/,%) : *
Traceback (most recent call last):
  File "C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py", line 10, in <module>
    print(firxt * second)
NameError: name 'firxt' is not defined. Did you mean: 'first'?

= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py
Enter first number: 5
Enter the operator(+,-,*,/,%) : 2


= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py
Enter first number: 5
Enter the operator(+,-,*,/,%) : *
Traceback (most recent call last):
  File "C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py", line 10, in <module>
    print(first * second)
TypeError: can't multiply sequence by non-int of type 'str'

= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py
Enter first number: 5
Enter the operator(+,-,*,/,%) : *
Enter second number: 2
10


= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python310/calculator by python.py
Enter first number: 5
Enter the operator(+,-,*,/,%) : **
Enter second number: 3
125
numbers = range(5)
print(numbers)
range(0, 5)
i=1
i
1
while i<=5
SyntaxError: expected ':'
while i<=5:
    print(i)
    i+=1

    
1
2
3
4
5
while i<=5:
    print(i * "*")
    i+=1

    


while i<=5:
    print(i * "*")
    i+=1

    
i=1

i
1
while i<=5:
    print(i * "*")
    i+=1

    
*
**
***
****
*****
i=1
i
1
 while i<=5:
     print(i * "*")
     i-=1
     
SyntaxError: unexpected indent
while i<=5:
    print(i * "*")
    i-=1

    
*







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































Traceback (most recent call last):
  File "<pyshell#134>", line 2, in <module>
    print(i * "*")
KeyboardInterrupt
i = 5
i
5
while i>=0:
    print(i * "*")
    i-=1

    
*****
****
***
**
*

for item in range(5)
SyntaxError: expected ':'
for item in range(5):
    print(item)

    
0
1
2
3
4
marks = [34,56,"maths"]
marks
[34, 56, 'maths']
print(marks[1])
56
print(marks[-1])
maths
print(marks[1:3])
[56, 'maths']
print(marks[1:2])
[56]
for score in marks:
    print(score)

    
34
56
maths
marks.append(99)
marks
[34, 56, 'maths', 99]
marks.insert(96)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    marks.insert(96)
TypeError: insert expected 2 arguments, got 1
marks.insert(1,96)
marks
[34, 96, 56, 'maths', 99]
93 in marks
False
len(marks)
5
i=0
i
0
while i<len(marks)
SyntaxError: expected ':'
while i<len(marks):
    print(marks[i])
    i+=1

    
34
96
56
maths
99
marks.clear()
marks
[]
students = ["ram","shyam","kishan","radha"]
students
['ram', 'shyam', 'kishan', 'radha']
for student in students:
    if student == "kishan"
    
SyntaxError: expected ':'
for student in students:
    if student == "kishan":
        continue:
            
SyntaxError: invalid syntax
for student in students:
    if student == "kishan":
        continue
    print(student)

    
ram
shyam
radha

for student in students:
    if student == "kishan":
        break
    print(student)

    
ram
shyam
marks = (97,52,64,32,32)
marks
(97, 52, 64, 32, 32)
marks.index(97)
0
marks.count()
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    marks.count()
TypeError: tuple.count() takes exactly one argument (0 given)
marks.count(52)
1
[],(),{}
([], (), {})
1
1
marks = {97,52,64,32,32}.
SyntaxError: invalid syntax
marks = {97,52,64,32,32}
marks
{64, 97, 32, 52}
for score in marks:
    print(score)

    
64
97
32
52
marks = {"maths":97,"english":52,64}
SyntaxError: ':' expected after dictionary key
marks = {"maths":97,"english":(52,64)}
marks
{'maths': 97, 'english': (52, 64)}
marks["english"]
(52, 64)
marks["physics"] = 97
marks
{'maths': 97, 'english': (52, 64), 'physics': 97}
marks["physics"] = 99
marks
{'maths': 97, 'english': (52, 64), 'physics': 99}
import math
sqrt(12)
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    sqrt(12)
NameError: name 'sqrt' is not defined
import math
int(sqrt(2))
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    int(sqrt(2))
NameError: name 'sqrt' is not defined
import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
from math import sqrt
sqrt(4)
2.0
from math import *
isqrt(4)
2
pow(4,2)
16.0
def print_sum(first,second):
    print(first + second)

    
print_sum(1,2)
3
print_sum(11,89)
100
def print_sum(first,second=25):
    print(first + second)

    
print_sum(11,89)
100
print_sum(11)
36
