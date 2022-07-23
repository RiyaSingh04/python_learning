class school:
    def __init__(self,name,details):
        self.name = name 
        self.details = details
    def get_name(self):
        return f'This name is {self .name}'
    def get_details(self):
        return f'This details is {self .details}'    
    

class student(school):
    def __init__(self,name,details,rollno):
        super().__init__(name,details)
        self.name = name
        self.rollno = rollno   

    def get_name(self):
        return f'This name is {self.name}'
    def get_rollno(self):
        return f'This rollno is {self.rollno}'

rose_school = student('Riya', '306784930','6')
print(rose_school.get_name())
print(rose_school.get_details())
print(rose_school.get_rollno())
 