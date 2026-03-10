# class Product:
#     count = 0
#     def __init__(self , name , price):
#         self.name = name
#         self.price = price
#         Product.count += 1
        
#     def getInfo(self):
#         print(f"price of {self.name} is {self.price}")
#     @classmethod
#     def getTotal(cls):
#         print(f"The total products till now are {cls.count}")
#    # @staticmethod
#     def getDicount(self , discount):
#         return self.price - (self.price * discount/100)
# p1 = Product("Phone" , 10_000)
# p2 = Product("Laptop" , 10_00_000)
# p1.getInfo()
# p2.getInfo()
# Product.getTotal()
# p3 = Product("Books" , 19_000)
# Product.getTotal() 
# print(f"The Discount price of Product {p2.name} is {p2.getDicount(50)}")


#Single Level Inheritance

# class Bank:
#     def __init__(self , name , balance):
#         self.name = name
#         self.__balance = balance #Private
#     def get_balance(self): #Getter
#         return self.__balance
#     def set_balance(self , bal):
#         self.__balance = bal
# acc1 = Bank("Yash" , 100)
# acc1.set_balance(4545)
# print(acc1.get_balance())
# class Employee:
#     start_Time = "10AM"
#     end_Time = "5AM"
# class Teacher(Employee):
#     def __init__(self , subject , name):
#         self.subject = subject
#         self.name = name
# t1 = Teacher("Physics" , "Yash")
# print(f"MR. {t1.name} teaches {t1.subject} from {t1.start_Time} to {t1.end_Time}")


#Multi Level Inheritance
# class Employee:
#     start_Time = "10AM"
#     end_Time = "5AM"
# class AdminStaff(Employee):
#     def __init__(self , role):
#         self.role = role
# class Accountant(AdminStaff):
#     def __init__(self , salary ,role):
#         super().__init__(role)
#         self.salary = salary
# acc1 = Accountant(5000 , "CA")
# print(acc1.role , acc1.salary)



#Multiple Level Inheritance
# class Teacher:
#     def __init__(self , salary):
#         self.salary = salary
        
# class Student:
#     def __init__(self , gpa):
#         self.gpa = gpa

# class TA(Teacher,Student):
#     def __init__(self , salary ,gpa, name):
#         super().__init__(salary)
#         Student.__init__(self, gpa)
#         self.name = name


# TA1 = TA(1500 , 9.99 , "Yash")
# print(f"{TA1.name} has score {TA1.gpa} and currently at salary of {TA1.salary}")       

 
# from abc import ABC , abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def makeSound():
#         pass
# class Lion(Animal):
#     def __init__(self , name):
#         self.name = name
#     def makeSound(self):
#         print(f"{self.name} sound Roar")
# class Cow(Animal):
#     def __init__(self , name):
#         self.name = name
#     def makeSound(self):
#         print(f"{self.name} sound Moo")
# L = Lion("Lion")
# C = Cow("Cow")
# L.makeSound()
# C.makeSound()


#Encapsulation
#Inheritace   
#Abstraction
#Polymorphism

#Function Over-riding
# class Employee:
#     def get_designation(self):
#         print("designation = Employee")
# class Teacher():
#     def get_designation(self):
#         print("designation = Teacher")
# class Accountant():
#     def get_designation(self):
#         print("designation = Accountant")


        
        
# data = True
# line = 1
# word = "Python"
# with open("sample.txt" , "r") as f:
#     while data:  
#         data = f.readline()
#         if("python" in data):
#             print(f"Word {word} Found at line no. {line}")
#             break
#         print(data)
#         line += 1

# try:  
#     x = int(input())
#     ans = 10/x
# except ZeroDivisionError:
#     print("Enter Number rather than 0")
# except ValueError:
#     print("Invalid Input")
# else :
#     print(ans)
# finally :
#     print("End of program")    
# squares = []
# for i in range(1,6):
#    squares.append(i*i)
# sq = [i*i for i in range(6) if i%2 != 0]
# print(sq)    
# list = [-2 , -4 , 3 , 5 , 2 , -1]
# list = [0 if val<0 else val  for val in list]
# print(list)
import json
# # json_str= '{"name":"Yash","isTeacher":true}'
python_obj= {'name': 'Yash', 'isTeacher': True}
# # pyt_obj = json.loads(json_str)
# # print(type(json_str) , json_str)
# print(type(python_obj) , python_obj)
# json_str = json.dumps(python_obj)
# print(type(json_str),json_str)
with open("data.json" , "w") as f:
    json.dump(python_obj , f , indent = 5 , sort_keys=True)