# -------------------------PYTHON------------------------------------
# print("hello")
# name="Tony Stark"
# age=51
# print(name)
# print(age)
# print("Tony stark is genius ")
# name=input("enter yor name")
# print(name)
# old_age=input("Enter your old age ")
# new_age=int(old_age)+2
# print(new_age)
# num1=input("First Number")
# num2=input("Second Number")
# sum=int(num1) + int(num2)
# print("Sum of two number is "+ str(sum))
#   special use of in to find whether sbstr is part of str or not
# for i in range(10):
#     print(i)
# name="Prabhat yadav"
# print("Pra" in name)
# print(3*2/4*2)
# print(3>=3 or  3==3)
# print(3>=3 and 3==3)
# age=input("Enter Your age")
# val=int(age)
# if val >= 16:2
#     print("You are eligible to vote")
#     print("Thank You") this 4 tab space sepcify that it is part of block of code

# print("Thank you")


# ##*********************CALCULATOR****************

# first_number=int(input("Enter first Number"))
# operator= input("Enter operator(+,-,*,/)")
# second_number=int(input("Enter second number"))
# if operator=="+":
#     print(first_number+second_number)

# if operator=="-":
#     print(first_number-second_number)

# if operator=="*":
#     print(first_number*second_number)     

# if operator=="/":
#     print(first_number/second_number)   
    
# else :
#     print("Enter valid opertaor")

#  ************************/CALCULATOR*******************************
# i=0
# while i<9 :
#     print((2*i-1) * "*")
#     i=i+1
# ***********list******
# marks=[100,200,300,400]
# print(marks[-1])
# print(marks[0:6])
# print(marks[0:-1])
# print(marks[0:-2])
# print(marks[0:-1])

# for score in marks:
#     print(score>150)

# marks.append(100)    
# for score in marks:
#     print(score)
# marks.clear() use to clear whole list
# ind=marks.index(200) find the index of 200 in list
# marks.sort()  sort the array
# marks.insert(0,900)  insert 900 at 0 index
# for score in marks:
#     print(score)
# print(88 in marks)  to check if 88 present in  marks
# print(len(marks))
# for score in marks:
#     if(score==300):
#         break
#     print(score)
   

# for score in marks:
#     if(score==300):
#        continue
#     print(score)
# ********************tuple*********************
# marks=(97,98,97,98,90,99,89)
# print(marks.count(97))
# print(marks.index(99))

# *******sets***********

# marks={100,100,100,78,98}
# print(marks)

# ********************FUNCTIONS**********
# def sum(first,second):
#     print(first+second)

# sum(1,4)
# x=["hello", "mj"]
# y=["hello", "mj"]
# z=x
# print(x is y)//even though both have same content but thay are not same object (have diff. location in memory)
# print(x==y)  
# print(x is z)
# print("mj" in x)


# **************FILE HANDLING***********


# F=open("File_name1.txt","r")
# data=F.read()
# print(data)

# F=open("File_name1.txt","r+")
# print(F.read())
# F.write("Hello  i am Prabhat yadav")

# F=open("File_name1.txt","w+")
# F.write("Hello  i am Prabhat yadav")
# F.seek(0)  #used to move back to 0th location in order to read the data 
# print(F.read())

# F=open("File_name1.txt","a")
# F.write("Hello  i am Prabhat yadav")
# F.seek(0)
# print(F.read())

# F=open("File_name1.txt","a+")
# # F.write("Hello  i am Prabhat yadav")
# # F.seek(0)
# print(F.read())


# import sys
# print(sys.maxsize)
# x=1+3j
# # print(type(x))

# ###############################----PYTHON-PROBLEM---###############
# #<<<<<<<<<<<<<<---------Perfect no------>>>>>>>>>>>>
# def is_Perfect(num):
#     if num<=1:
#         return False
#     divisor_sum=1
#     for i in range(2,int(num)):
#           if num%i==0:
#               divisor_sum+=i
          

#     return divisor_sum==num

# a=int(input("Enter number  -"))

# if is_Perfect(a):
#     print("It is a Perfect Number")

# else: 
#     print("It is not a Perfect Numeber")

