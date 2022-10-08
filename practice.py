Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t(52,32,56,'abc')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t(52,32,56,'abc')
NameError: name 't' is not defined
t = (52,32,56,'abc')
type(t)
<class 'tuple'>
t = t + new_element('palak')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t = t + new_element('palak')
NameError: name 'new_element' is not defined
new_element = ('palak')
t = t + new_element
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t = t + new_element
TypeError: can only concatenate tuple (not "str") to tuple
a_tuple = (24,76)
a_tuple
(24, 76)
new_element = ("abc")
a_tuple = a_tuple + new_element
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a_tuple = a_tuple + new_element
TypeError: can only concatenate tuple (not "str") to tuple
a_tuple = a_tuple + new_element
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a_tuple = a_tuple + new_element
TypeError: can only concatenate tuple (not "str") to tuple
a_tuple
(24, 76)
t = (23,54)
t += ('abc')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t += ('abc')
TypeError: can only concatenate tuple (not "str") to tuple
t+=1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t+=1
TypeError: can only concatenate tuple (not "int") to tuple
