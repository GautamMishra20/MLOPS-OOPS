# initiate a class
class Employees:
    # special method / magic method / dundar method - constructor
    def __init__(self) -> None:
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
    
    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")

# create an instance of the class called object
sam = Employees()

# print(sam.salary)
# print(sam.id)
# print(sam.designation)

# calling a method
# sam.travel("ooti")

print(type(sam))