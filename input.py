message = input("请输入\n")
print(message)
prompt = "if you"
prompt += "\n very good\n"
name = input(prompt)
print(name)

age = input("How old are you?")
age = int(age)

print(age > 18)

if age > 18:
    print("这个人成年了")
else:
    print("这个人未成年")

num = input("请输出一个数字:")

num = int(num)
if num % 10 == 0:
    print(f"{num}:这数是10的整数")
else:
    print(f"{num}:这个数不是10的证书")