#<<<<<<<<<<<--------Neon number->>>>>>>

# def is_Neon(a):
#  square=a**2
#  sum=0
#  while square>0:
#      last=square%10
#      sum+=last
#      square=square//10
  
#  return sum==a

# a=int(input("Enter number- "))
# if is_Neon(a):
#     print("It is neon number")
# else :
#     print("It is not a neon number")    

#<<<<<-----------SPY NUMBER---->>>>>>>>>>

# def is_spy(a):
#   mult=1
#   sum=0
#   while a>0:
#    last=a%10
#    mult*=last
#    sum+=last
#    a=a//10


#   return mult==sum

# a=int(input("Enter Number"))
# if is_spy(a):
#     print("It is a spy number")
# else:
#     print("It is not a spy number")
#
#<<<<<<<<----------friendly number--->>>>>>>>>>>>
# def is_friendly_number(num):
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)
#     other_num = sum(j for j in range(1, divisors_sum) if divisors_sum % j == 0)
#     return other_num == num

# # Test the function
# num = int(input("Enter a number to check if it's a friendly number: "))
# if is_friendly_number(num):
#     print(f"{num} is a friendly number.")
# else:
#     print(f"{num} is not a friendly number.")
#___________________NAHI SAMAJH AAYA BAWA_________________________

#<<<<<<-----------------Automorphic number------->>>>>>>>

# def is_automorphic(a):
#     number = str(a)
#     square = a ** 2
#     square = str(square)
#     ct = 0
#     temp_a = a
#     while temp_a > 0:
#         temp_a = temp_a // 10
#         ct += 1
#     sliced_square = square[-ct:]
#     print(sliced_square)
#     print(square)
#     return number == sliced_square

# a = int(input("Enter number: "))
# if is_automorphic(a):
#     print("Yes")
# else:
#     print("No")

#_______________MAZA AAYA!!!!!!!__________________________

# ------HARSHAD NUMBER----------


# def is_harshad(a):
#     num=a
#     sum=0
#     while num>0:
#         last=num%10
#         sum+=last
#         num=num//10
        
#     return a%sum==0


# a=input("Enter number")

# if is_harshad(int(a)):
#     print("yes")
# else :
#     print("No")



#<<<<<<<<<<------------Abudant NUMBER----------->>>>>>>>>>>>>.
# def is_abudant(a):
#  sum=0
#  for i in range(2,a):
#     if a%i==0:
#        sum+=i
#  print(sum)
#  return sum>a 

# a=int(input("Enter no. "))
# if is_abudant(a):
#     print("Yes")
# else :
#     print("No")

#_______________MAZA AAYA!!!!!!!__________________________
#

# #<<------------UGLY NUMBER-------->>>>>>>>>>>
# def is_ugly(a):
#  if a%2==0 or a%3==0 or a%5==0 or a==1:
   
#        return True
#  else :
#        return False

# # a=int(input("Enter number"))
# for i in range(1,16):
#  if is_ugly(i):
#     print(f"{i} -yes")
#  else :
#     print(f"{i} -no")

#_______________MAZA AAYA!!!!!!!__________________________
#<<<<<<-------------DEFICIENT NUMBER------->>>>>>>>
# def is_deficient(a):
#   sum=0
#   for i in range(2,a):
#      if a%i==0:
#         sum+=i
#   return sum<a

# a=int(input("Enter the number"))

# if is_deficient(a):
#     print(f"{a} is a deficient number")
# else :
#     print(f"{a} is Not a deficient number")    

#_______________MAZA AAYA!!!!!!!__________________________

#<<<---------------------KARPAKER NUMBER------------>>
# s="hello"
# print(s[4:])
# def is_kaprekar(a):
#     sq = a ** 2
#     sq_str = str(sq)
#     for i in range(1, len(sq_str)):
#         s1 = int(sq_str[:i])
#         s2 = int(sq_str[i:])
#         if s1 + s2 == a and s1 != 0 and s2 != 0:
#             return True
#     return False

# t = int(input("Test cases: "))
# while t > 0:
#     a = int(input("Enter number: "))
#     if is_kaprekar(a):
#         print("Yes")
#     else:
#         print("No")
#     t -= 1

