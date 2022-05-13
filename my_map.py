def my_map(fun,itera):
    res=[]
    for item in itera:
        res.append(fun(item))
    return res
