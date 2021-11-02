#                                        """Practice work of all summery"""

class employee():
    leave=8

    def __init__(self,name,stand):
        self.name=name
        self.stand=stand

    @classmethod
    def stringto(cls,string):
        return cls(*string.split("/"))

    @classmethod
    def newlea(cls,newleave):
        cls.leave=newleave

    @staticmethod
    def ood(string):
        print("hi ama i  "+ string)



har=employee("harry",4)
rohan=employee.stringto("rohan/4")
employee.newlea(5)

print(har.name)
print(rohan.stand)

print(rohan.leave)

rohan.ood("ji kasi ho mst hai sab")









#                            Real work
#
# class Employee:
#     no_of_leaves = 8
#     var = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)
#
#
# class player:
#     var=7
#     def __init__(self,name,game):
#         self.name=name
#         self.game=game
#
#     def detail(self):
#         return f"the name of game is {self.game} and player is {self.name}"
#
# class coolprogrammer(Employee, player):
#     language="c++"
#     def pinlanguage(self):
#         print(self.language)
#
# harry=Employee("Harry","hhj",33)
#
# karan=coolprogrammer("karan","hiioo",9)
#
# shubham=player("Shubham",["cricket"])
#
# print(karan.var)
# print(harry.name)
# print(karan.printdetails())
# print(karan.pinlanguage())
# print(shubham.detail())
# print(shubham.game)
# karan.pinlanguage()







#                   Inhertance multilevel


# class dad:
#     basketball=6
#
# class son(dad):
#     dance=2
#     basketball = 2
#     def isdance(self):
#         return f"tes i can dance {self.dance} no of time"
#
# class grandson(son):
#     dance=7
#     guitor=2
#
#     def isdance(self):
#         return f"jack son can dance {self.dance} no of time"
#
# darry=dad()
# larry=son()
# harry= grandson()
#
# print(harry.dance)
# print(harry.isdance())
#
#










                               # pubic , protected , private indicator= "___"

class Employee:
    no_of_leaves = 8
    var = 8
    __protectedsinger = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class coolprogrammer(Employee):
    language="c++"
    def pinlanguage(self):
        print(self.language)

harry=Employee("Harry","hhj",33)

emp=coolprogrammer("harry",3432,"hhs")
# print(emp._protectedsinger)
print(emp._Employee__protectedsinger)