# def fact(x):
#     a = 1
#     b = 1
#     if x == 0:
#         a = 1
#     if x < 0:
#         print('enter valid whole number!')
#     if x > 0:
#         while b < x:
#             a = a * b
#             b += 1
#     yield a
# #main
# z = input('Enter a number')
# g = (fact(n) for n in range (0,int(z)))
# print(next(g))





#                       Factorial till no
# def factorials_up_to(x):
#     a = 1
#     for i in range(1, x+1):
#         a *= i
#         yield a
# n=int(input("enter no"))
# for x in factorials_up_to(n):
#     print(x)









# list=[i for i in range(51) if i%2==0]
# print(list)
# dict1={i:f"item{i}" for i in range (2,100)}
# print(dict1)
#
# dresses={dress for dress in ["dress1","dress2","dress3"]}
# print(dresses)
#
# even=(i for i in range(100) if i%2==0)
# print(even.__next__())
#















khana=["roti","sabazi","chwal"]
for item in khana:
    # print(item)

    if item == "roiti":
        break

else:
    print("this for end ")








import time
def some_work(n):

    time.sleep(n)