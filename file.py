if __name__ == '__main__':
    print("aa")

# 读取文件
with open('wenjian.txt') as file:
    contents = file.read()
print(contents)

# 逐行读取
with open('wenjian.txt') as file:
    i = 0
    for line in file:
        i = i+1
        print(f"第{i}行", line.strip())


# 读取文件到列表
with open('wenjian.txt') as file:
    content = file.readlines()
print(content)

# 读取文件到列表去掉空格
with open('wenjian.txt') as file:
    content = file.readlines()
for cc in content:
    print(cc.strip())

# 判断输入的数字是否在文件中
with open('wenjian.txt') as file:
    contents = file.read()
shuzi = input("请输入数字:")
if shuzi in contents:
    print(f"输入的数字:{shuzi}包含在文件中")
else:
    print(f"输入的数字:{shuzi}不在文件中")


# 写入文件 mode读取模式('r')、写入模式('w')、附加模式('a')或读写模式('r+')
file_name = "write.file"
with open(file_name, mode='w') as write_file:
    write_file.write("write file test")

with open(file_name, mode='a') as write_file:
    write_file.write("\nwrite file test zhuijia")

try:
    print(5/0)
except ZeroDivisionError:
    print("发生异常了")

# try执行成功则执行else中的代码
try:
    aa = 5/1
except ZeroDivisionError:
    print("error")
else:
    print(int(aa))

# 文件不存在的异常
try:
    with open("aa.text") as aa:
        content = aa.read()
except FileNotFoundError:
    print("文件不存在")
else:
    print("文件存在")


# 文件不存在的 静默
try:
    with open("aa.text") as aa:
        content = aa.read()
except FileNotFoundError:
    pass
else:
    print("文件存在")






