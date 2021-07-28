x=int(input("enter your age"))
if x<4:
    print("invalid age for driving")
elif 4<x<18:
    print("to small to drive")
elif 18==x:
    print("we decide after seeing the driving skill")
elif 18<x<90:
    print("you can get your licence")
else:
    print("you enter wrong age not possible for driving")


l={1,2,3,4,5,6,7}
if x in l:
    print("yes you are won")
if x not in l:
    print("sorry you loose")