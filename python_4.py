#function
from math import factorial


def greet():
    print("hello, world")
    return 'hi mars'

var = greet()
print(var)    # the return statement of function will be printed here

#factoial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact    
fact_of_5 = factorial(5)
fact_of_10 = factorial(10)

print(fact_of_5)
print(fact_of_10)

#print a table for any number
def table(n):
    for i in range(1,11):
        mul = n*i
        print(mul)

y = int(input('enter a number'))
table(y)

#return list 
def return_list():
    return[1,2,3]

print(return_list())

# function to return true if the string is capital
def stringg(str_):
    if str_ == str_.upper():
        return True +
    else:
        return False 

y = input('enter a string')  
print(stringg(y))      


#print sum of ASCII value of a string
def ascii(str_):
    sum_=0
    for i in str_:
        sum_ = sum_ + ord(i)
    return sum_

y = input('enter a string')
print(ascii(y))        


#using map
def ascii(str_):
    return sum(map(ord, str_))

y = input('enter a string')
print(ascii(y))


#function which takes to string username and password return( 4 characters of namee and pass)
def nam_pass(username, password):
    return(username[0:4] + password[-4:])

y = input('enter name')
x = input('enter password')
print(nam_pass(y,x))  


#return a no. which represent that immediate character comes in the  string is same as alphabet sequence
def alphabet(str_):
    count = 0
    for i in range(0,len(str_)-1):
        if ord(str_[i])+1 == ord(str_[i+1]):
            count+=1
    return count

y = input('enter a string')    
print(alphabet(y))            


lst = [1,2,3,4]
def lstev(lstt):
    for i in lstt:
        if i%2==0:
            print(i)
lstev(lst)            
