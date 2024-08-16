# 字典就是map

dd = {'b': 2, 'a': 1, }

print("dd", dd)

print(dd['a'])

# 添加数据
dd['c'] = 3
print(dd)

# 修改数据
dd['c'] = 4
print(dd)
# 删除键值
del dd['c']
print(dd)

if bool(dd):
    print("非空")
if dd is not None:
    print("非空")
# 判断元素是否为空
if dd.get('c') is None:
    print("为空")

print(dd.get('a'))
# 如果f不存在给f一个默认值
print(dd.get('f', 'gg'))

# 遍历字典
for a in dd.items():
    print(a)
# 遍历字典
for key, value in dd.items():
    print(key, value)
    print('key:', key)
    print('value:', value)

# 遍历字典的key
for aa in dd.keys():
    print('key:' + aa)
# 遍历value
for aa in dd.values():
    print('value: ', aa)
# 按照顺序遍历key python3.7中默认是按照插入顺序遍历的key
for aa in sorted(dd.keys()):
    print(aa)
# set去重复的value值
for aa in set(dd.values()):
    print("去重的value", aa)

    #     注意　可使用一对花括号直接创建集合，并在其中用逗号分隔元素：
    languages = {'python', 'ruby', 'python', 'c'}
    print(languages)

# 嵌套 列表嵌套字典
qiantao1 = {'a': 1}
qiantao2 = {'b': 1}
qiantao3 = {'c': 1}
list1 = [qiantao1, qiantao2, qiantao3]
for list2 in list1:
    print(list2)

# 字典嵌套列表
list2 = [1, 2, 3, 4]
map1 = {'a': list2}
print(map1)

# 字典嵌套字典
map11 = {'a': '1'}
map12 = {'a': map11}
print(map12)
