import hashlib

def get_signature(timestamp, nonce, app_secret):
    # 对 token, timestamp, nonce 按字典排序
    param_arr = [app_secret, timestamp, nonce]
    param_arr.sort()

    # 将排序后的结果拼接成一个字符串
    content = ''.join(param_arr)

    # 对拼接后的字符串进行 SHA-1 加密
    sha1 = hashlib.sha1()
    sha1.update(content.encode('utf-8'))
    ciphertext = sha1.hexdigest()

    return ciphertext

# 示例用法
timestamp = "your_timestamp"
nonce = "your_nonce"
app_secret = "your_app_secret"

signature = get_signature(timestamp, nonce, app_secret)
print(signature)