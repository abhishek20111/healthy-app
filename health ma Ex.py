# # # Health Management System
# # client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
# # log_list = {1: "Exercise", 2: "Diet"}
# #
# #
# # def getdate():
# #     import datetime
# #     return datetime.datetime.now()
# #
# #
# # try:
# #     print("Select Client Name:")
# #     for key, value in client_list.items():
# #         print("Press", key, "for", value, "\n", end="")
# #     client_name = int(input())
# #
# #     print("Selected Client : ", client_list[client_name], "\n", end="")
# #
# #     print("Press 1 for Log")
# #     print("Press 2 for Retrieve")
# #     op = int(input())
# #
# #     if op is 1:
# #         for key, value in log_list.items():
# #             print("Press", key, "to log", value, "\n", end="")
# #         log_name = int(input())
# #         print("Selected Job : ", log_list[log_name])
# #         f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
# #         k = 'y'
# #         while (k is not "n"):
# #             print("Enter", log_list[log_name], "\n", end="")
# #             mytext = input()
# #             f.write("[ " + str(getdate()).replace(":", "-") + " ] : " + mytext + "\n")
# #             k = input("ADD MORE ? y/n:")
# #             continue
# #         f.close()
# #     elif op is 2:
# #         for key, value in log_list.items():
# #             print("Press", key, "to retrieve", value, "\n", end="")
# #         log_name = int(input())
# #         print(client_list[client_name], "-", log_list[log_name], "Report :" , "\n", end="")
# #         f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
# #         contents = f.readlines()
# #         for line in contents:
# #             print(line, end="")
# #         f.close()
# #     else:
# #         print("Invalid Input !!!")
# # except Exception as e:
# #     print("Wrong Input !!!, Error is - ",e)
#
#
#
#
#                             practice part 1
#
# list_client={1:"Iarry",2:"Rohan",3:"Hammed"}
# list_exd={1:"Excercise",2:"Diet"}
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# try:
#     print("Select Client Name:")
#     for key,value in list_client.items():
#         print("press ",key," for ",value,"\n")
#     key_no=int(input())
#
#     print("selectd name :",list_client[key_no])
#
#     print("Press 1 for Log")
#     print("Press 2 for Retrieve")
#     op = int(input())
#
#     if op is 1:
#         for key,value in list_exd.items():
#             print("press ",key," for ",value,"\n")
#
#         exd1=int(input())
#         print("selected option ",list_exd[exd1])
#         f=open(list_client[key_no]+"_"+list_exd[exd1]+".txt","a")
#         k='y'
#         while (k is not "n"):
#             print("Enter ",list_exd[exd1],"\n")
#             mytext = input()
#             f.write("[" + str(getdate()).replace(":","-") + "]"+ mytext+"\n")
#             k=input("For add : y/n")
#             continue
#         f.close()
#     elif op is 2:
#         for key,value in list_exd.items():
#             print("press ",key ,"to retrive ",value,"\n")
#         exd1=int(input())
#         print(list_client[key_no],"-",list_exd[exd1],"Report is :\n")
#         f = open(list_client[key_no] + "_" + list_exd[exd1] + ".txt", "rt")
#         cont=f.read()
#         for line in cont:
#             print(line, end="")
#         f.close()
#
#     else:
#         print("Invalid Input!!")
# except Exception as c:
#     print(c)




#                 Pratice of same as above

list_name={1:"abhi",2:"kabhi",3:"sabi"}
list_work={1:"Exercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Enter 1,2,3\n","1:Abhi","2:Kabhi","3:Sabhi")
    name_value=int(input())

    print(list_name[name_value], ":")

    print("Enter 1,2\n1:log\n2:Retweet")
    lor={1:"Log",2:"Retwet"}
    op=int(input())

    print(list_name[name_value], "  choice to", lor[op])

    if op is 1:
        for key,value in list_work.items():
            print("Enter ",key," for ",value)
        log_ex_die=int(input())
        print("You are ",list_name[name_value]," and want to log ",list_work[log_ex_die])
        fil=open(list_name[name_value]+"_"+list_work[log_ex_die]+".txt","a")
        k='y'
        while(k is not "n"):

            print("enter Exercise Name ")
            text=input()
            fil.write("["+str(getdate()).replace(":","-")+"]"+text+"\n")
            k=input("Enter to add more or not : y/n")
            continue
        fil.close()

    elif op is 2:
        for key,value in list_work.items():
            print("Enter ", key, " for ", value)
        log_ex_die=int(input())
        print("You are ",list_name[name_value]," and you want to retreve ",list_work[log_ex_die])
        fil = open(list_name[name_value] + "_" + list_work[log_ex_die] +".txt","rt")
        mytxt=fil.read()
        print(mytxt)
        fil.close()

    else:
        print("Invalid input")

except Exception as kd:
    print("Reasion is \n",kd)