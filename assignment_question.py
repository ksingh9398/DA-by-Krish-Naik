#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.2: Python Basics
# ## Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)
# 

# ## 1. Syntax and Semantics
# 
# **Question 1:** Write a Python program to print "Hello, World!".

# In[1]:


print("Hello, Wlorld")


# **Question 2:** Write a Python program that takes a user input and prints it.

# In[199]:


user=input('Enter something : ')
print('You entered : ', user)


# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

# In[200]:


for i in range(3):
    num=float(input('Number : '))
    if num ==0:
        print('Zero Number')
    elif num < 0:
        print('Negative Number ')
    else :
        print('Positive Number')


# **Question 4:** Write a Python program to find the largest of three numbers.

# In[203]:


num1=float(input('Enter first number '))
num2=float(input('Enter second number '))
num3=float(input('Enter third number '))

if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
    

print('Largest number is : ', largest)


# In[16]:


num=[15,52,62,62,71,25,92,10,100,42]
print('maximum number of this list ',max(num))


# **Question 5:** Write a Python program to calculate the factorial of a number.

# In[206]:


num=int(input('Factorial of : '))
fact=1
for i in range (1,num+1):
    fact *=i
print(f"Factorial of {num} is {fact}")


# ## 2. Variables and Data Types
# 
# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.

# In[208]:


num1=float(input('1st Number : '))
num2=float(input('2nd Number : '))
int3=str(input('Input any string '))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
devision=num1/num2
floor_devision=num1//num2
modulus=num1%num2
boolien=True


print(f"addition of {num1} and {num2} is :  {addition} {type(addition)}")
print(f"subtraction of {num1} and {num2} is :  {subtraction} {type(subtraction)}")
print(f"multiplication of {num1} and {num2} is :  {multiplication} {type(multiplication)}")
print(f"devision of {num1} and {num2} is :  {devision} {type(devision)}")
print(f"floor_devision of {num1} and {num2} is :  {floor_devision} {type(floor_devision)}")
print(f"modulus of {num1} and {num2} is :  {modulus} {type(modulus)}")
print(f"boolien of {num1} and {num2} is :  {boolien} {type(boolien)}")
print(f"string of {int3} is :  {int3} {type(int3)}")


# **Question 7:** Write a Python program to swap the values of two variables.

# In[8]:


# Input values
a=int(input('Number a : '))
b=int(input('Number b : '))

c=a
a=b
b=c
print(f"after swaping : a = {a}, b= {b}")


# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.

# In[17]:


for i in range (3):
    # Input values
    celsius=float(input('Enter Celsious values : '))
    # Formula of convert Celsius to Fahrenheit
    far=(celsius*9/5)+32
    print(f"Converted Fahrenheig : {far} .F")


# **Question 9:** Write a Python program to concatenate two strings.

# In[22]:


# Input first name and second name
a=str(input('first name : '))
b=str(input('Second Name : '))
# full name
name=print(f"Full Nmae : {a}{b}")


# In[209]:


# Input first name and second name
a=str(input('first name : '))
b=str(input('Second Name : '))

name=a + " " + b
print('Full name : ',name)


# **Question 10:** Write a Python program to check if a variable is of a specific data type.

# In[210]:


var=input('Enter values : ')
if isinstance(var,str):
    print('True')
else:
    print('False')
type(var)


# In[106]:


var=input('Enter values : ')
if type(var)==str:
    print('This is String values ')
else:
    print('Wrong entyr, please enter String values')


# In[103]:


for i in range(3):
    var = input("Enter a value: ")
    try:
        var=int(var)
    except ValueError:
        pass
    if isinstance(var,int):
        print('TRUE : The variable is an Integer.')
    else:
        print('FALSE : The Variable is not an Integer')


# ## 3. Basic Operators (Arithmetic, Comparison, Logical)
# 
# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.

# In[ ]:





# In[109]:


num1=float(input('1st Number : '))
num2=float(input('2nd Number : '))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
devision=num1/num2
floor_devision=num1//num2
modulus=num1%num2
boolien=True


print(f"addition of {num1} and {num2} is :  {addition}")
print(f"subtraction of {num1} and {num2} is :  {subtraction}")
print(f"multiplication of {num1} and {num2} is :  {multiplication}")
print(f"devision of {num1} and {num2} is :  {devision}")
print(f"floor_devision of {num1} and {num2} is :  {floor_devision}")
print(f"modulus of {num1} and {num2} is :  {modulus}")
print(f"boolien of {num1} and {num2} is :  {boolien}")


# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

# In[113]:


num1=float(input('1st Number : '))
num2=float(input('2nd Number : '))
if num1>num2:
    print(f"{num1} is grater then {num2}")
elif num1==num2:
    print('Both are equal number')
elif num1!=num2:
    print('Both are not equal number')
elif num1<num2:
    print(f"{num1} is less then {num2}")
else :
    print('Wrong Entry')


# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

# In[211]:


a = True
b = False

print(f"True and False: {a and b}")
print(f"True or False: {a or b}")
print(f"not True: {not a}")


# In[117]:


a='Navin'
b='Kumar'
c='Singh'
print(a and b)


# In[129]:


a=10
b=20
c=30
print(a < b and b < c)
print(a > b or b < c)
print(a > b not b < c)


# **Question 14:** Write a Python program to calculate the square of a number.

# In[136]:


def square():
    for i in range(5):
        num=float(input('Number : '))
        square=num**2
        print(f"Square of {num} : {square}")
square()


# **Question 15:** Write a Python program to check if a number is even or odd.

# In[141]:


for i in range(2):
    num=int(input('Number : '))
    if num%2==1:
        print(f"{num} : Odd Number ")
    else:
        print(f"{num} : Even Number")


# **Question 16:** Write a Python program to find the sum of the first n natural numbers.

# In[170]:


num=int(input('Enter a number '))
a=0
if num>0:
    while num>0:
        a+=num
        num-=1
    print(a)
    
else : 
    print('No is negative')


# In[169]:


num=int(input('Enter number '))
addition=(num*(num+1))//2
print(f"sum of 1 to {num} : {addition} ")


# **Question 17:** Write a Python program to check if a year is a leap year.

# In[213]:


year=int(input('Enter Year : '))
if year%4==0:
    print(year, "is leap year")
else : 
    print(f"{year } is not leap year")


# **Question 18:** Write a Python program to reverse a string.

# In[180]:


n='NAVIN KUMAR SINGH'
a=''
for char in n:
    a = char+a
print(a)


# **Question 19:** Write a Python program to check if a string is a palindrome.

# In[183]:


a ='Racecar'
b=''
for char in a:
    b = char+b
if a.lower()==b.lower():
    print(a, 'is palindrome')
else:
    print(a, 'is not a palindrome')


# **Question 20:** Write a Python program to sort a list of numbers in ascending order.

# In[184]:


a =[3, 5, 3, -19, 78]
b=sorted(a)
print(b)


# **Question 21:** Write a Python program to sort a list of numbers in decending order.

# In[198]:


a =[3, 5, 3, -19, 78]
b=sorted(a,reverse=True)
print(b)


# In[ ]:




