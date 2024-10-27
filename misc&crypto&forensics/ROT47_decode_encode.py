# ROT47适用于ASCII 33到126


def rot47(text):
    result = []
    for char in text:
        if 33 <= ord(char) <= 126:
            result.append(chr(33 + (ord(char) - 33 + 47) % 94))
        else:
            result.append(char)
    return ''.join(result)

# 示例
text = "Hello, World!"
rot47_encoded = rot47(text)

print("Original (ROT47):", text)
print("Encoded (ROT47):", rot47_encoded)  # 编码结果
print("Decoded (ROT47):", rot47(rot47_encoded))  # 解码结果