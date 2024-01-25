Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("welcome to cps")
welcome to cps
>>> print("hello, wrld")
hello, wrld
>>> print("hello\nworld")
hello
world
>>> print("how\nare\nyou")
how
are
you
>>> 7//3
2
>>> 9//3
3
>>> 9//4
2
>>> print("Today"+"is"+"Wednesday")
TodayisWednesday
>>> print("Today",+"is" "Wednesday")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("Today",+"is" "Wednesday")
TypeError: bad operand type for unary +: 'str'
>>> print("today", "is", "wednesday")
today is wednesday
>>> #print statements send through the information directly, whatever is inside the quotes
>>> #the \n is a line break in between each \n in the code
>>> # the + sign is equal to addition so there is no space inbetween the strings
>>> print("123\n45\n6")
123
45
6
>>> 1+2*3
7
>>> (1+2)*3
9
>>> 7/3
2.3333333333333335
>>> 7%3
1
>>> 22/4
5.5
>>> 22//4
5
>>> #% is module
>>> 3**2
9
>>> 2**3
8
>>> #yes python follows the normal order of operations
>>> #the difference between / and // is that / is normal division // gives the whole number after division
>>> #the % gives the remainder
>>> # ** raises the following number to a power
>>> 6%2
0
>>> 1+2*3**4
163
>>> print("2+2=", "4")
2+2= 4
>>> print("50 pounds is", 50*0.453592, "Kilograms")
50 pounds is 22.6796 Kilograms
>>> #predict (4+3)//2--> i think it will be 3
>>> (4+3)//2
3
