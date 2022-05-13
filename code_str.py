#字符串加密解密(利用itertools模块的cycle函数来实现根据秘钥循环加密)
from itertools import cycle
def code_str(s,key):
    keys=cycle(key)
    res=''
    for ch in s:
        res=res+chr(ord(ch)^ord(next(keys)))
    #return ''.join(map(lambda ch,item:chr(ord(ch)^ord(item)),s,cycle(key))) 函数调用过多效率会较低
    return res

if __name__ == "__main__":
    s=input("请输入加密字符或解密字符:>")
    key=input("请输入秘钥:>")
    print(code_str(s,key))
