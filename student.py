class student:
    id=1
    fname="regex"

#object = className()
#student_john()
s1 = student()
print(s1.fname)
s2 = student()
print(s2.id)  


#constructor L=: function (memory allocate => object)
class student:
    def __init__(self,id,fName):
    #     print("hello")
    # id=1
      self.id = id
      self.fname=fName
    def studentInfo(self):
        print(self.id,self.fname)  


s1 = student(10,"john")
# print(s1.fname,s1.id)
# s2 = student("sakshi",9)
# print(s2.fname,s2.id) 
s1.studentInfo()