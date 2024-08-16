class Dog:
    #  构造函数 __init__()是一个特殊方法，每当你根据Dog类创建新实例时，Python都会自动运行它
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("xiao_li", 11)

print(my_dog.name)
# 修改属性值
my_dog.name = 'xiaowang'
print(my_dog.name)
my_dog.sit()


# score = int(input())
# if score > 90:
#     print("you")
# else:
#     print("cha")


# 继承Dog类
class SmallDog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        super().roll_over()

    def roll_over(self):
        print("重写了父类的方法")


my_new_dog = SmallDog("xiaogou", 11)

my_new_dog.roll_over()
