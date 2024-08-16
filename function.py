def hello():
    # haha
    print("nihao")


# 形参
def hello(username):
    print(username, '你好')


# 位置形参
def zoom(dog_name, cat_name):
    print(f"小狗名字{dog_name.title()} 小猫名字{cat_name}")


# 有默认值的形参
def zoom_default_value(dog_name='小金', cat_name='阿奇'):
    print(f"小狗名字{dog_name.title()} 小猫名字{cat_name}")


# 这种定义dog_name必须传否侧报错
def zoom_default_value1(dog_name, cat_name='阿奇'):
    print(f"小狗名字{dog_name.title()} 小猫名字{cat_name}")


# 带返回值
def get_input(input_name):
    return input_name


# 传递列表
def get_user_name(names):
    for name in names:
        print("hello1", name)
        # names.pop()


# hello()
# 实参


hello("xiao_wang")

zoom("金毛", "波斯")
zoom(dog_name="金毛1", cat_name="波斯1")
zoom("金毛2", "波斯")
zoom_default_value()
zoom_default_value1("haha")
print(get_input("返回的值"))

# 只打印a b 因为pop把c删除了
list1 = ['a', 'b', 'c']
# for name in list1:
#     # print(list1.pop())
#     print("hello", name)
#     list1.pop()

# 由于list[:]创建了一个副本所以打印三个
for name in list1[:]:
    # print(list1.pop())
    print("hello", name)
    list1.pop()
# get_user_name(list1)
list2 = ['1', '2', '3']
get_user_name(list2[:])


# print(list1)

# 例如，来看一个制作比萨的函数，它需要接受很多配料，但无法预先确定顾客要多少种配料。下面的函数只有一个形参*toppings，但不管调用语句提供了多少实参，这个形参会将它们统统收入囊中
def make_pizza(*toppings):
    print(toppings)


def make_pizza1(*toppings):
    for topping in toppings:
        print(topping)


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


print(build_profile('a', 'b', location='c', field='d'))


# make_pizza("面粉", "水", "馅料")
# make_pizza(list2)
# make_pizza1("面粉", "水", "馅料")


# 编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参
def make_sandwich(*params):
    for param in params:
        print("sandwich:" + param)


make_sandwich("面粉", "蔬菜", "酱")


# 编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件
def make_car(brand, type, **select):
    print("您选择的品牌是:", brand, "型号是:", type, "颜色是:", select["colour"])


make_car("奔驰", "T1", colour='黑色')
