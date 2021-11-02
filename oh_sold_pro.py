# user=["ani","nina","kitta","jina"]
# temp=["suna","fula","kitta","suiia"]
# for i in range(0,len(user)):
#     tempwer="computer is {} as a billing {}"
#     print(tempwer.format(user[i],temp[i]))


                                                # Oh soldier program
import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i +=1

soldier(r"C:\Users\kushwaha\Pictures",r"C:\Users\kushwaha\PycharmProjects\untitled2\oh_sold_pro.py\ext.txt",".jpg")

pass