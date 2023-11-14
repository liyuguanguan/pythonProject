# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
# 元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。
# 例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的

aa = (3, )
print(aa[0])
dsa = ('f', 'd')
# 遍历元组
for a in dsa:
    print(a)
    # 重新给元组赋值
dsa = ('d', 'ff')
for a in dsa:
    print(a)



