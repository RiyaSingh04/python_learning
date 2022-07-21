# 21 july
#file_handeling

file = open('demo.txt', 'r')
# data = file.read()
data1 = file.readlines()
print(data1)
# print(data)

# write in a file 
file = open('demo.txt','w')
file.write('nfvnvjifikdkddr')
file.writelines('gddsrthj')
file.close()

file = open('demo.txt','r')
def fun_(file):
    dic = {}
    data = file.readlines()

    for i in data:
        sub , name = i.split()
        if sub in dic:
            dic[sub].add(name)
        else:
             dic[sub] = set()
             dic[sub].add(name)
    print(dic)  

fun_(file)

# randon.txt
file = open('random.txt' , 'r')
data = file.read().split()
def frequency(file):
    dict = {}
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

frequency(file)




#lambda
y = lambda n:[i for i in range(n)]
print(y(10))

#exception_handling
try:
    print(5/0)
except:
        print('cannot divide by 0')

#filter function
def even(n):
    return n%2==0

a = filter(even,[1,2,3,4,56,78,76,77])  #gives the values for which the function is returning true 
a = list(a)
print(a)
  
# class
class webseries:
    show_name = 'suites'
    show_len = '189'

web_series_obj = webseries()
print(web_series_obj.show_name)
print(web_series_obj.show_len)

class webseries:
    def __init__(self,name,season,episode):
        self.name = name
        self.season = season
        self.episode = episode
        print('i am hit') 

web_1 = webseries('game of thrones',1,1)
web_2 = webseries('hatim',1,2)
print(web_1.name,web_2.name)        





    



