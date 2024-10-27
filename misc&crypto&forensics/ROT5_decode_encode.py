# ROT5用于只用于数字旋转


def rot5(text):
    result = []
    for char in text:
        if '0' <= char <= '9':
            result.append(chr((ord(char) - ord('0') + 5) % 10 + ord('0')))
        else:
            result.append(char)
    return ''.join(result)


text = "12345" # 输入你要操作的原始数据
rot5_encoded = rot5(text)

print("Original (ROT5):", text)
print("Encoded (ROT5):", rot5_encoded)  # 67890