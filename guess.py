# n=23
# ta=8
# att=8
# while(True):
#     att-=1
#     u_input=int(input("\n enter the no"))
#     if u_input<n and att>0:
#         print("try again with high value")
#         print("remain guess",att)
#     elif u_input>n and att>0:
#         print("too low")
#         print("no of guess",att)
#         continue
#     elif u_input==n:
#         print("you won , no of guess",ta-att)
#         break
#     else:
#         print("your 8 attemt is over")
#         print("game over")
#         break
#
#
import numpy
for p in numpy.__path__:
    print(p)