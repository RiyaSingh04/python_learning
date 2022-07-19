# (14 july)



x=5
y=6
total=5+6
print(total)

first_name = 'riya'
last_name = 'singh'
print(first_name.upper())
updated_name = first_name.capitalize()
print(updated_name)
lower_name = first_name.lower()
print(lower_name)
print(first_name.casefold())
print(first_name.center(50))
print(first_name.encode())
print(first_name.endswith('i'))

# 15 july
print(first_name.count('a'))
print(first_name.find('v'))
print(first_name.isdigit())
print('2'.isdigit())

# f string
sentence = f'{first_name} {last_name} is a coder'
print(sentence)
# list
lst = [1, 2, 3, 4, 5, 'hello', ['a', 'b','c']] 
print(lst[0])
print(lst[-1])
print(lst[-2][0])

lst[0] = 100
print(lst)

random_number_list =[10, 32, 12, 45, 67, 89, 12, 34, 56, 78, 90]
random_number_list.sort()
print(random_number_list)

print(random_number_list, 'before appending anything')
random_number_list.append('Riya')
print(random_number_list, 'after appending anything')

name="riya"
ls=list(name)
print(ls)
ls.sort()
print(ls)

a =[1, 2, 3]
b =[4, 5, 6]
a + b
print(a + b)
a.append(b)
print(a)
a.extend(b)
print(a)


print(a.count('b'))
a.reverse()
print(a) 

# list slicing
a =[1, 2, 3, 4, 'hello world', 5, 6, 7]
a[0:len(a):1]
print(a)
a[-1:4:-1]
print(a)

#16 july
#tuples
tup = (1, 2, 3, 4, 'hello world')
print(tup)
print(type(tup))
#set
st = {4, 3, 4, 4, 2, 1, 3}
print(st)

bt = {4, 5, 6}
print(bt)
print(type(st))
print(st.intersection(bt))
print(st.union(bt))

#dictionaries
map_ ={
    'first_name':'riya',
    'last_name':'singh',
    'company':'regex'
}
print(map_['first_name'])
#print(map_['company'])#key error because this key is not present in dictionary
print(map_.get('company', 'not found'))#comapny key is not present in dict so the default value not found will be print
print(map_.keys())
print(map_.pop('first_name'))#first_name will be remove from dict , popitem()method removes the last inserted item from the dict
print(map_)

#loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in lst:
#     print(i)
for i in lst[2:]:  #printing will start from 3
        print(i)

#using range
two_table = range(2,21,2)
print(list(two_table))

for i in range(1,10):
    print(i)

for i in range(len(lst)):
    print(lst[i])    
print( '  ')
for i in range(0,len(list),2):
    print(list[i])



    #nested
for i in [1,2,3]:
        for j in['a','b','c']:
            print(i,j)


#prime number    
#while loop
i = 0
while i < 5:
    print(i)
    i += 1

#17 july
#condition
fname = 'Riya'
lname = 'Singh'

if fname == 'Riya' and lname == 'Singh':
    print ('yes first name is Riya and last name is singh')
else:
    print ('No first name is not Riya')

if fname == 'Riya' or lname == 'Singh':
        print ('yes')
else:
        print('No') 

if fname == 'Riya' and not lname == 'gupta':
    print ('yes first name is Riya')
else:
    print('no first name is not Riya')   

# elif 
if 'Riya' in ['a' , 'b' , 'c']:
    print('Riya is in list')
elif 'p' in 'Riya':
    print('Riya has p in spelling.')
elif 'k' in 'khushi':
    print('khushi has k in spelling.')
else:
    print('kuch hi nhi mila.')    


# take input from user  and print character whose ascii value is even
string =input('enter a string')
for i  in string :
    if(ord(i)%2==0):
        print('even:'+i)

# take 5 input from user and append all those in list
x = int(input('enter a number'))
lst =[]
for i in range(0,x):
    y =input('enter string to append in lst')
    lst.append(y)
print(lst)

# question
no_of_elem = int(input("Enter a number"))
map_ ={
    'str':[],
    'int':[],
    'float':[]
}
for i  in range(no_of_elem):
    dt = input('enter datatype:')
    value = input('enter value for above datatype:')
    if dt == 'str':
        map_['str'].append(value)
    elif dt =='int':
        map_['int'].append(int(value))
    elif dt == 'float':
        map_['float'].append(float(value))
    else:
        print('please initialize a empty list for {dt}' , format(dt))
print(map_)   


   
   

           







