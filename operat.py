#print("5+6=",5+6)
#print(15/6)
#print(15//6)
#print(3**2)#power
#print(3*2)#multiply
#print(5%5)#modulus or divided remander remain
#print(15%2)#modulus or divided remander remain
x=32
y=2
c=sum((x,y))
print(c)


def function1(a,b):
    print("hello you are in function",a+b)

function1(5,8)
function1(9,8)

def function2(a,b):
    """this is a function"""
    average=(a+b)/2
    print(average)
function2(2,2)
function2(5,8)
print(function2.__doc__)
