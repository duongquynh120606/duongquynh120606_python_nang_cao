
class Dog:
# Class attributes
 DogCount = 0
 def __init__(self, name, size, age, color): 
    self.name = name # object attributes
    self.size = size # object attributes
    self.age = age # object attributes
    self.color = color # object attributes
# tạo đối tượng của lớp Dog
bull = Dog("Dom", "large", 2, "yellow") 
# in thuộc tính name của đối tượng bull
print(getattr(bull, 'name'))
# gán giá trị của age cho 3
print(getattr(bull, "age", 3))
# in giá trị của age
print(getattr(bull, 'age'))
# true nếu bull chứa thuộc tính large
print(hasattr(bull, 'large'))
# xóa thuộc tính age
delattr(bull, 'age')
# Kích hoạt lỗi nếu age đã bị xóa
print(bull.age)
"""
class Dog:
    # Class attributes
    DogCount = 0
    def __init__(self, name, size, age, color): 
        self.name = name # object attributes
        self.size = size # object attributes
        self.age = age # object attributes
        self.color = color # object attributes
# tạo đối tượng của lớp Dog
bull = Dog("Dom", "large", 2, "yellow") 
# in thuộc tính name của đối tượng bull
print(getattr(bull, 'name'))
# gán giá trị mặc định của age là 3 nếu không tồn tại
print(getattr(bull, "age", 3))
# in giá trị của age
print(getattr(bull, 'age'))
# true nếu bull chứa thuộc tính size
print(hasattr(bull, 'size'))
# xóa thuộc tính age
delattr(bull, 'age')
# Kích hoạt lỗi nếu age đã bị xóa
print(getattr(bull, 'age', 'Không có thuộc tính age'))
"""