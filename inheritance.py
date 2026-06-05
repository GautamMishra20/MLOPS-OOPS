# Simple inheritance

# Base Class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a second.")
    
# Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
        
# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak() # Output: Generic Animal makes a sound.

# Create an instance of Dog
dog = Dog("Buddy")
dog.speak() # Output: Buddy barks.