# print("GG">"GA")

#<<<<<<<<<<---------------STAR PATEERN------>>>>>>>>>>>>>..
# a= int(input("Enter number of rows"))

# for i in range(1,a+1):
   
#        print("*"*i)
   
# print("\n")
# def sum(a=10,b=2):
   
#    print(type((a,b)))

# a,b=input("Enter a number").split()

# sum(int(a),int(b))
 

# def sum(a=10,b=2):
#     return a+b


# a,b=input("Enter two number").split()

# d=sum(int(a),int(b))
# print(d)

# def sum(a=10,b=2):
#     return a+b

# a,b=input("Enter two number").split()

# d=sum(b=10)
# print(d)
# s={1,2,2,2,2}
# print(s)
# ----------------Capital kr do=--------------
# def change(x):
#     b=""
#     for i in x:
#         i=int(i)
#         if i>chr(a) and i<chr(z):
         
#          i=int(i)
#          i=i-32
#          i=str(i)
#          b+=i
#     return b
# a=input("Enter string")



# a,b,c,d,e=map(int,input("Enter marks of 5 sub").split())

# total=a+b+c+d+e
# per=float(total/5)

# if per>=80:
#     print("A")


# sentence = "Hello, world! How are you?"
# words = sentence.split(2)  # Defaults to splitting on whitespace
# print(words)  # Output: ['Hello,', 'world!', 'How', 'are', 'you?']

# a=set({133,"a",})
# print(a)


# s="Prabhat"

# print("Prabhat1" in s)

# a=input("Enter number")

# for i in range (1,int(a)+1):
#         print(str(i)*i)

# s="I am the best in the world"
# g="NITIN"
# a=g[::-1]
# print(g.split("I"))
# f="Hello World"
# print(f.istitle())
# print(g.replace("N","*"))
# print(a)
# print(g[::2])

# ---------------OOPS IN PYTHON--------------------------

# class Student:
#     name="Prabhat Yadav"

# s1= Student()
# print(s1)
# print(s1.name)

#   __init__ constructor in .py 

# class Student:
   
#     def __init__(self, fullname):
#       print('Constructor Called...')
#       self.name= fullname
   
# s1= Student("Prabhat Yadav")
# # print(s1)
# print(s1.name)
# We can create multiple constructor in a single class of diffetrent type,  default and parameterized ,,,,,,construcors will be called according to the parameter paas during instance creation 


# --class and instance attribute - already known !!, Instance att.  > Classs att.

# Methods in class
# class student :
#     def __init__(name):
#         self.name= name

#     def hello(self):
#         print("Hello " , self.name ," !! How are you??"  )

# s1= student("Prabhat Yadav")
# s1.hello()

# -------Practice----------
# WITHOUT USING LIST
# class student : 
#     def __init__(self, marks1, marks2, marks3):
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
       

#     def avg(self):
#         avg_mrks =( self.marks1+ self.marks2+ self.marks3)/3
#         print("AVG marks is ", avg_mrks)

# s1=student(55,45,49)
# s1.avg()

#WITH USING LIST

# class student : 
#     def __init__(self, marks):
#       self.marks=marks
       

#     def avg(self):
#         avd_mrks=0
#         for i in self.marks:
#            avd_mrks+=i
        
#         avd_mrks/=3

#         print("AVG marks is ", avd_mrks)

# s1=student([55,45, 49])
# s1.avg()

# Static Methods , that dint use self parameter
# decorator @
# class student :
#     @staticmethod  Here due to use of static method we dont need to write self 


# --------Decorator allow us to wrap another function in order to extend the behaviour of the wrapped unction ---------



#     def hello():
#         print("I am the best in the world")

# s1=student()
# s1.hello()


# Inheritance---------------------------

# type of inheritance
# 1 single 
# 2 multi-level
# 3 multiple


# 2 multi-level
# class  car :
#     def start(self):
#         print("Car started")

# class tyota(car):
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(tyota):
#     def __init__(self, type):
#         self.type=type



# car1=fortuner("Diesel")
# car1.start()


# 3 multiple
#  class c(A,B):
#     multiple inheritance here!!
 
