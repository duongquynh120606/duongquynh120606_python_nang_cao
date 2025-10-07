class MyClass:
    DogCount = 0
    def __init__(self, value):
        self.value = value
    
    def my_method(self):
        print("Giá trị của đối tượng là:", self.value)
# Tạo đối tượng
obj = MyClass(50)
# Gọi phương thức my_method của đối tượng obj
obj.my_method()