#f=open("harry.txt","rt")
#w=f.read(1)
#print(w)

#for line in f:
#    print(line,end=" ")
#    print(f.readlines())


#f.close()



#f=open("jaiho.txt","w")
#a=f.write("jaiho yeh file aur kase ho, sab dik dak\n")
#print(a)
       #                        """it use 'w' to write and when you run it will print same and amke same file"""
#f.close()



# f=open("jaiho.txt","a")
# a=f.write("jaiho yeh file aur kase ho, sab dik dak\n")
# print(a)
#                                      """when you use "a" the line will add and the no of time you run it will add like that only"""
# f.close()
#




# HAndel read and write
#  "r+" =  read and write

f=open("harry.txt","r+")
print(f.read())

f.write("thanks ")
f.close()


f=open("harry.txt")

print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())


print(f.readline())
print(f.tell())
f.seek(25)            #it print the text after the 4 character
print(f.readline(),"yeh seek vala hai\n")
print(f.tell())


f.close()