# super Keyword is used to change the methods of a parent class 


# class car:
#     def __init__(self, type):
#         self.type=type
#     def start(self):
#         print("Car started...")
    
# class tyota(car):
#  def __init__(self,name,type ):
#        self.name=name
#        super().__init__(type)
#        super().start()
    
# car1=tyota("pirus", "electric")
# print(car1.type)

# if you want to change the attribue of class we can uise differnt methods 

# Method 1
# class person:
#     name = " Prabhat "

#     def __init__(self, name):
#         self.__class__.name=name

# p1=person("Prabhat Yadav")
# print(p1.name)
# method 2
#   class method



# Property decorator
# class student:
#     def __init__(self, m1, m2, m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def calpercent(self):
#         percent= ((self.m1+ self.m2+self.m3)*100)/300
#         return percent

# s1=student(100, 99, 89)
# print(s1.calpercent())
# s1.m1=10
# print(s1.calpercent())


# insted of this we can use property decorartor 
# jab ek attribute ki value function pe depend krti hai to hum is function ko he ek poopertty ban sakte 

# class student:
#     def __init__(self, m1, m2, m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     @property
#     def calpercent(self):
#         return  str(((self.m1+ self.m2+self.m3)*100)/300) + "%"


# s1=student(100, 99, 89)
# print(s1.calpercent)
# s1.m1=10
# print(s1.calpercent)


# ----------Polymorphism--------
# + !!
# print(1+2+3)
# print("I am the "+ "best in the world")
# print([1,2,3]+ [4,5,6])

# /////////DUNDER FUNCTION /////////////
# class complex:
#   def __init__(self, real, img ):
#       self.real= real
#       self.img=img

 

#   def __add__(self, num2):
#      newReal=self.real+ num2.real
#      newImg=self.img + num2.img
#      return complex(newReal, newImg)
  

#   def __sub__(self, num2):
#      newReal=self.real- num2.real
#      newImg=self.img - num2.img
#      return complex(newReal, newImg)
  
#   def show(self):
#       print(self.real ,"i" , "+", self.img, "j")

# num1=complex(1,3)
# num2=complex(4,6)
# num1.show()
# num2.show()

# num3 = num1 + num2
# print("Add")
# num3.show()
# print("Subtract")
# num3 = num1 - num2

# num3.show()

# -------------PRACTICE TIME------------

#----------------------Q1

# class circle:
#     def __init__(self,r):
#         self.r=r
    
#     def area(self):
#         return 3.14*(self.r)*(self.r)
    
#     def parameter(self):
#         return 2*3.14*(self.r)
 
# c1=circle(1)
# print(c1.area())
# print(c1.parameter())

#-----------------------Q2

# class employee:
#     def __init__(self, name , role):
#         self.name=name
#         self.role=role

#     def show(self):
#         print("Name : " , self.name, )
#         print("Role: " , self.role, )

# class engineer(employee):
#     def __init__(self, exp, age):
#         self.exp=exp
#         self.age=age
#         super().__init__("Prabhat","SDE")

# e1=engineer(10, 32)
# e1.show()

#------------------FILE HANDLING --------------------

# f=open("File_name1.txt")
# print(f.name)

# import os
# a=input("Enter file name")
# if os.path.isfile(a):
#     print("File exist")
# else :
#     print("File not exist")

# f=open("File_name1.txt",'r')
# d=f.read(-3)
# print(d)
# f=open("File_name1.txt",'rb')
# e=f.read()
# print(e)


# f=open("File_name1.txt")
# d=f.readline()
# print(d,end="") to avoid a new empty line we use end=""
# f.close()


# f=open("File_name1.txt")
# d=f.readlines()
# print(d) 
# for i in d:
#     print(i)
# f.close()
# readlines returns the list

# f=open("File_name1.txt")
# print(f.tell())
# d=f.read(3)
# print(f.tell())
# d=f.read()
# print(f.tell())
# f.seek(0)
# print(f.read())

# f.close()

# ----Assignmnet--

# Q) To find number of lines , word and character in a text file  

# f=open("demo.txt",'r')

# total_char=0
# total_word=0
# total_lines=0

