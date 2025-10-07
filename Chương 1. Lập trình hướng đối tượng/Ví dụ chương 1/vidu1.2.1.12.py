class Dog:
 #Thuộc tính của lớp – thuộc tính tĩnh DogCount
 DogCount = 0
 def __init__ (self, name, size, age, color): 
    self.name = name # object attributes 
    self.size = size # object attributes 
    self.age = age # object attributes 
    self.color = color # object attributes 
    Dog.DogCount = Dog.DogCount + 1
 def __del__ (self):
    print("A dog object is being deleted.")
    Dog.DogCount=Dog.DogCount - 1
obj1 = Dog("bull", "large", 2, "yellow")
obj2 = Dog ("Poodle", "small", 1, "white")
print ("Number of dogs: {}".format(Dog.DogCount))