class Dog:
# Class attributes
 DogCount = 0
 def __init__(self, name, size, age, color): 
    self.name = name # object attributes 
    self.size = size # object attributes 
    self.age = age # object attributes 
    self.color = color # object attributes
 def __del__(self):
    print("A dog object is being deleted.")
obj = Dog("bull", "large", 2, "yellow") 
del obj