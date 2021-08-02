# --- Python Mini Project - Library Management System -----
# Create list_of_books.txt file
# List of books :

# import datetime
# import os
#
# os.getcwd()
#
#
# class LMS:
#     def __init__(self, list_of_books, library_name):
#         self.list_of_books = "list_of_books.txt"
#         self.library_name = library_name
#         self.books_dict = {}
#         id = 101
#         with open(self.list_of_books) as b:
#             content = b.readlines()
#         for line in content:
#             self.books_dict.update({str(id): {'books_title': line.replace("\n", ""), 'lender_name': '', 'lend_date': '','status': 'Available'}})
#             id += 1
#
#     def display_books(self):
#         print("------------------------List of Books---------------------")
#         print("Books ID", "\t", "Title")
#         print("----------------------------------------------------------")
#         for key, value in self.books_dict.items():
#             print(key, "\t\t", value.get("books_title"), "- [", value.get("status"), "]")
#
#     def Issue_books(self):
#         books_id = input("Enter Books ID : ")
#         current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         if books_id in self.books_dict.keys():
#             if not self.books_dict[books_id]['status'] == 'Available':
#                 print(
#                     f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
#                 return self.lend_books()
#             elif self.books_dict[books_id]['status'] == 'Available':
#                 your_name = input("Enter Your Name : ")
#                 self.books_dict[books_id]['lender_name'] = your_name
#                 self.books_dict[books_id]['lend_date'] = current_date
#                 self.books_dict[books_id]['status'] = 'Already Issued'
#                 print("Book Issued Successfully !!!\n")
#         else:
#             print("Book ID Not Found !!!")
#             return self.Issue_books()
#
#     def add_books(self):
#         new_books = input("Enter Books Title : ")
#         if new_books == "":
#             return self.add_books()
#         elif len(new_books) > 20:
#             print("Books title length is too long !!! Title length limit is 20 characters")
#             return self.add_books()
#         else:
#             with open(self.list_of_books, "a") as b:
#                 b.writelines(f"{new_books}\n")
#             self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_books, 'lender_name': '',
#                                                                          'lend_date': '', 'status': 'Available'}})
#             print(f"The books '{new_books}' has been added successfully !!!")
#
#     def return_books(self):
#         books_id = input("Enter Books ID : ")
#         if books_id in self.books_dict.keys():
#             if self.books_dict[books_id]['status'] == 'Available':
#                 print("This book is already available in library. Please check book id. !!! ")
#                 return self.return_books()
#             elif not self.books_dict[books_id]['status'] == 'Available':
#                 self.books_dict[books_id]['lender_name'] = ''
#                 self.books_dict[books_id]['lend_date'] = ''
#                 self.books_dict[books_id]['status'] = 'Available'
#                 print("Successfully Updated !!!\n")
#         else:
#             print("Book ID Not Found !!!")
#
#
# if __name__ == "__main__":
#     try:
#         mylms = LMS("list_of_books.txt", "Python's")
#         press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
#
#         key_press = False
#         while not (key_press == "q"):
#             print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
#             for key, value in press_key_list.items():
#                 print("Press", key, "To", value)
#             key_press = input("Press Key : ").lower()
#             if key_press == "i":
#                 print("\nCurrent Selection : ISSUE BOOK\n")
#                 mylms.Issue_books()
#
#             elif key_press == "a":
#                 print("\nCurrent Selection : ADD BOOK\n")
#                 mylms.add_books()
#
#             elif key_press == "d":
#                 print("\nCurrent Selection : DISPLAY BOOKS\n")
#                 mylms.display_books()
#
#             elif key_press == "r":
#                 print("\nCurrent Selection : RETURN BOOK\n")
#                 mylms.return_books()
#             elif key_press == "q":
#                 break
#             else:
#                 continue
#     except Exception as e:
#         print("Something went wrong. Please check. !!!")










