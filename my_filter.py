def my_filter(fun,itera):
    res=[]
    for item in itera:
        if fun(item):
            res.append(item)
    return res
