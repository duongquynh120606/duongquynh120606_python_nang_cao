class Dog:
# Class attributes
  DogCount = 0
  def __init__ (self, name, size, age, color): 
    self._name = name # protected attributes
    self._size = size # protected attributes
    self.__age = age # private attributes
    self.__color = color # private attributes
    Dog.DogCount = Dog.DogCount + 1
obj = Dog("bull", "large", 2, "yellow")
print("Number of dogs: {}".format(Dog.DogCount))