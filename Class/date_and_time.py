import datetime
import time
# print(time.time())
# print(time.asctime())
# print(time.asctime(time.localtime(time.time())))

'''

datetime_object = datetime.datetime.now()
# print(datetime_object)
print("Year :", datetime_object.year)
print("Month :", datetime_object.month)
print("Day :", datetime_object.day)
print("Hour :", datetime_object.hour)
print("Minute :", datetime_object.minute)
print("Second :", datetime_object.second)

'''

# import calendar
# s = calendar.prcal(2022)

'''
# Classes in Python :

# 1. Name Space in Python
# 2. Built-In Class Attributes
# 3. Base OverLoading Methods

count = 5                         # Global variable
def some_method():    
    global count                    # Global Keyword to call Global Variable
    count=count+1
    local=10                        # Local Variable
    print(count)
    print(local)
    some_method()

'''

# Constructor

class klu:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \n Name : %s"%(self.id,self.name))

    obj1 = klu("Nitin",896)
    obj2 = klu("sai", 30)
    obj1.display()
    obj2.display()

