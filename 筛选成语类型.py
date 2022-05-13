import re
def is_need(s, flag):
    if flag == "AABB":
        pattern = r"((.)\2(.)\3)，"
        res=re.findall(pattern,s)
    elif flag == "AABC":
        pattern = r"((.)\2(.)(?!\3).)，"
        res=re.findall(pattern,s)
    elif flag == "ABCC":
        pattern = r"((.)(?!\2).(.)\3)，"
        res=re.findall(pattern,s)
    elif flag == "ABAC":
        pattern=r"((.)(?!\2)(.)\2(?!\3).)，"
        res=re.findall(pattern,s)
    elif flag == "ABCB":
        pattern = r"((.)(.)(?!\2).\3)，"
        res=re.findall(pattern,s)
    else:
        print("该成语类型不存在，请检查筛选类型是否输入正确")
        return
    for item in res:
        print(item[0])
 

if __name__ == "__main__":
    s=input("请输入要筛选的成语:>")
    flag=input("请输入筛选的类型(如AABB):>")
    is_need(s,flag)
