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
def anticae(strings,num):
    a=list(string.ascii_uppercase)
    b=list(string.ascii_lowercase)
    result = []
    for char in strings:
        if char in a:
            idx = a.index(char)
            result.append(a[abs(26-num+idx)%26])
        elif char in b:
            idx=b.index(char)
            result.append(b[abs(26-num+idx)%26])
        else:
            result.append(char)
    return ''.join(result)

co_code =int(input("输入0进入凯撒加密，输入1进入凯撒解密:"))
if co_code == 0:
    print("欢迎使用凯撒加密v1.0")
    strings = str(input("先输入你要加密的字符串:"))
    num = int(input("输入偏移量:"))
    print(cae(strings, num))
if co_code == 1:
    print("欢迎使用凯撒解密v1.0")
    strings = str(input("先输入你要解密的字符串:"))
    num = int(input("输入偏移量:"))
    print(anticae(strings, num))




