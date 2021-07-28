# def fact_ite(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# no=int(input("enter no"))
#
# print(fact_ite(no))


# for recursive method

# def fact_rec(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact_rec(n-1)
# no=int(input("enter no"))
# print("factoial",fact_rec(no))


#fabonicci series by recursive method
# def fab(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# no=int(input("enter no"))
#
# print(fab(no))



#iterative method for factorial

# def fact(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# no=int(input("enter the no"))
# print(fact(no)
#


# fabonacci series
def fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

no=int(input("enter the no"))

print(fab(no))