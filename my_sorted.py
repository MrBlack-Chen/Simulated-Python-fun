import copy
def my_sorted(itera,key=None,reverse=False):
    '''itera must be an iterable object
        key can be a function to handle the itera, default None
        reverse is an ascending order or not, default False'''
    flag=1
    if key:
        tmp=copy.deepcopy(itera)
        res=list(map(key,itera))
    elif isinstance(itera,dict):
        res=list(itera.keys())
    else:
        res=list(itera)
    lenth=len(res)-1
    for i in range(lenth):
        for j in range(lenth-i):
            if res[j]>res[j+1]:
                res[j],res[j+1]=res[j+1],res[j]
                flag=0
        if flag:
            break
    if key:  #对res进行key函数的逆运算，从而恢复原数据，但不改变排序
        for item in tmp:
            tmp2=key(item)
            if tmp2 in res:
                res[res.index(tmp2)]=item
    if reverse:
        return res[::-1]
    else:
        return res

