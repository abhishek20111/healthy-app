# import requests
# r=requests.get("https://www.summet.com/dmsi/html/codesamples/addresses.html")
# data=r.text
# print(data)
# print(requests.head)



# import json
# # in this data have keys and value which is in javascript and it convert into dictionary as load function work
# data='{"var1":"harry","var2":34,"var3":"larry"}'
# parsed=json.loads(data)
# print(parsed['var2'])


# data2={1:'Welcome', 2:'to',
#             3:'Geeks', 4:'For',
#             5:{'Geeks':'fiiiu'}}
# # the dump convert dictionary to java dictionary capableml
# https=json.dumps(data2)
# print(https)


# f=open('data.json')
# data=json.load(f)
# for i in data('data2'):
#     print(i)
# f.close()






# __________________________________________________   pickless practice
import pickle
# toys=["cartoon","cars","plan"]
#
# filess=open("mycars.pkl",'wb')
# pickle.dump(toys,filess)
# filess.close()

# f="mycars.pkl"
# fileobj=open(f,'rb')
# mycar=pickle.load(fileobj)
# print(mycar)
# print(type(mycar))


# data={
#     'a':[3,2,1],
#     'b':"nikil",
#     (1,2):[1,2,3]}
# file=open("mycars.pkl",'wb')
# pickle.dump(data,file)


# ____________________   load and dump of pickle cant run together

# oooo=open("mycars.pkl","rb")
# s=pickle.load(oooo)
# print(s)














# ________________________________________Regular Expression Module
import re

# nameage="""Janice is 22 and Thoen is 23
#            Gaberia is 44 and Joey is 21"""
#
# age=re.findall(r'\d{1,3}',nameage)
# name=re.findall(r'[A-Z][a-z]*',nameage)
#
# age_Dict={}
# x=0
# for eachname in name:
#     age_Dict[eachname]=age[x]
#     x +=1
# print(age_Dict)




# if re.search("inform","we can inform him as a document"):
#     print("there is information in the list")



# all_inform =  re.findall("inform","we can inform him as a document")
# for i in all_inform:
#     print(i)






# str = "We are in the bus"
# for i in re.finditer("bus",str):
#     loctup = i.span()
#     print(loctup)








# str="sat,hat,nat,cat"
# allstr=re.findall(r"[shn]at",str)
# print(allstr)





# str="sat,hat,rat,mat,cat"
# all_str=re.findall(r"[a-m]at",str)
# print(all_str)





# Food="hat,rat,mat,sat,nat"
# regix=re.compile("[h]at")
# string_it=regix.sub("food",Food)
# print(string_it)



# rand_str="""
# it is on the
# jackky suratt
# vijjjay off
# so on
# """
#
# print(rand_str)
# siring=re.compile("\n")
# vertic=siring.sub(" ",rand_str)
# print(vertic)










# ranges="1 12 123 1234 12345 123456 1234567"
# print("Matches: ",len(re.findall("\d{6}",ranges)))


# str=re.findall("\d{2,6}",ranges)
# print(len(str))






# phone="""
#       234-653-6673
#       83-378-89
#       """
#
# if re.search("\d{3}-\d{3}-\d{4}",phone):
#     print("it is correct no")
#
# else:
#     print("it is not correct no")







# import requests
# url=requests.get("https://www.summet.com/dmsi/html/codesamples/addresses.html")
# html=url.text
# for_get = re.findall("\(\d{3}\) \d{3}-\d{4}",html)
# for i in for_get:
#     print(i)






# import re
#
# str = """POPULAR MOBILES:Vivo V21e 5GOnePlus Nord 2OPPO Reno 6Redmi Note 10T 5GTecno Camon 17 ProMySmartPrice
# Search millions of products
#
# Mobiles
# Laptops
# TV
# Appliances
# Audio & Accessories
# News & Reviews
# Recharge
# Email us at
# For Media Promotions / Advertisements:
# advertise@mysmartprice.com
# For Affiliate / Merchant Partnerships:
# sales@mysmartprice.com
# For PR / Editorial / Brand Relations
# press@mysmartprice.com
# For Website Feedback / Customer Care:
# hi@mysmartprice.com
# Our registered office
# MySmartPrice
# 4th Floor, GNR's RV Insignia
# Silicon Valley, Image Garden Rd
# Madhapur, Hyderabad – 500081
# Contact us
# Have a question or feedback? Please fill the form below to contact us.
# Name
# Email
#
# Subject
# Message
# Recently Launched Mobiles
# Vivo S10 5GXiaomi Redmi 10Samsung Galaxy S22 UltraSamsung Galaxy M52 5GJiophone NextRealme GT 2 5GApple iPhone 14OnePlus 9T
# Quick Links
# Contact UsAbout MySmartPricePurpose & FeaturesAdvertise With UsPrivacy PolicyTerms of UsePublic Notice
# Our Presence
# google playstore link
#
# MySmartPrice
# © 2021 MySmartPrice Web Technology Private Limited
# Made with ❤ in indian flag
# """
#
# email = re.findall("\w{1,20}.@\w{2,20}.[A-Za-z]{2,3}",str)
# print(email)



                                                          #  Practice

import requests
import re

url = "https://www.mysmartprice.com/contact/"
gets= requests.get(url)
sss = gets.text

email = re.findall("\w{1,20}@\w{1,20}.[A-Za-z]{1,3}",sss)

for i in email:
    print(i)