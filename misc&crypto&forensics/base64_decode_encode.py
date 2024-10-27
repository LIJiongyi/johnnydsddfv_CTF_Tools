# base64，结果为先编码后解码



import base64

# 要编码的原始数据
data = "Hello, World!"
# 将字符串编码为字节
byte_data = data.encode('utf-8')

# 进行Base64编码
encoded_data = base64.b64encode(byte_data)

# 打印编码后的数据
print("Encoded:", encoded_data.decode('utf-8'))
# 进行Base64解码
decoded_data = base64.b64decode(encoded_data)

# 打印解码后的数据
print("Decoded:", decoded_data.decode('utf-8'))