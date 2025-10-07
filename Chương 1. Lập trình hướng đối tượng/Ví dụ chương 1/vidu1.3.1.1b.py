class Dog:

# Class attributes
  __DogCount = 0
  def __init__ (self, name, size, age, color): 
    self._name = name # protected attributes
    self._size = size # protected attributes
    self.__age = age # private attributes
    self.__color = color # private attributes
    Dog.__DogCount += 1

# Getter method for _name
  def get_name(self):
    return self._name
    
# Getter method for _age
  def get_age(self):
    return self.__age

  @classmethod
  def get_DogCount(cls):
    return cls.__DogCount

obj1 = Dog("bull", "large", 2, "yellow")
print("Dog of number: {}".format(obj1.get_DogCount()))
print("Dog's Name is: {}".format(obj1.get_name()))
print("Dog's Age is: {}".format(obj1.get_age()))
