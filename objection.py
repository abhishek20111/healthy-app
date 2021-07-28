# class Employee:
#     leave=8
#
#     def __init__(self, aname, asalary, arole):
#          self.name=aname
#          self.salary=asalary
#          self.role=arole
#
#     def printdetails(self):
#          return f"name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#
#
# harry=Employee("harry",30000,"instructor")
# rohan=Employee("rohan",50000,"manager assistant")
#
# print(harry.printdetails())
# print(harry.salary)
# print(rohan.__dict__)
# print(rohan.printdetails())
# print(rohan.__dict__)








# class employee():
#     leave=8
#
#     def __init__(self,aname,arole,asalary):
#         self.name=aname
#         self.role=arole
#         self.salary=asalary
#
#     @classmethod
#     def chane_leave(cls,newleave):
#         cls.leave=newleave
#
# harry=employee("harry","inductor",9000000)
# harry.chane_leave(23)
#
# print(harry.leave)






# class employee():
#     leave=8
#
#     def __init__(self,aname,arole,asalary):
#         self.name=aname
#         self.role=arole
#         self.salary=asalary
#
#     @classmethod
#     def change_leave(cls,newleave):
#         cls.leave=newleave
#
#     @classmethod
#     def from_str(cls,string):
#         # param=string.split(("-"))
#         # print(param)
#         # return cls(param[0],param[1],param[2])
#         return cls(*string.split("-"))
#
# harry=employee("harry","inductor",30000000)
# rohan=employee.from_str("Rohan-Manager-900000000")
#
# print(harry.role)
# print(rohan.salary)













# class student():
#     leave=3
#     def __init__(self,aname,astander):
#         self.name=aname
#         self.stander=astander
#
#     @classmethod
#     def from_string(cls,string):
#         return cls(*string.split("-"))
#
#     @classmethod
#     def change_leave(cls,newleave):
#         cls.leave=newleave
#
#
# abhishek=student("Abhishek","8")
# nisha=student.from_string("Nisha-7")
#
# abhishek.change_leave(6)
#
# print(abhishek.leave)
# print(abhishek.name)
#
# print(nisha.name)
# print(nisha.stander)









# practice

class student():
    leave=12
    teacher=8

    def __init__(self,aname,astander,abeacher):
        self.name=aname
        self.stander=astander
        self.beacher=abeacher


    def details(self):
        return f"the name is {self.name} .And the salary is {self.stander} . And as {self.beacher} in company"


    @classmethod
    def string_class(cls,string):
        return cls(*string.split("-"))

    @classmethod
    def change_leave(cls,newleave):
        cls.leave=newleave

    @classmethod
    def change_teacher(cls,newteacher):
        cls.teacher=newteacher

    # # @staticmethod
    # # def good(string):
    # #     print("this is a  "+string)


abhishek=student.string_class("Abhishek-11-Nisha")
abhishek.change_leave(18)

# # abhishek.good("boy")

nisha=student.string_class("Nisha-10-Abhishek")
# print(nisha.teacher,"  nisha teacher")
# print(student.teacher,"  studdent teacher ")
student.change_teacher(5)
# print(nisha.teacher, "  teacher nisha change")
# print(student.teacher,"  student techare change")

karan=student("Karan",0,"abhishek")

# print(karan.name)
# print(karan.beacher)
#
# print(abhishek.name)
# print(abhishek.beacher)
#
# print(nisha.name)
# print(nisha.beacher)
#
# print(abhishek.leave)







class programmer(student):

    def __init__(self,name,stander,becher,lan):
        self.name=name
        self.stander=stander
        self.becher=becher
        self.lan=lan

    def progress(self):
        return f"the name is {self.name} .And the salary is {self.stander} . And as {self.beacher} in company , And programm are {self.lan}"

ram=student.string_class("Ram-4-lula")
print(ram.beacher,  " = ram beache")
print(ram.name, " = ram name")

nunu=programmer("Nunu",4,"hjhd","python")
print(nunu.name, "  = nunu name")

# print(ram.details())
su=nunu.progress()
print(su)










