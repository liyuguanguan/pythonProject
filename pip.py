import os

# 需要安装的库
libs = ["Pillow"]
# 指定版本号
# libs = ["requests==版本号", "beautifulsoup4==版本号", "matplotlib==版本号", "wordcloud==版本号", "pandas", "pillow", "openpyxl"]


# 循环遍历安装
for lib in libs:
    os.system("pip install " + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple")

print("dsadsa")