# import os
# import datetime
# os.getcwd()
#
# class LMS:
#     def __init__(self,list_of_books,list_of_liberary):
#         self.list_of_books="list_of_books.txt"
#         self.list_of_liberary=list_of_liberary
#         self.list_detail={}
#         id = 10947
#         with open(self.list_of_books) as f:
#             content = f.readlines()
#         for line in content:
#             self.list_detail.update({str(id):{'book_title':line.replace("\n",""),'lender_name':'','lender_date':'','status':'Available'}})
#             id += 1
#
#     def Display_Book(self):
#         print("_______________________Welcome_________________")
#         print("Book ID:","\t","Title")
#         print("-----------------------------------------------")
#         for key , value in self.list_detail.items():
#             print(key,"\t\t",value.get("book_title"),"- [",value.get("status"),"]")
#
#     def Issue_books(self):
#         book_id = input("Enter book ID")
#         current_date = datetime.datetime.now()
#         if book_id in self.list_detail.keys():
#             if not self.list_detail[book_id]['status'] == 'Available':
#                 print(f"Book is already Issued to {self.list_detail[book_id]['lender_name']} in  {self.list_detail[book_id]['lender_date']}")
#                 return Issue_books()
#                 # return lend_books()
#             elif self.list_detail[book_id]['status'] == 'Available':
#                 your_name = input("Enter your name")
#                 self.list_detail[book_id]['lender_name'] = your_name
#                 self.list_detail[book_id]['lender_date'] = current_date
#                 self.list_detail[book_id]['status'] = 'Already Issued'
#                 print("Book Issued Scuccesfully !!!\n")
#
#             else:
#                 print("Book ID not FOUND")
#                 return self.Issue_books()
#
#     def add_books(self):
#         new_books = input("Enter book name")
#         if new_books == '':
#             return self.add_books()
#         elif len(new_books) > 20:
#             print("The book name is too long")
#             return self.add_books()
#         else:
#             with open(self.list_of_books,"a") as b:
#                 b.writelines(f"{new_books}\n")
#                 self.list_detail.update({str(int(max(self.list_detail)) + 1):{'books_title': new_books, 'lender_name': '','lender_date': '', 'status': 'Available'}})
#                 print(f"The book '{new_books}' has been added successfully!!!")
#
#     def return_book(self):
#         book_id = input("Enter Books ID")
#         if book_id in self.list_detail.keys():
#             if self.list_detail[book_id]['status'] == 'Available':
#                 print("This book is already avilable in liberary check ID again")
#                 return self.return_book()
#             elif not self.list_detail[book_id]['status'] == 'Available':
#                 self.list_detail[book_id]['lender_name'] = ''
#                 self.list_detail[book_id]['lender_date'] = ''
#                 self.list_detail[book_id]['status'] = 'Available'
#                 print("Successfully update -----\n")
#
#             elif not self.list_detail[book_id]['status']=='Available':
#                 print("Book ID not found")
#
# if __name__ == '__main__':
#     # try:
#     myclass = LMS("list_of_books.txt","Python's")
#     press_key_list = {"D":"Display Book","I":"Issue Book","A":"Add Books","R":"Return Books","Q":"Quit"}
#
#     key_press = False
#     while not (key_press=="q"):
#         print(f"\n-------Welcome to {myclass.list_of_liberary}'s Mangement System-------------\n")
#         for key,value in press_key_list.items():
#             print("Press",key,"to",value)
#
#         key_press = input("Press key : ").lower()
#         if key_press == 'i':
#             print("\nCurrent selection : Issued book\n")
#             myclass.Issue_books()
#         elif key_press == 'a':
#             print("\nCurrent selection : Add book\n")
#             myclass.add_books()
#         elif key_press == 'd':
#             print("\nCurrent selection : Display book\n")
#             myclass.Display_Book()
#         elif key_press == 'r':
#             print("\nCurrent selection : Return book\n")
#             myclass.return_book()
#         elif key_press =="q":
#             break
#         else:
#             continue
#     # except Exception as e:
#     #     print("Something went wrong \nMay be---",e)
