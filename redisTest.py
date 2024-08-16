import json
import pickle

import redis
from PIL import Image
# 测试
r = redis.Redis(host='r-2ze11fjvcdhq5rg9lx.redis.rds.aliyuncs.com',port=6379,password='bgr-JXF6yqj8xac4awt',db=5)
# 生产
# r = redis.Redis(host='r-2ze2asukejqltkxywt.redis.rds.aliyuncs.com',port=6379,password='!@#Neolix@2018',db=6)

aa = r.get(100024170227)
# print(aa.decode())
# print(json.dumps(aa))
# bb = b'\xac\xed\x00\x05sr\x00\x11java.lang.Integer\x12\xe2\xa4\xf7\x81\x878\x02\x00\x01I\x00\x05valuexr\x00\x10java.lang.Number\x86\x95\x1d\x0b\x94\xe0\x8b\x02\x00\x00xp\x00\x00\x00\x00'
# print(aa)
print(aa)
# pickle.loads(aa)
#
# contents = ''
# with open(aa,'rb') as f:
#     contents = f.read()
print(aa.decode("ISO-8859-1"))
# print(json.dumps(contents))

