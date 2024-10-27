# 输出ROT13编解码


def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

# 示例
original_text = "Hello, World!"
encoded_text = rot13(original_text)
decoded_text = rot13(encoded_text)  # ROT13是对称的

print("Original:", original_text)
print("Encoded (ROT13):", encoded_text)
print("Decoded (ROT13):", decoded_text)