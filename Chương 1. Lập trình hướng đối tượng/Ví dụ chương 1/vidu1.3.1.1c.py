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

#Setter method for _age
  def set_age(self, new_value):
    self.__age = new_value
obj1 = Dog("bull", "large", 2, "yellow")
obj1.set_age(5)
print("Dog's age is {}".format(obj1.get_age()))
