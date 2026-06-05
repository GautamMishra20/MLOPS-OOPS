# initiate a class
class Employees:
    # special method / magic method / dundar method - constructor
    def __init__(self) -> None:
        print(id(self))
        # print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("attributes/data have been initiated")
    
    # def travel(self,destination):
    #     print("This travel function was called manually")
    #     print(f"Employee is now travelling to {destination}")  simple working is happening
        
    # def travel(destination):
    #     print("This travel function was called manually")
    #     print(f"Employee is now travelling to {destination}")
    
    # Traceback (most recent call last):
    #     File "C:\Users\GAUTAM MISHRA\Desktop\MLOps\MLOPS-OOPS\oops1.py", line 25, in <module>
    #         sam.travel("ooti")
    #     TypeError: Employees.travel() takes 1 positional argument but 2 were given
            
    def travel(self):
        print("This travel function was called manually")
        print(f"Employee is now travelling to Delhi")
        
    # 1897285508368
    # 1897285508368
    # This travel function was called manually
    # Employee is now travelling to Delhi
    

# create an instance of the class called object
sam = Employees()
sam.name = "Samarth"
# print(id(sam1))
print(sam.name)

# sam2 = Employees()
# print(id(sam2))





# print(sam.salary)
# print(sam.id)
# print(sam.designation)

# calling a method
# sam.travel()

# print(type(sam))