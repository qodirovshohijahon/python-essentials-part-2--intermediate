**1.Is the below statement true regarding the variable name?** <br>
Statement: For the default encoding in python 3, A variable name can contain the letters from the
English language only.
- [ ] Yes
- [ ] No

**2.Choose the correct output of the following code:-**
```python
list1 = [("abc","bca"),24,56,23,64,[1,2,3]]
list2 = list(list1)
list2[1] = "abc"
list1[3] = "bca"
print(list1)
print(list2)
```
- [ ] Erorr
- [ ] [("abc","bca"),24.56,23.64,"bca"]<br>[("abc","bca"),"abc,23.64,[1,2,3]]
- [ ] [("abc","bca"),"abc",23.64,"bca"]<br>[("abc","bca"),"abc",23.64,"bca"]

**3.Choose the correct output of the following code:-**
```python
s = "0123456789"
obj = range(0,len(s),0)
l = []
for i in obj:
    l.append(int(s[i]))
add = 0
for i in obj:
    add = add + l[i]
print(add)
```
- [ ] 45
- [ ] 0
- [ ] Erorr
- [ ] 36

**4.Choose the correct output of the following code:-**
```python
i = ""
while i in "       ":
    print("Python", end= i)
```
- [ ] Python <br>Python <br>Python <br> .... <br> .... <br> .... <br> ....
- [ ] PythonPythonPythonPython....
- [ ] Erorr
- [ ] Print Nothing

**5.The output of the following code is:-**
```python
print(not("False"))
print(not(0))
print(not(""))
print(not(" "))
print(not(["Python"]))
print(not([]))
```
- [ ] False <br> True <br> True <br> False <br> False <br> True <br>
- [ ] False <br> False <br> False <br> False <br> False <br> False <br>
- [ ]  True  <br> False <br> False <br> True <br> True <br> False <br>

**6.Which among the following print statement will print 4?**
- [ ] print(2<<1)
- [ ] print(2^2)
- [ ] print(2**2)
- [ ] print(2*2)

**7.Choose the correct statement.**
- [ ] The below equation is evaluated from left or right. <br> `2&2+3*3**2`
- [ ] The below equation is evaluated from left or right. <br> `3*2/3*3`
- [ ] The below equation is evaluated from left or right. <br> `2&2+3*3**2`
- [ ] The below equation is evaluated from left or right. <br> `3*3/3*3`

**8.Choose the correct output of the following code:-**
```python
class Class_A:
    def __init__(self,var):
        return var
obj = Class_A(20)
print(obj)
```
- [ ] prints address of Class_A object
- [ ] Erorr
- [ ] 20

**9.Fill the blank with the correct option, So that the below code will print `File not found`**
```python
try :
    open("sys.txt","r")
expect _______:
    print("File not found")
expect :
    print("File not opened")
```
Assume that the file `sys.txt` does not exist in the system.
- [ ] OSErorr
- [ ] TypeEror
- [ ] ValueErorr
- [ ] IOErorr

**10.Assume that the location of the `sys.txt` file is `D:/New`.**
<br>
Which among the following code will print the data present inside the `sys.txt` file.
<br>
- [ ] file = open(`"D:\\New\sys.txt"`, `"r"`) <br> `for` each `in` file: <br> `print`(each)
- [ ] file = open(`"D:\New\sys.txt"`, `"r"`) <br> `for` each `in` file: <br> `print`(each) <br> file.close()
- [ ] file = open(`"D:\\New\sys.txt"`, `"r"`) <br> `for` each `in` file: <br> `print`(each) <br> file.close()
- [ ] file = open(`"D:\New\sys.txt"`, `"r"`) <br> `for` each `in` file: <br> `print`(each)

**11.Which among the following function is used to clos the file in the python program?**
- [ ] close()
- [ ] closed()
- [ ] end()
- [ ] flush()

**12.Which among the following are the correct whise to present**
`0.000000123`
- [ ] 1.23 * 10 ** -7
- [ ] 1.23E-7
- [ ] 1.23e-7
- [ ] 1.23 * 10 ^ -7

**13.Choose the correct output of the following code:-**
```python
i = 0
while i < 4:
    print(i, end="-")
    i += 1.5
    if((i < 4) == False):
        break
    else:
        print(0, end=" ")
```
- [ ] `0-1.5-3.0-`
- [ ] `0-1.5-3.0`
- [ ] `0-1.5-3.0-0`
- [ ] Erorr as else can not be used with a while loop

**14.Choose the correct output of the following code:-**
```python
class Calculate:
    var1 = 20
    def __init__(self,var1)
        self.var1 = var1
        self.var1 = Calculate.var1 + 7
        Calculate.var1 = Calculate.var1 + 7
    def Print(self):
        print(Calculate.var1)
        print(self.var1)
Calculate(10).Print()
Calculate(15).Print()
```
- [ ] 27 <br> 17 <br> 27 <br> 22 <br>
- [ ] 27 <br> 17 <br> 27 <br> 22 <br>
- [ ] 22 <br> 22 <br> 29 <br> 29 <br>
- [ ] Erorr

**15.Choose the correct output of the following code:-**
```python
print(tuple[3])
```
- [ ] Index Erorr
- [ ] Type Erorr
- [ ] Name Erorr
- [ ] Value Erorr

**16.Choose the correct output of the following code:-**
```python
x = 45
y = 25
def Sum(f):
    global x
    print("Sum inside Sum() :",x+y)
Sum(25)
print("Sum outside Sum() :",x+y)
```
- [ ] Sum inside Sum() : 70 <br> Sum outside Sum() : 70
- [ ] Sum inside Sum() : 50 <br> Sum outside Sum() : 70
- [ ] Sum inside Sum() : 50 <br> Sum outside Sum() : 50
- [ ] Erorr

**17.if the `sys.txt` file contains the 3 lines, <br> 1st line (Welcom), <br> 2nd line (To Python),<br> 3rd line (Programming)**
What will be the output of the following cod:-
```python
file = open(`"sys.txt"`, `"r"`)
print(file.read(500))
file.cose()
```
- [ ] Welcome <br> To Python <br> Programming
- [ ] Weico
- [ ] Welcome
- [ ] Erorr 

**18.Choose the correct output of the following code:-**
```python
result1 = "{0}, {2} and {1}" .format("a","b","c")
result2 = "{}, {} and {}" .format("a","b","c")
print(result1)
print(result2)
```
- [ ] a, c and b <br> a, b and c
- [ ] ,aa and a <br> a, a and a
- [ ]  a, b and c <br> a, b and c
- [ ]  a, a and b <br> ,and

**19.Will the below code will raise an erorr or not.**
```python
a = "😂"
b = "🥰"
c = "😊"
d = "🤨"
print(a + b + c + d)
```
- [ ] Yes
- [ ] No

**20.Choose the correct output of the following code:-**
```python
print(1**2**2.)
```
- [ ] 2
- [ ] 2.0
- [ ] 1.0
- [ ] 1

**21.The output of the following code is:-**
```python
print("%.2o"% (25))
print("%.5o"% (25))
```
- [ ] 31 <br> 00031
- [ ] 26 <br> 00026
- [ ] 25 <br> 00025
- [ ] 25 <br> 25

**22.Choose the correct output of the following code:-**
```python
print("% 10E"% (85792229130))
```
- [ ] 8.5792229130E + 10
- [ ] 8.579223E + 10
- [ ] 8.579223E + 09
- [ ] 8.579222913E + 10

**23.Which among the following are unary operators?**
- [ ] -
- [ ] +
- [ ] +=
- [ ] ~
- [ ] not
- [ ] &

**24.Choose the correct output of the following code:-**
```python
D = {5 : 5, 15 : "15", "5" : 5, "15" : 25}
D[str(15)] = 100
L = list(D)
L.append("Python")
print(L)
```
- [ ] [5, 15, "5", "15", "Python"]
- [ ] [5, "15", 5, 100, "Python"]
- [ ] [{5 : 5, 15 : "15", "5" : 5, "15" : 100}, "python"]
- [ ] Erorr, a dictionary can not be converted into a list

**25.Choose the correct output of the following code:-**
```python
print(0x3 | 0x9)
```
- [ ] 20
- [ ] 27
- [ ] 0b1011
- [ ] 11

**26.Choose the correct output of the following code:-**
```python
try :
    print(30/0)
except ZeroDivisionErorr :
    print("Zero Division Erorr")
else :
    print("Nothing went wrong")
except :
    print("Something went wrong ")
```
- [ ] 30/0
- [ ] SyntaxErorr will be raised.
- [ ] Zero Division Erorr.
- [ ] Nothing went wrong.

**27.Which among the following operators hove the lowst binding among all the operators present in python.**
- [ ] **
- [ ] =
- [ ] ~
- [ ] not

**28.Choose the correct output of the following code:-**
```python
i = ""
for i in "    ":
    print("Java", end=i)
```
- [ ] Java <br> Java <br> Java <br> . <br> . <br> .
- [ ] Java Java Java Java
- [ ] JavaJavaJavaJavaJava......
- [ ] Prints Nothing

**29.Which among the following is the correct way to delete the file `sys.txt` from the hard drive using the python program**
- [ ] import os <br> os.remove(sys.txt)
- [ ] import os <br> os.delete(sys.txt)
- [ ] del sys.txt

**30.Choose the correct output of the following code:-**
```python
class Class:                    #line1
    def __init__(self, var):    #line2
        self.var1 = var         #line3
        self._var1 = var        #line4
        self.__var1 = var       #line5
                                #line6    
obj = Class(20)                 #line7
print(obj.__var1)               #line8
print(obj._var1)                #line9
print(obj.var1)                 #line10
```
- [ ] The raises an erorr due to line 10.
- [ ] The raises an erorr due to line 9.
- [ ] The raises an erorr due to line 8.
- [ ] No erorr will be raised

**31.Choose the correct output of the following code:-**
```python
class A:
    def __init__(self):
        self.num1 = 10
    def show_num1(self):
        print(self.num1)

class B(A):
    def __init__(self):
        self.num2 = 20
    def show_num2(self):
        print(self.num2)

obj = B()
obj.show_num1()
obj.show_num2()
```
- [ ] 10 <br> 20
- [ ] 0 <br> 20
- [ ] Erorr

**32.Choose the correct output of the following code:-**
```python
class Parent:
    def __init__(self, age):
        self.age = age
    def get_Parent_age(self):
        return self.age

class Child(Parent):
    def __init__(self, age1, age2):
        self.age = age1
        super().__init__(age2)
    def get_Child_age(self):
        return self.age

son = Child(20,40)
print("Parent age: ", son.get_Parent_age())
print("Child age: ", son.get_Child_age())
```
- [ ] Parent age: 40 <br> Child age: 40
- [ ] Parent age: 40 <br> Child age: 20
- [ ] Parent age: 20 <br> Child age: 20
- [ ] Parent age: 20 <br> Child age: 40

**33.Choose the correct output of the following code:-**
```python
try:
    print("Pytho"n")
expect:
    print("Erorr is raised")
finally:
    print("Code End")
```
- [ ] Pytho"n
- [ ] None of the print function will print anything.
- [ ] Pytho"n <br> Code End
- [ ] Erorr is raised <br> Code End

**34.Due to which type of erorr the code will terminate:-**
```python
str = " , ".join(["Java", "Python", "Ruby"])
l = (str, " are", "Programing", "Langueges")
print(l[-5])
```
- [ ] IndexErorr
- [ ] TypeErorr, because join function takes tuple as an input
- [ ] NameErorr
- [ ] Valuerorr

**35.Which among the following way will convert the binary value '0b100' to the decimal value 4?**
- [ ] `print(int(100, 2))`
- [ ] `print(int(0b100, 2))`
- [ ] `print(int("100", 2))`
- [ ] `print(int("100", 10))`

**36.Due to which type of erorr the code will terminate:-**
```python
var = round(0.5) + round(0.6) + round(0.4)
print(var)
```
- [ ] 2
- [ ] 1
- [ ] 0
- [ ] 1.5

**37.Due to which type of erorr the code will terminate:-**
```python
a = {2 + 3} * 5 + 2 ** 2
print(a)
```
- [ ] 29
- [ ] 729
- [ ] Erorr
- [ ] 21

**38.Due to which type of erorr the code will terminate:-**
```python
class Calculate:
    A = 20
    B = 20
    def __init__(self, a, b)
        A = a
        B = b
        print(self.A + self.B / 2 + 1)

Calculate(4, 10)
```
- [ ] Erorr
- [ ] 10
- [ ] 10.0
- [ ] 31.0

**39.Which among the following is the correct way to comment multiple lines in python?**
- [ ] """Hello <br> Word <br> Python"""
- [ ] \*/Hello <br> Word <br> Python\*/
- [ ] </!--Hello <br> Word <br> Python-->
- [ ] #Hello <br> Word <br> Python#

**40.Due to which type of erorr the code will terminate:-**
```python
import math
print(math.factorial(0.6))
```
- [ ] 0.72
- [ ] TypeErorr
- [ ] ValueErorr
- [ ] SyntaxErorr