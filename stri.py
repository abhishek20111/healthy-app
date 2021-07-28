
def fun(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"(keys) are in (value)")
    normal="dfgf ghfh"
    har=["harry","rohan","sdf","fsfffffsd"]
    d=["sdf":"hgh","sdfs":"jhg","fsdf":"fgfgh","sdffd":"ghfg"]
fun(normal,*har,**d)





