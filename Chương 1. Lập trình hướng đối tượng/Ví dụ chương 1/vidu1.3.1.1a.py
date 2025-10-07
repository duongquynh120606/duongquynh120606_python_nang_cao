class Dog:
    __DogCount = 0
    def __init__(self, name, size, age, color):
        self._name = name
        self._size = size
        self.__age = age
        Dog.__DogCount += 1

obj1 = Dog("bull", "large", 2, "yellow")
# a. print("Number of Dog: {}".format(Dog._name)) #Lỗi
# b. print("Dog's Name is {}".format(obj1._name)) #Ko nên dùng - can thiệp vào 1 đối tượng
# c. print("Dog's age is {}".format(obj1.__age)) #Lỗi
# d. print("Number of Dog: {}".format(Dog.__DogCount)) #Lỗi