# for i in f:
     
#      total_lines+=1
#      i=i.strip() to remove \n

#      total_char+=len(i)

#      i=i.split()
#      total_word+=len(i)

# print(total_char)
# print(total_word)
# print(total_lines)

# f.close()

# Q) Find total vowel in a text File 

# f=open("demo.txt",'r')
# vowel=0
# for line in f:
#    for i in line:
#      if(i=='a' or i=='e' or i=='i' or i=='o'or i=='u' ):
#         vowel+=1


# f.close()
# print(vowel)

# f=open("write.txt",'w')

# f.write("Hi i am the best in the world")
# f.write("   \n- Prabhat Yadav")
# f.close()

# class Grandfather:
#     def test(self):
#         if isinstance(self, Child):
#             print("I am Child")
#         elif isinstance(self, Father):
#             print("I am Father")
#         elif isinstance(self, Grandfather):
#             print("I am Grandfather")


# class Father(Grandfather):
#     pass


# class Child(Father):
#     pass


# # Creating objects of each class
# grandfather_obj = Grandfather()
# father_obj = Father()
# child_obj = Child()

# # Calling the test method for each object
# grandfather_obj.test()  # Outputs: I am Grandfather
# father_obj.test()       # Outputs: I am Father
# child_obj.test()        # Outputs: I am Child

# class Emp():
#     def __init__(self, id, name, Add):
#         self.id = id
#         self.name = name
#         self.Add = Add

# Class freelancer inherits EMP
# class Freelance(Emp):
#     def __init__(self, id, name, Add, Emails):
#         super().__init__(id, name, Add)
#         self.Emails = Emails
        
#     def details(self):
#         print('The ID is:', self.id)
#         print('The Name is:', self.name)
#         print('The Address is:', self.Add)
#         print('The Emails is:', self.Emails)

# Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
# Emp_1.details()

# --------------------------------NUM PY------------------------
# import numpy as np
# import timeit

# a=np.array([[1,2,3]])
# print(a[0,1])
# print("Data Type", a.dtype)

# b=np.array([['a','b','c']])

# print("Data Type", b.dtype)
# a=np.array([1,2,3])
# b=np.array([1,2,3])
# # addition of 1d array 
# b=np.add(a,b)
# # or 
# b=a+b
# print(b)
# addition of 2d array 
# a=np.array([[1,2,3],[1, 2, 3]])
# b=np.array([[1,1],[1,1]])
# print(a*b)

# import sys 
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([0,1,2,3,4,5])
# ypoint1=np.array([0,10,20,30,40,50])
# ypoint2=np.array([0,11,22,33,44,55])
# plt.plot(xpoints,ypoint1,ypoint2)
# plt.show()
# plt.legend(['Existing Scheme','Proposed Scheme'])
# plt.xlabel('Time')
# plt.ylabel('Sensor value')
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# class greeting :
#     def __init__(self, name):
#         self.name=name

#     def greetings(self):
#         print("Hello "+self.name+ " , How are you??")
    
# g1=greeting("Piyush Yadav")
# del  g1.name
# g1.greetings()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}"

# class Employee(Person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age,)
#         self.salary = salary
    
#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age},  Salary: {self.salary}"

# emp = Employee("John Doe",1234,30000)
# print(emp.get_details())
# Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"{self.name} makes a sound."

# # Derived class (inherits from Animal)
# class Mammal(Animal):
#     def __init__(self, name, habitat):
#         super().__init__(name)
#         self.habitat = habitat
    
#     def describe(self):
#         return f"{self.name} lives in {self.habitat}."

# # Further derived class (inherits from Mammal)
# class Dog(Mammal):
#     def __init__(self, name, habitat, breed):
#         super().__init__(name, habitat)
#         self.breed = breed
    
#     def bark(self):
#         return f"{self.name}, the {self.breed}, barks!"

# # Create an instance of the Dog class
# my_dog = Dog("Buddy", "house", "Golden Retriever")

# # Access methods from all levels of inheritance
# print(my_dog.speak())        # From Animal class
# print(my_dog.describe())     # From Mammal class
# print(my_dog.bark())         # From Dog class
