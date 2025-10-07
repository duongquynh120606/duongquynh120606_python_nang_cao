class Dog:
    # Thuộc tính  lớp
    DogCount = 0 
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng
        self.size = size # Thuộc tính đối tượng
        self.age = age # Thuộc tính đối tượng
        self.color = color # Thuộc tính đối tượng
    @classmethod
    def CountDog(cls, name, size, age, color): # Phương thức lớp
        cls.DogCount = cls.DogCount + 1 # Tăng số lượng đối tượng Dog
        return cls(name, size, age, color) # Trả về đối tượng Dog mới tạo
    @classmethod
    def get_DogCount(cls): # Phương thức lớp
        return cls.DogCount # Trả về số lượng đối tượng Dog đã tạo
obj = Dog.CountDog("bull", "large", 2, "yellow") # Tạo đối tượng Dog mới
print(" Số lượng đối tượng Dog đã được tạo: ",Dog.get_DogCount()) # In ra số lượng đối tượng Dog đã tạo
obj2 = Dog.CountDog("poodle", "small", 1, "white") # Tạo đối tượng Dog mới
print(" Số lượng đối tượng Dog đã được tạo: ",Dog.get_DogCount()) # In ra số lượng đối tượng Dog đã tạo