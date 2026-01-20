import string
def cae(strings,num):
    a=list(string.ascii_uppercase)#大写A~Z元素列表
    b=list(string.ascii_lowercase)
    result = []
    for char in strings:
        if char in a:
            idx=a.index(char)
            result.append(a[(idx+num)%26])
        elif char in b:
            idx=b.index(char)
            result.append(b[(idx+num)%26])
        else:
            result.append(char)
    return ''.join(result)
print("欢迎使用凯撒加密v1.0")
strings = str(input("先输入你要加密的字符串:"))
num = int(input("输入偏移量:"))
print(cae(strings, num))

