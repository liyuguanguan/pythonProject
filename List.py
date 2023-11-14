if __name__ == '__main__':
    list1 = ['21', 'ff']
    print(list1[1].title())
    # -1是最后一个节点，从后面开始数
    print(list1[-1].title())
    message = f"aa {list1[1]}"
    print(message)
    # 替换列表中的值
    list1[1] = 'dd'
    print(message)
    # 向末尾添加元素
    list1.append("dsa")
    print(list1)
    # 向任意位置添加元素
    list1.insert(1, 'd')
    print(list1)
    # 删除元素
    del list1[0]
    print(list1)
    # 弹出并使用列表的任意元素的值
    print(list1.pop(0))
    # 删除等于这个值的元素 只删除第一次遇到的这个值，如果这个列表有多个相同的值，只会删除第一次遇到的
    print(list1.remove('dd'))
    list2 = ['vv', 'aa']
    # 排序
    list2.sort(reverse=True)
    print(list2)
    # sorted 会保存list2的值创建一个新的列表
    print(sorted(list2, reverse=True))
    # 翻转列表元素
    list2.reverse()
    print(list2)
    # 列表长度
    print(len(list2))
    # 遍历列表
    for aa in list2:
        print(aa)
    aaa = 'a'
    bbb = 'a'
    print(aaa == bbb)
    for ran in range(1, 4):
        print(ran)
    # 创建一个 1-3的列表
    print(list(range(1, 4)))
    # 创建一个的列表 数值从1开始 每次加2,直到小于30
    print(list(range(1, 30, 1)))
    sq = []
    for value in range(1, 20):
        sq.append(value ** 2)
    print(sq)
    # 同上面的写法是一样的
    sq = [value**2 for value in range(1, 9)]
    print(sq)

    dig = [1, 2, 3, 4]
    print(min(dig))
    print(max(dig))
    print(sum(dig))
    # 创建一个列表，其中包含3～30能被3整除的数，再使用一个for循环将这个列表中的数打印出来
    sqq = [value for value in range(0, 31, 3)]
    print(sqq)
    # 输出0 1 2 的元素 [0, 3, 6]
    print(sqq[0:3])
    # 从头开始到第三个索引
    print(sqq[:3])
    # 从第三个索引开始一直到末尾
    print(sqq[2:])
    # 遍历元素
    for sqqq in sqq[:3]:
        print(sqqq)
    aa = sqq[:]
    print(aa)
    print(*map(str, sqq))

    # 这种赋值是把aaaa的地址 赋值给bbbb，所以 aaaa变动了 bbbb也会变动 bbbb变动了aaaa也会变动，因为他们指向的是同一个值
    # 如果想要深copy则需要 用copy方法
    aaaa = ["dd"]
    bbbb = aaaa
    aaaa.append("ccc")
    bbbb.append('bbb')
    print(aaaa)
    print(bbbb)


