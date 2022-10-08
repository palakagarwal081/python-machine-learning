Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = print("palak")
palak
a
print(a)
None
def myfunc(parameter)
SyntaxError: expected ':'
def myfunc(parameter):
    print("This is the firs function")

    
myfunc()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myfunc()
TypeError: myfunc() missing 1 required positional argument: 'parameter'
myfunc(parameter)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    myfunc(parameter)
NameError: name 'parameter' is not defined
def myfunc():
    print("This is the first function").
    
SyntaxError: invalid syntax
def myfunc():
    print("This is the first function")

    
myfunc()
This is the first function
a = myfunc()
This is the first function
print(a)
None
#no input no output
###############################################################################################################################################################################################################
#no input but output

def second():
    return "abcd"

second()
'abcd'
def second():
    return abcd

second()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    second()
  File "<pyshell#24>", line 2, in second
    return abcd
NameError: name 'abcd' is not defined

def second():
    return "abcd"

second()
'abcd'
b = second()
print(b)
abcd
###############################################################################################################################################################################################################

#input but no output

def third(x):
    print("Hello")

    
third()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
third(2)
Hello
###############################################################################################################################################################################################################

#input and output both

def fourth(x):
    return x/10

fourth(5)
0.5
def fourth(x):
    return x*0

fourth(5)
0
def fourth(x):
    return x*10

fourth(5)
50
def fourth(x):
    print("Hi")
    print("Hello")
    print("How are you?")
    return x*10

fourth(4)
Hi
Hello
How are you?
40
def fourth(x):
    print("Hi")
    print("Hello")
    print("How are you?")
    return x*10
print("Hey")
SyntaxError: invalid syntax
def fourth(x):
    print("Hi")
    print("Hello")
    print("How are you?")
    return x*10
    print("Hey")

    
fourth(3)
Hi
Hello
How are you?
30
##########################################################################################################################################

##Taking multiple input

def five(x,y,z):
    return x+y+z

five(7,2,5)
14


##returning multiple output

def five(x,y,z):
    return x+y+z, x*2, x**2

five(7,2,5)
(14, 14, 49)

##keyboard argument

def six(x,y,z):
    return (x+y+z)

six(x=2,y=3,z=8)
13
six(y=2,x=3,z=8)
13

##default values

def seven(x,y,z=1)
SyntaxError: expected ':'
def seven(x,y,z=1):
    return x+y+z

seven(4,8,7)
19
seven(4,8)
13
def seven(x=1,y,z=1)
SyntaxError: non-default argument follows default argument
def seven(x=1,y,z=1):
    
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z=1):
    return x+y+z

seven(4)
6

##args

##arguments = tuple

def eight(*x)
SyntaxError: expected ':'
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
eight(2,3,4)
(2, 3, 4)

##**kwargs
## keyword arguments = always return dictionary

def nine(**x):
    return x

nine()
{}
nine(2,5)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    nine(2,5)
TypeError: nine() takes 0 positional arguments but 2 were given
nine(2)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    nine(2)
TypeError: nine() takes 0 positional arguments but 1 was given
nine(name = "Palak","palk")
SyntaxError: positional argument follows keyword argument
nine(name = "Palak",email = "palak@gmail.com")
{'name': 'Palak', 'email': 'palak@gmail.com'}
nine(n1=0,n2=[11,10,13],n3=['a',"xyz",12,52])
{'n1': 0, 'n2': [11, 10, 13], 'n3': ['a', 'xyz', 12, 52]}
def my_name(x):
    print(4 * "Happy birthday to u")

    
my_name("palak")
Happy birthday to uHappy birthday to uHappy birthday to uHappy birthday to u
def my_name(x):
    print(4 * "Happy birthday to u /n")

    
my_name("palak")
Happy birthday to u /nHappy birthday to u /nHappy birthday to u /nHappy birthday to u /n
def my_name(x):
    print(4 * "Happy birthday to u")

    
my_name("bipul")
Happy birthday to uHappy birthday to uHappy birthday to uHappy birthday to u
def my_name(x):
    print(4 * "Happy birthday to u")
    print()

    
my_name("palak")
Happy birthday to uHappy birthday to uHappy birthday to uHappy birthday to u

i=4
i
4
def my_name(x):
    while i=4:
        print("Happy birthday to u")
    print()
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
def my_name(x):
    while i==4:
        print("Happy birthday to u")
    print()

    
my_name("palak")
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Happy birthday to u
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    my_name("palak")
  File "<pyshell#149>", line 3, in my_name
    print("Happy birthday to u")
KeyboardInterrupt
def my_name(x):
    while i==4:
        print("Happy birthday to u")
        i+=1
    print()

    
my_name("palak")
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    my_name("palak")
  File "<pyshell#152>", line 2, in my_name
    while i==4:
UnboundLocalError: local variable 'i' referenced before assignment
def birthday(name):
    print("Happy birthday to u")
    print("Happy birthday to u")
    print(f'Happy birthday to dear {name}')
    print("Happy birthday to u")

    
birthday("palak")
Happy birthday to u
Happy birthday to u
Happy birthday to dear palak
Happy birthday to u
i=4
i
4
def my_name(x):
    while i==4:
        print("Happy birthday to u")
        i+=1
    print()

    
my_name("Palak")
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    my_name("Palak")
  File "<pyshell#162>", line 2, in my_name
    while i==4:
UnboundLocalError: local variable 'i' referenced before assignment
def birthday(name):
    print("Happy birthday to u")
    print("Happy birthday to u")
    print(f"Happy birthday to dear {name}")
    print("Happy birthday to u")

    
birthday("Palak")
Happy birthday to u
Happy birthday to u
Happy birthday to dear Palak
Happy birthday to u

= RESTART: C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py

= RESTART: C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py
Traceback (most recent call last):
  File "C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py", line 7, in <module>
    my_name("Palak")
  File "C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py", line 3, in my_name
    while i==4:
UnboundLocalError: local variable 'i' referenced before assignment

= RESTART: C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py
Traceback (most recent call last):
  File "C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py", line 7, in <module>
    print(my_name("Palak"))
  File "C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py", line 3, in my_name
    while i==4:
UnboundLocalError: local variable 'i' referenced before assignment

= RESTART: C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py
Happy birthday to u

None

= RESTART: C:/Users/dell/Desktop/machine learning/palakakkkkakkakak.py
Happy birthday to uHappy birthday to uHappy birthday to uHappy birthday to u

None
def myfun(x,y,z):
    return x+y+z

mrfun(2,4,6)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    mrfun(2,4,6)
NameError: name 'mrfun' is not defined. Did you mean: 'myfun'?
myfun(2,4,6)
12
myadd = lambda x,y,z: x+y+z
myadd(5,9,7)
21
########lambda a one line anonymous function

def my_name(x):
    while i==4:
        print("Happy birthday to u")
    print()

    
my_name("Palak")
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    my_name("Palak")
  File "<pyshell#177>", line 2, in my_name
    while i==4:
NameError: name 'i' is not defined. Did you mean: 'id'?
