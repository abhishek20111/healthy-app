# import argparse
# import sys
#
# def cal(arg):
#     if arg.o=='add':
#         return arg.x + arg.y
#     elif arg.o=='mul':
#         return arg.x * arg.y
#     elif arg.o=='sub':
#         return arg.x - arg.y
#     elif arg.o=='div':
#         return arg.x / arg.y
#     else:
#         print("something wrong error 404")
#
# if __name__ == '__main__':
#     parsaer = argparse.ArgumentParser()
#     parsaer.add_argument('--x',type=float, default=1.0 , help="for help contact whitecoder")
#     parsaer.add_argument('--y',type=float, default=2.0 , help="for help contact whitecoder")
#     parsaer.add_argument('--o',type=str, default='add', help="for help contact whitecoder")
#
#     arg=parsaer.parse_args()
#     sys.stdout.write(str(cal(arg)))

#                                 Practice

# import argparse
# import sys
#
# def cal(args):
#     if args.o== 'add':
#         return args.x + args.y
#     elif args.o== 'mul':
#         return args.x * args.y
#     elif args.o== 'div':
#         return args.x / args.y
#     elif args.o== 'sub':
#         return args.x - args.y
#     else:
#         return "Error 404"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,help='Enter first no, For queston contact whitecoder')
#     parser.add_argument('--y',type=float,default=2.0,help='Enter second no, For queston contact whitecoder')
#     parser.add_argument('--o',type=str,default='add',help=' For queston contact whitecoder')
#     args = parser.parse_args()
#     sys.stdout.write(str(cal(args)))





                                                  # Pratice faluty calculator by command  line utility
import argparse
import sys

def calculate(args):
    if args.c == '+':
        if args.a == 26 and args.b == 26:
            return 22
        else:
            return args.a + args.b
    elif args.c == '-':
        if args.a == 45 and args.b == 2:
            print("455")
        else:
            print(args.a - args.b)
    elif args.c == '/':
        if args.a == 23 and args.b == 76:
            print("2")
        else:
            print(args.a / args.b)
    elif args.c == '*':
        if args.a == 1 and args.b == 455:
            print("5")
        else:
            print(args.a * args.b)
    else:
        print("your something is fault")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--a",type=float,default=1.0,help="he you can take your own help, First no")
    parser.add_argument("--b",type=float,default=2.0,help="he you can take your own help, Second no")
    parser.add_argument("--c",type=str,default='+',help="he you can take your own help, Give opertor")
    args = parser.parse_args()
    sys.stdout.write(str(calculate(args)))



