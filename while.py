if __name__ == '__main__':

    aa = 1
    while aa <= 5:
        print(aa)
        aa += 1

    # 让用户输入特殊指令退出
    # quit = "请输入exit指令退出"
    # message = input(quit)
    # while "exit" != message:
    #     print("输入错误不能退出请重新输入")
    #     message = input(quit)
    # print("成功退出")

    flag = True
    # message1 = "请输入exit指令退出"
    # while flag:
    #     message1 = input(message1)
    #     # 断点
    #     # breakpoint()
    #     if message1=='quit':
    #         flag=False
    #     else:
    #         print("haha"+message1)

    while flag:
        print("break")
        break
    # 将一个列表移动到领一个列表
    list1 = ['a', 'b', 'c', 'd','a']
    list2 = []
    while list1:
        list2.append(list1.pop())
    print(list2)
    print(list1)
    # 删除特定元素 remove只能删除第一个元素
    list3 = ['a', 'b', 'c', 'd','a']

    while 'a' in list3:
        list3.remove('a')
    print("list3", list3)

    # 用while操作map
    haha = True
    map1 = {}
    while haha:
        aaa = input("请输入你的名字")
        bbb = input("请输入你的爱好")
        map1[aaa] = bbb

        if aaa == "小王":
            break
    print(map1)


