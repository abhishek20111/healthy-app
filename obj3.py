# class employee():
#     def __init__(self,name,salary,role):
#         self.name=name
#         self.salary=salary
#         self.role=role
#
#     def __add__(self, other):
#         return self.role+other.role
#
#     def __truediv__(self, other):
#         return self.salary/other.salary
#
#     def __pow__(self, power, modulo=None):
#         return self.salary**power.salary
#
#     def __repr__(self):
#         return f"the name is [ {self.name}, {self.salary} , {self.role} ]"
#
# emp1=employee("hiroshi",40,"suar")
# emp2=employee("hritik",3,"hu")
# print(emp1+emp2)
# print("devide",emp1/emp2)
# print("power",emp1**emp2)
# print(emp1.__repr__())




# from abc import ABC,abstractmethod
#
# class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#
# class laptop(computer):
#     def process(self):
#         pass
#
# comp1=laptop()

















class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"the employee is {self.fname}  {self.lname}"

    def printemail(self):
        return f"email is {self.fname}.{self.lname}@gmail.com"

    @printemail.setter
    def email(self,string):
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]

hi=employee("hinduatan","ji")
ni=employee("niki","ja")

print(hi.fname)
print(hi.email)
print(ni.email)

hi.fname="Us"
print(hi.email)
print(hi.printemail())

# hi.email="this.that@gmail.com"
# print(hi.fname)


